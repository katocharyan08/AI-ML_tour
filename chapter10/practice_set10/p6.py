from random import randint

class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo
    def book(self,fro,to):
        print(f"Ticket is booked in TrainNo. {self.trainNo} from {fro} to {to}")
    def getStatus(self):
        print(f"Train of TrainNo. {self.trainNo} is arriving at time")
    def getFare(self,fro,to):
        print(f"Ticket fare in TranNo. {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

obj = Train(26782)
obj.book("Jassur","Kangra")
obj.getStatus()
obj.getFare("Jassur","Kangra")