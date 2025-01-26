import pathlib

expenses = []
Expenses = pathlib.Path("./expenses.txt")
if Expenses.exists():
     with open(Expenses, "r") as f:
          content = f.read().strip()
          lines = content.splitlines()
               
          expenses = lines
else:
     with open(Expenses, "a") as f: # Create File
          pass

print("***Opening Expense Tracker***")

running = True
while running:
     print("1. View Expenses")
     print("2. Add Expense")
     print("3. Delete Expense")
     print("4. Quit")

     while True:
          try:
               option = int(input())
               if option < 1 or option > 4:
                    print("Enter an Int between 1 and 4")
                    continue
               break
          except:
               print("Enter an Int")
     
     if option == 1:
          if expenses != []:
               for index, expense in enumerate(expenses):
                    name, price, date = expense.split("/")
                    print(f"{index + 1}. NAME: {name} PRICE: {price} DATE: {date}")
          else:
               print("You have no expenses at the moment...")
          
     elif option == 2:
          name = input("Enter name of expense ")
          while True:
               try:
                    price = float(input("Enter price of expense "))
                    if price < 0:
                         print("Must be a positive decimal")
                         continue
                    break
               except:
                    print("Enter a float")
     
          date = input("Enter date of expense ")

          print("**** Adding Expense ****")
          name = name.strip()
          price = str(price).strip()
          date = date.strip()
          expenses.append(f"{name}/{price}/{date}")
          print("Finished")


     elif option == 3:
          expense_name = input("Enter name of expense to update: ")
          print("Deleting...")
          for expense in expenses:
               name, price, date = expense.split("/")
               if name == expense_name:
                    expenses.remove(expense)
     else:
          break
print('Quitting')

     