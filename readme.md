# 📊 Demand Planning IBP Summary with AI  

## 📝 Description  

This project aims to automate forecast error analysis in demand planning, using **Python** and the **OpenAI API** to generate standardized summaries that support **IBP (Integrated Business Planning) meetings**.  

The system allows the user to select a `.csv` file containing forecast, sales, error, and reason by product family, and automatically:  

- Identifies the top N largest errors (from 1 to 5, based on user input).  
- Creates a cleaned and reduced table, optimizing token usage.  
- Sends the data to the OpenAI API for contextualized analysis.  
- Generates a standardized summary (up to 700 tokens) with explanations and insights about the error reasons.  
- Exports the final result in `.txt` format, ready to be used in meetings.  

⚠️ **Note:** All data used in this repository is **fictitious** and only represents an example of application.  

---

## 🚀 Features  

- Select `.csv` files via interface.  
- Automatic processing and selection of the top errors.  
- Integration with the OpenAI API to generate consistent and standardized analyses.  
- Summary reports ready to use in IBP meetings.  
- Final output in `.txt` format for easy sharing.  

---

## 🛠️ Technologies Used  

- **Python 3.10+**  
- **pandas** – data manipulation  
- **tkinter** – file selection (simple interface)  
- **openai** – AI model integration  

---

## 📂 Project Structure  

├── csv/ # Example fictitious CSV files
├── ibp_summary.txt # Generated .txt reports
├── main.py # Main script
├── requirements.txt # Project dependencies
└── README.md # Documentation


---

## ⚙️ Installation  

Clone the repository and install dependencies:  
pip install -r requirements.txt


## ▶️ How to Use
Run the main script:
python main.py

Steps:

Select a .csv file in the expected format (example available in csv/).

Enter the number of errors to analyze (between 1 and 5).

Wait for the analysis and check the generated summary in ibp_summary.txt.

## 📈 Future Extensions
Connect with workflow tools (e.g., n8n, Zapier).

## 📜 License
This project was inspired by activities performed during my professional work, but all the data included here is fictitious and was adapted for educational and portfolio purposes only.
No confidential company information has been used.