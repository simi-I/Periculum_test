class StatementInfo(object):
    customerName = None # str
    accountNumber = None # str
    currency = None # str
    periodStart = None # datetime object
    periodEnd = None # datetime object
    openingBalance = None # float
    closingBalance = None # float
    totalDebit = None # float
    totalCredit = None # float
    transactions = list()


class Transaction(object):
    transactionDate = None # datetime object - e.g., 2022-08-27T00:00:00, using datetime.strptime(the_date_string,'%d-%m-%Y').isoformat()
    amount = None # float
    balance = None # float
    type = None # str
    narration = None # str

    def haveData(self):
        if self.__dict__.keys():
            return True
        else:
            return False
