# Import libraries
import json
import re
from datetime import datetime
from src.variables import *

#load Json file        
def load_json():
    with open('src/bank_statement_sample.json', 'r') as f:
      json_data = json.load(f)
    json_content = json_data["content"]
    return json_content

# Write to Json file
def write_json(data):
    with open('output/output.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Convert date string to date format
def convert_date(date):
    date_format = datetime.strptime(date, "%d-%m-%Y").isoformat()
    return date_format

# Convert date string to date format
def convert_date_mt(date):
    date_format = datetime.strptime(date, "%d-%b-%Y").isoformat()
    return date_format

# Convert string to float
def string_float(str):
    float_str = float(str.replace(',',''))
    return float_str

# Extracting Information from Json content
def extract_details():
    
    json_content = load_json()
    
    statementInfo = StatementInfo()
    
    # Customer Name
    customer_name = re.search(r"Account Name:\s*(.*?)\s+Account Number:\s*(.*?)\s", json_content).group(1)
    statementInfo.customerName = customer_name
    
    # Account Number
    account_number = re.search(r"Account Number:\s+(\d+-\d+)", json_content).group(1)
    statementInfo.accountNumber = account_number
    
    # Currency 
    currency = re.search(r"Currency:\s+(\w{3})", json_content).group(1)
    statementInfo.currency = currency

    # Start Period
    periodstart = re.search(r"Period:\s+From\s+(\d{2}-\d{2}-\d{4})\s+To", json_content).group(1)
    statementInfo.periodStart = convert_date(periodstart)

    # End Period
    periodEnd = re.search(r"Period:\s+From\s+(\d{2}-\d{2}-\d{4})\s+To\s+(\d{2}-\d{2}-\d{4})", json_content).group(2)
    statementInfo.periodEnd = convert_date(periodEnd)

    # Opening  Balance
    openingBalance = re.search(r"\s+(.*?)Opening\s+Balance", json_content).group(1)
    statementInfo.openingBalance = string_float(openingBalance)

    # Extract Transaction Details
    transaction_details = re.findall(r"\n(\d{2}-\w{3}-\d{4})\s+(.*?)(\d{2}-\w{3}-\d{4})\s+(.*?)\n", json_content)

    transactionList = []

    currentBalance = string_float(openingBalance)
    totalDebit = 0.0
    totalCredit = 0.0

    # Extracting Transaction details 
    for transaction_detail in transaction_details[1:]:
        transact_d = Transaction()

        transact_d.transactionDate = convert_date_mt(transaction_detail[0])
        transact_d.narration = transaction_detail[1]

        amount_balance = transaction_detail[3].split()
        amount = string_float(amount_balance[0])
        balance = string_float(amount_balance[1])

        transact_d.amount = amount
        transact_d.balance = balance

        if balance < currentBalance:
            transaction_type = "Debit"
            currentBalance = balance
            totalDebit += amount
        else:
            transaction_type = "Credit"
            currentBalance = balance
            totalCredit += amount

        transact_d.type = transaction_type
        transactionList.append(transact_d)

    statementInfo.closingBalance = currentBalance
    statementInfo.totalCredit = totalCredit
    statementInfo.totalDebit = totalDebit
    
    statementInfo.transactions = [obj.__dict__ for obj in transactionList]

    # writing output to json file
    write_json(statementInfo.__dict__ )





    



