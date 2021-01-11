# 일정 입력 / 일정 보기 / 일정 수정 / 일정 삭제 

todos =[{"todoNum": 0, "todo": "dinner"}]
todoNum =1 

while True:
    print("====TO DO====")
    print("1.일정 입력")
    print("2.일정 보기")
    print("3.일정 수정")
    print("4.일정 삭제")
    print("0.종료")
    menu=input("메뉴를 선택하세요")
    if menu=="1":
        title=input("일정을 입력하세요 :")
        
        todo = {"todoNum": todoNum, "todo" : title }
        todos.append(todo)
        print("{0} 일정이 등록됐습니다".format(title))
        todoNum +=1
    
    elif menu=="2":   # == 이후 "" 빼먹으면 안됨       
        print("====일정 보기====")
        print(todos)
    
    elif menu=="3":                                 #수정 필요
        todoNum = input("수정할 일정 번호 입력하세요")                
        new_title = input("일정 수정" :)
            for todo in todos :
                if todo["tittle"] == new_title:                    
                    print("{0} 일정이 수정됐습니다.".format(todo["title"]))
    
    elif menu=="4":       #수정필요
        while not todoNum.isdecimal():
            print("삭제할 일정 번호를 입력하세요")
            todoNum=input("삭제할 일정 번호 :")
            for todo in todos:
              if todo["todoNum"] == todoNum:                
                todos.remove(todo)
                print("{0}의 정보를 삭제합니다")
                break
    
    elif menu=="0":
        print("프로그램을 종료합니다")
        break
    else :
        print()
        print("번호를 선택하세요")



