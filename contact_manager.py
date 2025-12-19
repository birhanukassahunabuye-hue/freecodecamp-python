my_contacts = {
    "Abdi": "0911-2233",
    "sara": "0922-4455"
}
def add_contact(name, number):
    my_contacts[name.title()]= number
    return f"sucess! {name.title()}'s phone number has been added."






print(f"Current Book: {my_contacts}")
def contact_book(search):
  
   formated_name = search.title()
   if formated_name in my_contacts:
      
        return f"{formated_name}:  {my_contacts[formated_name]}"
   else: 
         return "contact not found"
      


          



while True:
     print("\n---CONTACT BOOK MENU---")
     choice = input("Pick one: (A)dd, (S)earch, or (Q)uit: ")


     if choice.upper() == 'A':
         new_name = input("Enter name: ") 
         new_num = input("Enter phone number: ")
         print(add_contact(new_name, new_num))
     elif  choice.upper() =="S":
          user_input = input("Who are you looking for?")
          print(contact_book(user_input))
     elif choice.upper()=="Q":
          print("Closing contact Book. Goodbye!")
          break
     else:
          print("Invalid choice, please try again.")
