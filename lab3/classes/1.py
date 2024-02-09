class str:
    def __init__(self):
        self.str=""
    def getstr(self):
        self.str=input()
    def printstr(self):
        print(self.str.upper())

x=str()
x.getstr()
x.printstr()