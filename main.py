from src.List import List as ls
from src.Task import Task as ts
from src.Checker import Checker as ch
import os


class Main:
    location = "List-Container"

    def __init__(self):
        print("+---------------------------------------------+")
        print("WELCOME TO CURSEDTASK TYPE help TO GET HELP ^_^")
        print("+---------------------------------------------+")
        while True:
            print(f"Location : {self.location}")
            if self.location != "List-Container":
                print(f"{self.location} Progress : {ls().getStatus(self.location)}")

            check = ch()
            userInput = self.getInput()
            if userInput == False:
                return
            inputCommand = self.inputHandler(userInput)
            if inputCommand == False:
                continue
            if check.isCommandExist(inputCommand["command"], self.location)[0]:
                if check.isCommandValid(inputCommand)[0]:
                    self.execute(inputCommand)
                else:
                    print(check.isCommandValid(inputCommand)[1])
            else:
                print(check.isCommandExist(inputCommand["command"], self.location)[1])
            print("-----------")
    
    def help(self):
        print("changeDue <nameTask/List> <newDue>")
        print("rename <nameTask/List> <newFileName>")
        print("create <nameTask/List> <(optional)due>")
        print("delete <nameTask/List>")
        print("open <nameList> ")
        print("done <nameList> ")
        print("undone <nameTask> ")
        print("show (to display List or Task) ")
        print("exit (back to List-Container)")
        print("close (closr program))")
        print("clear (clear screen))")
        print("help (display help))")

            
    
    def inputHandler(self, input):
        if input == "":
            return False
        inputCommand = {
            "command" : input.split(" ")[0]
        } 
        if input[-1] in (" ", "-"):
            input = input[:-1]
        stop = None
        for i in range(0, len(input)):
            
            if stop != None and i != stop:
                continue
            else:
                stop = None
            if input[i] == " " and input[i + 1] != "\"":
                start = i
                for j in range(i + 1, len(input)):
                    if input[j] == " " or j == len(input) - 1:
                        stop = j if input[j] == " " else  j + 1
                        inputCommand["arg" + str(len(inputCommand))] = input[start+1:stop]
                        break
                continue

            if input[i] == "\"":
                start = i
                for j in range(i + 1, len(input)):
                    if input[j] == "\"" or j == len(input):
                        stop = j if input[j] == " " else  j + 1
                        inputCommand["arg" + str(len(inputCommand))] = input[start+1:stop-1]
                        break
                continue
            
        return inputCommand
            
    def getInput(self):
        command = input(">> ")
        if command == "close":
            return False
        elif command == "clear":
            os.system("cls" if os.name == "nt" else "clear")
            command = self.getInput()
        elif command == "help":
            self.help()
            command = self.getInput()
        return command
    
    def showList(self):
        data = ls().getData()
        for n, key in enumerate(data, start=1):
            print(f"{n}. {key}  | Due : {data[key]['info']['due']} | {data[key]['info']['status']}")
        
    
    def execute(self, inputCommand):
        if self.location == "List-Container":
            if inputCommand["command"] in ("delete", "changeDue", "rename", "done", "undone", "open"):
                if not ch().isListExist(inputCommand["arg1"]):
                    print(f"ERROR : {inputCommand['arg1']} is not exist \"show\" for diplaying list")
                    return
            elif inputCommand["command"] in ("create"):
                if ch().isListExist(inputCommand['arg1']):
                    print(f"ERROR : {inputCommand['arg1']} is already exist \"show\" for diplaying list")
            if inputCommand["command"] == "create":
                if "arg2" in inputCommand:
                    ls().createList(nameList = inputCommand['arg1'], due = inputCommand["arg2"])
                else:
                    ls().createList(nameList = inputCommand['arg1']) 
            elif inputCommand["command"] == "open":
                self.location = inputCommand["arg1"]
            elif inputCommand["command"] == "show":
                self.showList()
            elif inputCommand["command"] == "delete":
                ls().deleteList(inputCommand["arg1"])
            elif inputCommand["command"] == "rename":
                ls().renameList(inputCommand["arg1"], inputCommand["arg2"])
            elif inputCommand["command"] == "changeDue":
                ls().changeDueList(inputCommand["arg1"], inputCommand["arg2"])
            elif inputCommand["command"] == "exit":
                print("SEE YOU ^_^")
                exit()
        else:
            if inputCommand["command"] in ("delete", "changeDue", "rename", "done", "undone"):
                if not ch().isTaskExist(self.location, inputCommand["arg1"]):
                    print(f"ERROR : {inputCommand['arg1']} task is not exist \"show\" for diplaying task")
                    return
            elif inputCommand["command"] in ("create", "open"):
                if ch().isTaskExist(self.location, inputCommand["arg1"]):
                    print(f"ERROR : {inputCommand['arg1']} task is already exist \"show\" for diplaying task")
                    return
            if inputCommand["command"] == "create":
                if "arg2" in inputCommand:
                    ls().createTask(nameList = self.location, due = inputCommand["arg2"], nameTask = inputCommand["arg1"])
                else:
                    ls().createTask(nameList = self.location, nameTask = inputCommand["arg1"])
            elif inputCommand["command"] == "delete":
                ls().deleteTask(nameList=self.location, nameTask=inputCommand["arg1"])
            elif inputCommand["command"] == "done":
                ls().doneTask(nameTask=inputCommand["arg1"], nameList=self.location)
            elif inputCommand["command"] == "show":
                ls().showTask(self.location)
            elif inputCommand["command"] == "undone":
                ls().undoneTask(nameTask=inputCommand["arg1"], nameList=self.location)
            elif inputCommand["command"] == "rename":
                ls().renameTask(nameList=self.location, nameTask=inputCommand["arg1"], newTaskName=inputCommand["arg2"])
            elif inputCommand["command"] == "changeDue":
                ls().changeDueTasK(nameList=self.location, nameTask=inputCommand["arg1"], newTaskDue=inputCommand["arg2"])
            elif inputCommand["command"] == "exit":
                self.location = "List-Container"
        

Main()