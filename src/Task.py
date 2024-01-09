
class Task:
    def __init__(self, description, status = "pending", due = "no-due"):
        self.description = description
        self.status = status
        self.due = due 
     
    def getInformation(self):
        return {
            "status" : self.status,
            "due" : self.due
        }  