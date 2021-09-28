from enum import Enum
from abc import ABC


class AccountType(Enum):
    whitout_profit = 0
    short_time = 10
    long_time = 20


class Customer(ABC):
    def __init__(self, ncode: str, fname: str, lname: str):
        if not self.__validator(ncode):
            print("invalid national code")
            exit(0)
        elif not self.__validator(fname):
            print("invalid first name")
            exit(0)
        elif not self.__validator(lname):
            print("invalid last name")
            exit(0)

        self.national_code = ncode
        self.first_name = fname
        self.last_name = lname

    def __str__(self):
        return 'National Code: {} , FullName: {}'.format(self.national_code, "{} {}".format(self.first_name,
                                                                                            self.last_name))

    @staticmethod
    def __validator(input: str) -> bool:
        return input is not None and len(input) > 0


class CustomerWantNewAccount(Customer):
    def __init__(self, ncode: str, fname: str, lname: str, acctype: AccountType):
        super().__init__(ncode, fname, lname)
        self.account_type = acctype

    def __str__(self):
        return "{0}\n{1}".format(super().__str__(), str("Account Type: {}".format(self.account_type.name.replace("_",
                                                                                                                 " "))))


class CustomerWantLoan(Customer):
    def __init__(self, ncode: str, fname: str, lname: str, loan: float):
        super().__init__(ncode, fname, lname)

        if loan <= 0.0:
            loan = (-loan + 1000)

        self.loan_value = loan

    def __str__(self):
        return "{0}\n{1}".format(super().__str__(), str("Loan Value: {:.2f}".format(self.loan_value)))


class CustomerWantTelBank(Customer):
    def __init__(self, ncode: str, fname: str, lname: str, phone: str):
        super().__init__(ncode, fname, lname)

        if 0 <= len(phone) > 11:
            print("invalid cell-phone Number")
            exit(0)

        self.phone_number = phone

    def __str__(self):
        return "{0}\n{1}".format(super().__str__(), str("Phone Number: {}".format(self.phone_number)))


customers = list()
customers.append(CustomerWantLoan(input("Enter You't National Code: "), input("Enter You't First Name: "),
                                  input("Enter You't Last Name: "), float(input("Enter You't Loan Value: "))))
print(10 * "==")
customers.append(CustomerWantNewAccount(input("Enter You't National Code: "), input("Enter You't First Name: "),
                                  input("Enter You't Last Name: "), AccountType.whitout_profit))
print(10 * "==")
customers.append(CustomerWantNewAccount(input("Enter You't National Code: "), input("Enter You't First Name: "),
                                  input("Enter You't Last Name: "), AccountType.long_time))
print(10 * "==")
customers.append(CustomerWantTelBank(input("Enter You't National Code: "), input("Enter You't First Name: "),
                                  input("Enter You't Last Name: "), input("Enter You't 11 digit Phone Number: ")))

for customer in customers:
    if type(customer) is CustomerWantTelBank:
        print(customer)

