# 일정 입력 / 일정 보기 / 일정 수정 / 일정 삭제 

todos =[{"title": "dinner"}]
 

while True:
    print("====TO DO====")
    print("1.일정 입력")
    print("2.일정 보기")
    print("3.일정 수정")
    print("4.일정 삭제")
    print("5.일괄 삭제")
    print("0.종료")
    menu=input("메뉴를 선택하세요")
    if menu=="1":
        title=input("일정을 입력하세요 :")
        
        todo = { "title" : title }
        todos.append(todo)
        print("{0} 일정이 등록됐습니다".format(title))
        
    
    elif menu=="2":   # == 이후 "" 빼먹으면 안됨       
        print("====일정 보기====")
        print(todos)
    
    elif menu=="3":                             
        select_title = input("수정할 일정을 입력하세요 :" )
        for todo in todos:
                if todo["title"] == select_title:
                    new_title = input("새로운 일정을 입력하세요 :")
                    todo['title'] = new_title                   
                    print("{0} 일정이 수정됐습니다.".format(todo["title"]))
                    print()
    
    elif menu=="4":       #수정필요
            delete_title =input("삭제할 일정을 입력하세요 :")
            for todo in todos:
              if todo["title"] == delete_title:                
                todos.remove(todo)
                print("{0}의 정보를 삭제합니다" .format(todo["title"]))
                print()    
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



