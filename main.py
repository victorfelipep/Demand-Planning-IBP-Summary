import pandas as pd
import tkinter as tk
from tkinter import filedialog
from openai import OpenAI

#Set Business OpenAI API Key
client = OpenAI(api_key="DP BIC OPENAI API KEY HERE")

#Function to create a table with the top L5 by error
def lag2_top_table(df, top_l5, ascending=False):
    df['ABS Error'] = abs(df['FORECAST LAG-2'] - df['ACTUAL'])
    df_sort = df.sort_values('ABS Error', ascending=ascending).head(top_l5)

    return df_sort

#Function to get a integer number from input (between 1 and 5):
def get_int_input_1_to_5(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 5:
                return value
            else:
                print("Error: Number should be between 1 and 5.")
        except ValueError:
            print("Error: Input only integer numbers.")


#tkinter file selector set-up
root = tk.Tk()
root.withdraw()

#Select IBP results csv file path with tkinter
error_file = filedialog.askopenfilename(title="Select an IBP results file")

#Read IBP csv file with pandas
error_csv = pd.read_csv(error_file)

#Insert the quantity of top L5 to be analyzed (Max: 5)
top_l5 = get_int_input_1_to_5("Insert the quantity of top L5 to be analyzed (Max: 5): ")

#Get the top lines (L5) by error from the table
top_table = lag2_top_table(error_csv, top_l5)

#Transform top lines table into string
top_table_string = top_table.to_string()

#Set up OpenAI to get the analysis
prompt = (
    "You are an specialist IBP assistant "
    "Your job is to create an IBP meeting summary to be used in Executive and Operative Demand Review Meetings "
    "You'll receive a table with the top L5 by absolute error, and the respective reason "
    "L1 will be the category. HE means stationery from BIC company, FFL means Lighters from BIC and BE means Shavers "
    "You will work in the summary by helping to drive the meeting focused in the top L5 (product family) "
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": top_table_string}
    ],
    max_tokens=700 
)

#Print AI response with meeting summary and save as .txt
print("\n===== IBP SUMMARY =====\n")
summary = response.choices[0].message.content
print(summary)

with open("ibp_summary.txt", "w", encoding="utf-8") as f:
    f.write(summary)

print("\nSummary saved at 'ibp_summary.txt'")