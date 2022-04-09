import random # import required librarys 
class ccolour(object):
    def __init__(self):
        self.colour = (0,0,0)
        self.R = 0
        self.G = 0
        self.B = 0 
        self.A = 255

    def getrgba(self, colour, alpha):
        if alpha == "":
            ialpha = random.randint(0,255)
        else:
            ialpha = int(alpha)
        c = self.getrgb(colour)
        self.R = c[0]
        self.G = c[1]
        self.B = c[2]
        self.alpha = ialpha
        return (c[0],c[1],c[2],ialpha)
        
    def getrgb(self, colour = ""):
        self.alpha = 255
        if colour == "RED":
            self.R = random.randint(0, 255)
            self.G = 0
            self.B = 0
        if colour == "GREEN":
            self.R = 0
            self.G = random.randint(0, 255)
            self.B = 0
        if colour == "BLUE":
            self.R = 0
            self.G = 0
            self.B = random.randint(0, 255)
        if colour == "YELLOW":
            self.R = random.randint(0, 255)
            self.G = random.randint(0, 255)
            self.B = 0
        if colour == "MAGENTA":
            self.R = random.randint(0, 255)
            self.G = 0
            self.B = random.randint(0, 255)
        if colour == "CYAN":
            self.R = 0
            self.G = random.randint(0, 255)
            self.B = random.randint(0, 255)
        if colour == "GREY":
            icolour = random.randint(0, 255)
            self.R = icolour
            self.G = icolour
            self.B = icolour
        if colour == "":
            self.R = random.randint(0, 255)
            self.G = random.randint(0, 255)
            self.B = random.randint(0, 255)
        self.colour = (self.R, self.G, self.B)
        return self.colour