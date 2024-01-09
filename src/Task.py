
class Task:
    def __init__(self):
        pass
     
    def getInformation(due):
        return {
            "status" : "[task empty]",
            "due" : due
        }  

    def createTask(self, nameTask, nameList, data, status = "pending", due = "no-due"):
        if type(data[nameList]["task"]) != dict:
            data[nameList]["task"] = {}

        data[nameList]["task"][nameTask] = {
            "status" : status,
            "due" : due
        }
        return data
    
    def deleteTask(self, nameTask, nameList, data):
        data[nameList]["task"].pop(nameTask)
        if len(data[nameList]["task"]) < 1:
            data[nameList]["task"] = "empty"
        return data
    
    def renameTask(self, nameTask, nameList, newTaskName, data):
        data[nameList]["task"][newTaskName] = data[nameList]["task"][nameTask]
        data[nameList]["task"].pop(nameTask)
        return data
    
    def doneTask(self, nameTask, nameList, data):
        if data[nameList]["task"][nameTask]["status"] == "done":
            return f"WARNING : {nameTask} already done!!!"
        data[nameList]["task"][nameTask]["status"] = "done"
        return data

    def undoneTask(self, nameTask, nameList, data):
        if data[nameList]["task"][nameTask]["status"] == "pending":
            return f"WARNING : {nameTask} already pending!!!"
        data[nameList]["task"][nameTask]["status"] = "pending"
        return data
    
    def changeDueTasK(self, nameTask, nameList, newTaskDue, data):
        data[nameList]["task"][nameTask]["due"] = newTaskDue
        return data
    




