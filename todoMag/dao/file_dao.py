import os.path
from entity.todo import Todo

def save_list(todos):
    save_file = open("todoList.dat","w")
    for index, todo in enumerate(todos):
        save_file.write("{0}번째 | {1},{2}\n".format(index,todo.todoNum,todo.title))

    save_file.close()


def init_data_load():
    fileExist = os.path.isfile("todoList.dat")
    todos =[]
    if fileExist:
        print("todoList file loaded")
        with open("todoList.dat","r") as f:
            while True:
                data = f.readline()
                if len(data.split("|")) == 2:
                    todo = data.split("|")[1].strip("\n").split(",")
                    todos.append(Todo(todo[0].strip(), todo[1].strip()))
                if not data:
                    break
    return todos
    