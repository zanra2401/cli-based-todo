from src.List import List as ls

class Checker:
    listCommand = ["create", "delete", "rename", "changeDue", "open", "show"]
    taskCommand = ["done", "undone", "create", "delete", "rename", "changeDue", "show", "exit"]
    def isListExist(self, name):
        data = ls().getData()
        return name in data
        
    
    def isTaskExist(self, nameList, nameTask):
        data = ls().getData()[nameList]["task"]
        for i in data:
            if i == nameTask:
                return True
        return False
    
    def isCommandExist(self, command, location):
        validCommand = self.listCommand if location == "List-Container"  else self.taskCommand
        if command in validCommand:
            return [True]
                
        return [False, f"command \"{command}\" not exist in {location}"]
        
    def isCommandValid(self, command):
        command_name = command["command"]
        if command_name in "create":
            if len(command) > 3:
                return [False, f"Error: Command \"{command_name}\" max accepted argument is two"]
            elif len(command) < 2:
                return [False, f"Error: Command \"{command_name}\" at least have one argument"]
        elif command_name in ["delete", "undone", "done", "open"]:
            if len(command) != 2:
                return [False, f"Error: Command \"{command_name}\" only accept one argument"]
        elif command_name in ["rename", "changeDue"]:
            if len(command) != 3:
                return [False, f"Error: Command \"{command_name}\" must have two arguments"]
        elif command_name in ["show", "exit"]:
            if len(command) != 1:
                return [False, f"Error: Command \"{command_name}\" does not accept arguments"]
        return [True]



        



    

