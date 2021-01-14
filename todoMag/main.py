

from controller.todo_controller import TodoController
from view.view import display_menu,menu_select,message_display,list_display
from view.view import input_display,update_display,delete_display
controller = TodoController()

controller.file_read() 

while True:

    display_menu()
    menu = menu_select()
    menu = int(menu)

    if menu==1:
        todo = input_display()
        message_display(controller.register(todo))
    
    elif menu==2:
        controller.getAlltodos()

    elif menu==3:
        todoNum = update_display()
        message_display(controller.update(todoNum))

    elif menu==4:
        todoNum = delete_display()
        message_display(controller.delete(todoNum))

    elif menu==5:
        message_display(controller.clearAll())

    elif menu==0:
        print()
        controller.file_write()
        message_display("프로그램을 종료합니다.")
        break

    else:
        message_display("1,2,3,4,0 번 중 선택하세요")

    


