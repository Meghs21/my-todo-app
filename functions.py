FILEPATH="todos.txt"
def get_todos(filepath=FILEPATH):
    with open("todos.txt", "r") as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath,"w") as file:
        file.writelines(todos_arg)

if __name__=="__to do list__":
    print("hello")
    print(get_todos())