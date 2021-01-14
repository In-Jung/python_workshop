from service.todo_service import TodoService
from view.view import message_display,list_display

class TodoController:
    
    
    def register(self,todo):
        service = TodoService()
        message = service.register(todo)
        message_display(message)

    
    def update(self,todoNum):
        service = TodoService()
        message = service.update(todoNum)
        message_display(message)

   
    def delete(self,todo):
        service = TodoService()
        message = service.delete(todo)
        message_display(message)
        
    
    def clearAll(self):
        service = TodoService()
        message= service.clearAll()
        message_display(message)


    def getAlltodos(self):
        service = TodoService()
        todos = service.todos
        list_display(todos)


    def file_read(self):
        service = TodoService()
        service.file_read()
        

    def file_write(self):
        service = TodoService()
        service.file_write()
    


    
