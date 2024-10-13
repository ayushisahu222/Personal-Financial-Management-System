# ---------------------------------------------------------FINANCIAL MANAGEMENT SYSTEM----------------------------------------------------------

# This project demonstrates the core OOP concepts:
#  - Encapsulation: Controlled access to class attributes.
#  - Inheritance: Reuse and extend functionality across classes.
#  - Polymorphism: Different behavior for methods with the same name.
#  - Abstraction: Hiding implementation details and exposing simple interfaces.
#  - MRO: Defines the order of method resolution in complex hierarchies.
#  - Mixins: Reusable functionality shared across classes.
#  - Properties: Manage attribute access in a controlled way.
#  - Singleton pattern: Ensures a class has only one instance.

from abc import ABC, abstractmethod
# Base class
class financialEntity(ABC): # inherits from ABC to make sure its an abstract base class
    def __init__(self,amount):
        self._amount = amount # protected attribute
    
    @abstractmethod
    def get_details(self):  # abstract method
        pass
    
    def get_total_amount(self):
        return self._amount

# Dervied class
class income(financialEntity): # inherits from class financialEntity
    def __init__(self,amount):
        super().__init__(amount) # initialize base class with amount

    def get_details(self): # method overriding
        return f"Income: {self._amount}"
    
    def get_amount(self):
        return super().get_amount()

# Dervied class
class expense(financialEntity): # inherits from class financialEntity
    def __init__(self,rent,utilities,groceries,transportation,entertainment):
        self.rent = rent
        self.utilities = utilities
        self.groceries = groceries
        self.transportation = transportation
        self.entertainment = entertainment
        self._amount = rent + utilities + groceries + transportation + entertainment  # Total expense

    
    def get_details(self): # method overriding
        return (
            f"Expenses Details:\n"
            f"Rent: {self.rent}\n"
            f"Utilities: {self.utilities}\n"
            f"Groceries: {self.groceries}\n"
            f"Transportation: {self.transportation}\n"
            f"Entertainment: {self.entertainment}\n"
            f"Total Expense: {self._amount}" # protected attribute
        )

# Dervied class
class savings(financialEntity):  # inherits from class financialEntity
    def __init__(self,emergency_fund,retirement_savings,investments):
        self.emergency_fund = emergency_fund
        self.retirement_savings = retirement_savings
        self.investments = investments
        self._totalSavings = emergency_fund + retirement_savings + investments

    def get_details(self): # method overriding
        return (f"Emergency Fund: {self.emergency_fund}\n"
                f"Retirement Savings: {self.retirement_savings}\n"
                f"Investments: {self.investments}\n"
                f"Total Savings: {self._totalSavings}")

# Polymorphism
def print_financial_details(entities):
    for entity in entities:
        # Showcases the correct implementation of get_details() for each specific class, regardless of the reference type
        print(f"{entity.get_details()}") 
        print("_" * 30)

   
def main():
    # create an object of income, expense, savings classes
    salary = income(5000)                  
    rent = expense(300)
    save = salary.get_amount() - rent.get_amount()  # get the amount of salary and rent and calculate difference
    bank_savings = savings(save)

    # print(salary.get_details())
    # print(rent.get_details())
    # print(bank_savings.get_details())

    print_financial_details(salary)       # Calls get_details from income
    print_financial_details(rent)         # Calls get_details from expense
    print_financial_details(bank_savings) # Calls get_details from savings


if __name__ == "__main__":
    main()