import json
import os
from src.Task import Task as ts

class List(ts):
    def __init__(self):
        ts.__init__(self) 
        self.path = os.getcwd()
        print(self.path)
   
    def createList(self, nameList, task = "empty", due = "no-due"):
        listToDo = {
                "info" : ts.getInformation(due),
                "task" : task
                }
        if not os.path.isfile(os.path.join(self.path + "storage", "data.json")):
            with open("storage/data.json", "w") as file:
                file.write("{ " + " }")

        data = self.getData() 
        data[nameList] = listToDo
        self.saveList(data)
    
    def calculateStatus(self, data, nameList):
        totalTask = 0
        taskDone = 0
        for i in data[nameList]["task"]:
            if data[nameList]["task"][i]["status"] == "done":
                taskDone += 1
            totalTask += 1
        percentage = int((taskDone/totalTask) * 100)
        data[nameList]["info"]["status"] = "[" + str(percentage) + "%" + "]"
        return data
 
    def deleteList(self, nameList):
        data = self.getData()
        data.pop(nameList)
        self.saveList(data)
    
    def renameList(self, nameList, newNameList):
        data = self.getData()
        data[newNameList] = data[nameList]
        data.pop(nameList)
        self.saveList(data)
    
    def changeDueList(self, nameList, newDue):
        data = self.getData()
        data[nameList]["info"]["due"] = newDue   
        self.saveList(data)

    def getStatus(self, nameList):
        data = self.getData()[nameList]
        return data["info"]["status"]
    
    def getData(self):
        if not os.path.isfile(os.path.join("storage", "data.json")):
            with open("storage/data.json", "w") as file:
                file.write("{ " + " }")
        f = open("storage/data.json")
        data = dict(json.load(f))
        return data

    def saveList(self, listToSave):
        listToSave = json.dumps(listToSave, indent = 2)
        with open('storage/data.json', 'w') as json_file:
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
        data = super().createTask(nameTask, nameList, data, status, due)
        data = self.calculateStatus(data, nameList)
        self.saveList(data)
    
    def deleteTask(self, nameTask, nameList):
        data = self.getData()
        data = super().deleteTask(nameTask, nameList, data)
        data = self.calculateStatus(data, nameList)
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
        data = self.calculateStatus(data, nameList)
        self.saveList(data)
    
    def doneTask(self, nameTask, nameList):
        data = self.getData()
        data = super().doneTask(nameTask, nameList, data)
        data = self.calculateStatus(data, nameList)
        self.saveList(data)
    
    def showTask(self, nameList):
        data = self.getData()[nameList]["task"]
        if data == "empty":
            print("Task Empty :<)")
            return
        for n, key in enumerate(data, start=1):
            print(f"{n}. {key}  | Due: {data[key]['due']} | Status : {data[key]['status']}")