from datetime import date
import json
import re


class DataParser:

    def __init__(self,bool_debugMode = False):
        self.json_threadData=dict()
        self.bool_debugMode = bool_debugMode

        pass
    
    def loadFromJson(self,json_threadData):
        self.json_threadData = json.load(json_threadData)

        if(self.bool_debugMode):
            writeLog('=========loadFromJson=========')     
            writeLog('Input name:')
            writeLog('json_threadData')
            writeLog('Input type:')
            writeLog(type(json_threadData))
            writeLog('Input value:')
            writeLog(json_threadData)
            writeLog(' ')
            writeLog('Output name:')
            writeLog('json_threadData')
            writeLog('Output type:')
            writeLog(type(self.json_threadData))
            writeLog('Output value:')
            writeLog(self.json_threadData)
            writeLog('=========loadFromJson=========')

        pass

    def loadFromFile(self,json_threadData):
        try:
            fs_fileStream = open(json_threadData,'r')
            self.json_threadData=json.load(fs_fileStream)
            fs_fileStream.close()

        except:
            print('=========loadFromFile=========')
            print('except call')
            print('=========loadFromFile=========')

        if(self.bool_debugMode):
            writeLog('=========loadFromFile=========')     
            writeLog('Input name:')
            writeLog('json_threadData')
            writeLog('Input type:')
            writeLog(type(json_threadData))
            writeLog('Input value:')
            writeLog(json_threadData)
            writeLog(' ')
            writeLog('Output name:')
            writeLog('json_threadData')
            writeLog('Output type:')
            writeLog(type(self.json_threadData))
            writeLog('Output value:')
            writeLog(self.json_threadData)
            writeLog('=========loadFromFile=========')

        pass

    def loadFromStream(self,json_threadData):
        try:
            self.json_threadData=json.load(json_threadData)
            
        except:
            print('=========loadFromFile=========')
            print('except call')
            print('=========loadFromFile=========')

        if(self.bool_debugMode):
            writeLog('=========loadFromStream=========')     
            writeLog('Input name:')
            writeLog('json_threadData')
            writeLog('Input type:')
            writeLog(type(json_threadData))
            writeLog('Input value:')
            writeLog(json_threadData)
            writeLog(' ')
            writeLog('Output name:')
            writeLog('json_threadData')
            writeLog('Output type:')
            writeLog(type(self.json_threadData))
            writeLog('Output value:')
            writeLog(self.json_threadData)
            writeLog('=========loadFromStream=========')

        pass

    def feedData(self,json_threadData):
        try:
            if(type(json_threadData)==str):
                loadFromFile(json_threadData)
            elif(type(json_threadData)==dict):
                loadFromJson(json_threadData)
            else:
                loadFromStream(json_threadData)

        except:
            print('Invalid input type')
            writeLog('Invalid input type')
        
        if(self.bool_debugMode):
            writeLog('=========feedData=========')     
            writeLog('Input name:')
            writeLog('json_threadData')
            writeLog('Input type:')
            writeLog(type(json_threadData))
            writeLog('Input value:')
            writeLog(json_threadData)
            writeLog('=========feedData=========')
        
        pass
            
    def writeLog(self,str_logString):
        try:
            str_filePath = 'log/'+str(date.today())+'.log'
            fs_logStream = open(str_filePath,'a')
            str_date = '['+str(date.today())+'] '
            fs_logStream.write(str_date+str(str_logString)+'\n')
            fs_logStream.close()

        except:
            print('=========writeLog=========')
            print('except call')
            print('=========writeLog=========')

        pass

    def getData(self):
        return self.json_threadData

        pass

    def setData(self,json_threadData):
        self.json_threadData = json_threadData
        
        pass

    def getDebugMode(self):
        return self.bool_debugMode

        pass

    def setDebugMode(self,bool_debugMode):
        self.bool_debugMode = bool_debugMode

        pass
