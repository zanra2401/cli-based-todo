import json
from src.Task import Task as ts

class List(ts):
    def __init__(self, description, status = "pending", task = "empty", due = "no-due"):
  
        ts.__init__(self, description, status, due)
        self.task = task
   
    def createList(self) :
        listToDo = {
                "info" : ts.getInformation(self),
                "task" : self.task
                }
        data = self.getData()
        data[self.description] = listToDo
        dataString = json.dumps(data, indent = 2)
        self.saveList(dataString)
        

    def setStatus(self, status):
        self.status = status

    def setTask(self, task):
        self.task = task

    def setDue(self, due):
        self.due = due
    
    def getDescription(self):
        return self.description

    def getTask(self):
        return self.task

    def getDue(self):
        return self.due

    def getStatus(self):
        return self.status
    
    def getData(self):
        f = open("data.json")
        data = dict(json.load(f))
        return data

    def saveList(self, listToSave):
        listToSave = json.dumps(listToSave, indent = 2)
        with open('data.json', 'w') as json_file:
            json_file.write(listToSave)
    
    def getList(self):
        data = self.getData()
        if data["task"] == "empty":
            return 
        else: 
            self.task = data["task"]
            for i in data["task"]:
                self.task.append = i

    def createTask(self, nameTask, nameList, status = "pending", due = "no-due"):
        data = self.getData()
        data = ts.createTask(self, nameTask, nameList, data, status, due)
        self.saveList(data)
    
    def deleteTask(self, nameTask, nameList):
        data = self.getData()
        data = ts.deleteTask(self, nameTask, nameList, data)
        self.saveList(data)
    
    def changeDueTasK(self, nameTask, nameList, newTaskDue):
        data = self.getData()
        data = super().changeDueTasK(nameTask, nameList, newTaskDue, data)
        self.saveList(data)
    
    def renameTask(self, nameTask, nameList, newTaskName):
        data = self.getData()
        data = super().renameTask(nameTask, nameList, newTaskName, data)
        self.saveList(data)
    
    def undoneTask(self, nameTask, nameList):
        data = self.getData()
        data = super().undoneTask(nameTask, nameList, data)
        self.saveList(data)
    
    def doneTask(self, nameTask, nameList):
        data = self.getData()
        data = super().doneTask(nameTask, nameList, data)
        self.saveList(data)
    


        


