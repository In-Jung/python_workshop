


class Todo:
    def __init__(self,todoNum,title):
        self.todoNum = todoNum
        self.title = title
    
    def __eq__(self, todoNum):
        return self.todoNum == todoNum 

    def __str__(self):
        return ("일정번호:{} 일정명:{} ".format(self.todoNum, self.title))
        

