import time
LOGFILEPREFIX = 'reddit'
LOGFILENAME = time.strftime("%Y%m%d")
bPrintToScreen = True
class clog(object):    
    def __init__(self):
        self.LOGFILEPREFIX = 'reddit'
        self.LOGFILENAME = time.strftime("%Y%m%d")
        self.bPrintToScreen = True
    def add(self, KEY, DESC):
        f = open(self.LOGFILEPREFIX + '-' + self.LOGFILENAME + '.log', 'a')
        LOGSTRING = ''
        LOGSTRING = time.strftime("%Y%m%d,%H%M%S")
        LOGSTRING = LOGSTRING + ', ' + KEY.rstrip()
        LOGSTRING = LOGSTRING + ', ' + DESC.rstrip() + "\n"
        f.write(LOGSTRING)
        f.close()
        if bPrintToScreen:
            print(str("Logged: " + LOGSTRING).strip())