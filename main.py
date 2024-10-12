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
class financialEntity:
    def __init__(self,amount):
        self._amount = amount # private attribute
    
    @abstractmethod
    def get_details(self):  # abstract method
        pass
    
    def get_amount(self): 
        return self._amount

# Dervied class
class income(financialEntity): # inherits from class financialEntity
    def get_details(self): # method overriding
        return f"Income: {self._amount}"
    def get_amount(self):
        return super().get_amount()

# Dervied class
class expense(financialEntity): # inherits from class financialEntity
    def get_details(self): # method overriding
        return f"Expense: {self._amount}"
    def get_amount(self):
        return super().get_amount()

# Dervied class
class savings(financialEntity):  # inherits from class financialEntity
    def get_details(self): # method overriding
        return f"Savings: {self._amount}"
    def get_amount(self):
        return super().get_amount()

# Polymorphism
def print_transaction_details(transaction):
    print(f"{transaction.get_details()}") # It accepts any object of type financialEntity (or its subclasses) and calls get_details which executes the appropriate version of the method based on the object type.

   
def main():
    # create an object of income, expense, savings classes
    salary = income(5000)                  
    rent = expense(300)
    save = salary.get_amount() - rent.get_amount()  # get the amount of salary and rent and calculate difference
    bank_savings = savings(save)

    # print(salary.get_details())
    # print(rent.get_details())
    # print(bank_savings.get_details())

    print_transaction_details(salary)       # Calls get_details from income
    print_transaction_details(rent)         # Calls get_details from expense
    print_transaction_details(bank_savings) # Calls get_details from savings


if __name__ == "__main__":
    main()