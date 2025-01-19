
# CashCompass

## Overview
The **CashCompass** is a command-line application designed to help users manage their personal finances with ease. Users can add income and expense transactions, view transaction summaries within a specified date range, and generate visual plots to analyze their financial data.

This project is lightweight, stores data in a CSV file, and is ideal for those who prefer a simple, no-frills solution to track their finances.

---

## Features
- **Transaction Tracking:** Add details like date, amount, category (Income/Expense), and description for each transaction.
- **Summary Reports:** View transaction summaries between specific dates, including total income, total expenses, and net savings.
- **Visualization:** Generate plots to visually analyze income and expense trends over time.
- **CSV-Based Storage:** All data is securely stored in a CSV file for long-term access and portability.
- **Error Handling:** Built-in validation for user inputs such as dates, amounts, and categories.

---

## How to Use

### Prerequisites
- Python 3.8 or higher
- The following Python libraries:
  - `pandas`
  - `matplotlib`

Install dependencies using:
```bash
pip install pandas matplotlib
```

## Steps to Run the Application

1. Clone this repository:
```bash
git clone https://github.com/AmeyPimpalkar/CashCompass
```

2. Navigate to the project directory:
```bash
cd CashCompass
```
3. Run the application
```bash
python FinanceTracker.py
```



---

### Application Flow

**1. Adding a Transaction** 

	•	Select “Add a new transaction” from the menu.
	•	Enter the following details:
	•	Date: In dd-mm-yyyy format (leave blank for today’s date).
	•	Amount: Positive value for the transaction.
	•	Category: Select Income or Expense.
	•	Description: An optional description for the transaction.

**2. Viewing Transactions**

	•	Select “View transactions and summary within a date range”.
	•	Enter the start and end dates in dd-mm-yyyy format.
	•	The application will:
	•	Display all transactions within the date range.
	•	Provide a summary with total income, total expenses, and net savings.
	•	Optionally, generate a visual plot to analyze income and expense trends.

**3. Exiting the Application**
	•	Select “Exit” from the menu to terminate the program.

 **Example Workflow** 

 **Adding Transactions** 

<img width="413" alt="Screenshot 2025-01-19 at 11 15 17 AM" src="https://github.com/user-attachments/assets/eab32093-00d9-4138-bd3a-79a6735eb38f" />

 **Viewing Transactions** 

 <img width="336" alt="Screenshot 2025-01-19 at 9 36 36 PM" src="https://github.com/user-attachments/assets/e13eae9e-7b8d-4e48-befc-bc426b327777" />

---

**File Structure** 

	CashCompass/
	│
	├── FinanceTracker.py                  # Main application file
	├── DataEntry.py            # Handles input validations for date, amount, category, and description
	├── Personal_Finance_Data.csv         # CSV file to store transaction data (created automatically)
	└── README.md                # Documentation

---

**Acknowledgments** 

	•	pandas: For CSV manipulation and data handling.
	•	matplotlib: For generating interactive and informative visualizations.
	•	Inspiration: The need for a simple, offline finance management tool for personal use.

---

	If you’d like to contribute:
		1.	Fork the repository.
		2.	Create a new branch (git checkout -b feature-name).
		3.	Commit your changes (git commit -m "Add feature-name").
		4.	Push to the branch (git push origin feature-name).
		5.	Open a Pull Request.
