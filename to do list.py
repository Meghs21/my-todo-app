import functions
import time

now=time.strftime("%b %d %Y %H:%M:%S")
print("it is",now)
while True:
       user_action=input("type add,show,edit,complete or exit:")#user input
       user_action=user_action.strip()

       if  user_action.startswith("add"):
           todo=user_action[4:]

           todos=functions.get_todos()

           todos.append(todo + "\n")

           functions.write_todos(todos)

       elif user_action.startswith("show"):

           todos=functions.get_todos()

           for index,items in enumerate(todos):
               items=items.strip("\n")
               print(f"{index+1}-{items}")

       elif user_action.startswith("edit"):
           try:
               number=int(todo[5:])
               print(number)

               number=number-1

               todos=functions.get_todos()


               new_todo=input("enter new todo:")
               todos[number]=new_todo + "\n"

               with open("todos.txt", "w") as file:
                    todos = file.writelines(todos)
           except ValueError:
               print("your command is not valid")
               continue



       elif user_action.startswith("complete"):
           todo_done=input("enter the todo completed:")

           todos=functions.get_todos()

       elif user_action.startswith("exit"):
           break
           
       else:
           print("command is invalid")
print("bye")

