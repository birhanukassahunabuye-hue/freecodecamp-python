tasks = [{"tasks": "Buy Milk", "status":"pending"}, {"tasks": "Code Python", "status":"Done" }]

def add_dict():
   
   new_task_name=input("Enter your new task:") 
   new_status =input("Enter your task status")
   new_dict = {
     "tasks": new_task_name,
     "status":new_status
    }
   tasks.append(new_dict)
   return f"success! '{new_task_name}' added."





def mark_done(name_to_find):
   for item in tasks:
      if item['tasks'].lower()== name_to_find.lower():
         item['status']="Done"
         return f"Found it! '{item['tasks']}' is now Done."
   return "Task not found."
   

def show_pending():
     found_any = False
     for item in tasks:
          if item['status'].lower()=="pending":
             print(f"Pending Tasks: {item['tasks']}")
             found_any= True
     if not found_any:
             print("No pending tasks! You're all caught up.")



def delete_tasks():
    user_del=input("Enter task you want to delete: ")
    for item in tasks:
        if item['tasks'].lower()==user_del.lower():
            tasks.remove(item)
            return f"success! '{item['tasks']} has been removed.'"


    return "Task not found. Nothing was deleted."


while True:
   
   print("\n--- TO-DO LIST MANAGER---")
   print("1. View Tasks")
   print("2. Add Task")
   print("3. Mark Task as Done")
   print("4. View pending list")
   print("5. Delete ")
   print("6. Exit")
   
   choice = input("Select an option (1-6):")
   

   if choice == "1":
      print("\n---CURRENT TASKS---")
      for item in tasks:
         print(f"Task: {item['tasks']} | Status: {item['status']}")
   elif choice=="2":
      print(add_dict())
   elif choice=="3":
      target = input("Which task did you finish?")
      print(mark_done(target))
   elif choice=="4":
      print("\n---TASKS IN PENDING ARE:---")
      show_pending()
   elif choice=="5":
       print(delete_tasks())
   elif choice=="6":
      print("Goodbye!")
      break
   else:
      print("Invalid choice, please try again.")
      

      
      