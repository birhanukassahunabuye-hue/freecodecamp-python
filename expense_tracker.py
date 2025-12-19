expense=[]
def expense_tracker():
    item = input("Enter the item you want to buy: ")
    try:
       price = float(input("Enter the price of your item: "))
       expense_data = {"item": item, "price": price}
       expense.append(expense_data)
       print(f"Added {item} successfully!")
    except ValueError:
        print("\nInvalid Input! Please enter a number for the price.")
def view_all():
    print("\n---History---")
    for dict in expense:
        print(f"{dict['item']}: ${dict['price']}")

def total_expense():
    total = 0
    for dict in expense:
          total += dict['price']
    
    print(f"\n Your total spending is: ${total:.2f}")

while True:
    print("\n1.Add expense | 2. view   | 3.Total expense |4.Exit")
    choice= input("Select: ")
    if choice == "1":
        expense_tracker()
    elif choice=="2":
        
        view_all()
    elif choice=="3":
        total_expense()
    elif choice=="4":
        break