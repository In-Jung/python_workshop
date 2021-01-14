
from dao.file_dao import save_list,init_data_load

class TodoService:
    todos = [] #static variable
    
    def register(self,todo):
        index = self.is_exist(todo.todoNum)
        if index <0:           
            TodoService.todos.append(todo)
            return ("{0} 일정이 등록되었습니다.".format(todo.title)) 
        else:
            return ("이미 존재하는 ID 입니다.")  
        

    
    def update(self,todoNum):
        index = self.is_exist(todoNum)
        if index >-1:
            new_title = input("일정 수정: ")
            TodoService.todos[index].title=new_title
            return("{} 수정되었습니다.".format(new_title))
        else:
            return("존재하지 않는 일정 ID입니다")

    
    def delete(self,todoNum):
        index = self.is_exist(todoNum)
        if index >-1:
            TodoService.todos.pop(index)
            return("{} 삭제되었습니다.".format(index))
        else:
            return("존재하지 않는 일정 ID입니다")

   
    def clearAll(self):
        response = input("전체 삭제하시겠습니까? (Y/N)")
        if(response=='y' or 'Y'):
            TodoService.todos.clear()
            return("전체 삭제 되었습니다." )
        

    
    def is_exist(self,id):
        for i, todo in enumerate(TodoService.todos):
            if todo.todoNum == id:
                return i  
        return -1 


    def file_read(self):
        TodoService.todos = init_data_load()

    def file_write(self):
        save_list(TodoService.todos)