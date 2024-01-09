import json
from src.Task import Task as ts

class List(ts):
    def __init__(self, description, status = "pending", task = "empty", due = "no-due"):
        print(ts)
        ts.__init__(self, description, status, due)
        self.task = task
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
        print(type(data))
        if type(data[nameList]["task"]) != dict:
            data[nameList]["task"] = {}

        data[nameList]["task"][nameTask] = {
            "status" : status,
            "due" : due
        }

        data = json.dumps(data, indent = 2)
        self.saveList(data)

        


