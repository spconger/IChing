class Hexline:
    # This class defines a line. Each Hexigram
    # in the Iching consists of six lines
    # the line can be solid or broken
    # a line can also be strong or weak
    # a strong line changes into its opposite
    # a weak line states the same
    # the changed lines are used to generate
    # a second hexigram that represents
    # where things are going
    # the position is to note what position the line 
    # occupies in the hexagram (1-6)

    # constructor calls the setInitial method
    # which sets all values to their minimum
    def __init__(self):
        self.setInitial()

    # sets or resets values to initial values
    def setInitial(self):
        self.value=0
        self.linetext=""
        self.change=0
        self. position=0

    # sets and gets. I did not want to pass
    # the class values through the constructor
    # so I created a set/get pair for each field

    def setValue(self, value):
        self.value=value
    
    def getValue(self):
        return self.value
    
    def setLineText(self, ltext):
        self.linetext=ltext
    
    def getLineText(self):
        return self.linetext
    
    def setChange(self, change):
        self.change=change

    def getChange(self):
        return self.change
    
    def setPosition(self, pos):
        self.position=pos

    def getPosition(self):
        return self.position

