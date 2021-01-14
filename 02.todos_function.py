# 일정 입력 / 일정 보기 / 일정 수정 / 일정 삭제 
import os. path
todos =[{"title": "dinner"}]


def is_exist(title):
    for index, todo in enumerate(todos):
        if todo["title"] == title :
            return index
    return -1

#일정 등록
def register(todo) :
    index = is_exist(todo["title"])
    if  index <0 : 
        todos.append(todo)
        return "{0} 등록됐습니다. ".format(todo["title"])
    else:
        return "해당 일정은 존재하지 않습니다"

#일정 목록
def getAlltodos():
    return todos
#일정 수정
def update(title):
    index = is_exist(todo["title"])
    if index > -1:
        todos[index]["title"] = title
        return "{0} 수정 완료 ".format(todo["title"])
    else:
        "해당 일정은 존재하지 않습니다"

#일정 삭제
def remove(title):
    index = todo["title"]
    if index > -1 :
        todos.pop(index)
        return "{0} 삭제 완료 ".format(todo["title"])
    else:
        return"해당 일정은 존재하지 않습니다"
         
#menu display
def menu_dispay():
    print("====TO DO====")
    print("1.일정 입력")
    print("2.일정 보기")
    print("3.일정 수정")
    print("4.일정 삭제")
    print("5.일괄 삭제")
    print("0.종료")



#message display
def message_display(message):
    print(message)

#data save
def save_list():
    save_file=open("todos.dat", "w")
    for index, todo in enumerate(todos):
        save_file.write("{0}번째 | {1},{2},{3},{4}\n".format(index, todo["id"],todo["name"],todo["age"],todo["major"]))
    save_file.close()#파일 존재시 초기화 

def init_data_load():
    fileExist = os.path.isfile("todos.dat")
    if fileExist:
        read_file = open("todos.dat", "r")
        while True:
            data = read_file.readline()
            if len( data.split("|")) ==2:
                todo = data.split("|")[1].strip("\n").split(",")
                todos.append({"ititle": student[0].strip()})
            if not data : break 
        read_file.close()

while True:
    menu_display 
    menu=input("일정을 선택하세요")
    if menu=="1":
        title=input("일정을 입력하세요 :")
        
        todo = { "title" : title }
        todos.append(todo)

        message_display(register(todo))    
    
    elif menu=="2":   # == 이후 "" 빼먹으면 안됨       
        print("====일정 보기====")
        print(todos)
    
    elif menu=="3":                             
        select_title = input("수정할 일정을 입력하세요 :" )                     
            # new_title = input("새로운 일정을 입력하세요 :")
            message_display(update(title))               
    
    elif menu=="4":      
            delete_title =input("삭제할 일정을 입력하세요 :")
            message_display(update(title))          
    elif menu=="0":
        print("프로그램을 종료합니다")
        break
    elif menu=="5":
        order_all = input("기록을 전부 삭제합니다. [Y]")
        if order_all == 'Y' or order_all == 'y':
            todos.clear()
            print()
        else :
            print()
    else :
        print()
        print("번호를 선택하세요")



