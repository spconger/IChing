from Hexline import Hexline

class Hexagram:
    # a hexagram consists of a set of six lines broken or unbroken
    # in a specific order
    # the lines objects are stored in a list
    # A hexigram has a name and an explanatory text
    def __init__(self):
         self.InializeHex()
     
    #method to initialize or reinitialize values
    def initializeHex(self):
        self.name=""
        self.lines=[]
        self.hexText=""
        self.hexNumber=0

    # sets and gets

    def setName(self, name):
        self.name=name

    def getName(self):
        return self.name
    
    # method to add a line to list
    def addLine(self, line):
        self.lines.append(line)

    # the get returns the whole list
    def getLines(self):
        return self.lines
    
    def setHexText(self, text):
        self.hexText=text

    def getHexText(self):
        return self.hexText
    
    def setHexNumber(self, num):
        self.hexNumber=num

    def getHexNumber(self):
        return self.hexNumber
