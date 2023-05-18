In this test, you are provided with a JSON sample of transactions from a PDF bank statement. Your task is to parse individual transactions from the JSON file, and for each transaction, extract the transaction date, transaction description, amount, type (credit or debit), and balance, into a dictionary corresponding to that transaction. These records are to be returned in a very specific way and a file named expected_output.json has been provided to show you what the final output JSON should look like.

Further, you are to extract other meaningful information from the statement sample, including customer name, account number, etc. Again, the expected_output.json file shows you the relevant fields to extract.

Attachments

The attached folder contains the following 3 files:

- bank_statement_sample.json: This is the JSON file containing extracted transactions from a PDF bank statement.
- variables.py: This contains two classes consisting of variables relevant to the statement records. Variables in the StatementInfo class pertain to general information about the statement, while variables in the Transaction class pertain to information about each transaction in the statement. You are to use these classes to store the relevant transaction records.
- expected_output.json: This is the expected format for your solution output.

Directory Structure

Your solution directory should contain the following:

- extract.py: The main script that contains the functions you have defined for extracting the transactions and loading all records into a nested dict object, which can then be dumped into a JSON file.
- run.py: The script that implements your solution to generate the required output.
- output: The folder to dump the output JSON.
- src: The source folder containing the files provided for this test.
