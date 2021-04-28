from requests.structures import CaseInsensitiveDict
from WebParser import WebParser
from datetime import date
import json
import requests
import re
import os

class Crawler:
    def __init__(self,bool_debugMode=False):
        self.bool_debugMode = bool_debugMode
        self.strct_header = CaseInsensitiveDict()
        self.strct_header['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'
        self.strct_header['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8'
        self.strct_header["Connection"] = "keep-alive"
        self.strct_header["Origin"] = "https://groups.google.com"
        self.strct_header["X-Same-Domain"] = "1"
        self.strct_header["Accept-Language"]= "en-US,en;q=0.5"
        self.strct_header["Accept"] = "*/*"
        self.arr_threadCode = []
        self.int_totalThread = 0
        self.str_groupName = ''
        self.str_fragmentViewURL='https://groups.google.com/forum/?_escaped_fragment_=categories/'
        self.str_ggroupURL='https://groups.google.com/g/'
        self.c_webParser = WebParser()
        self.dict_groupData= dict()

        pass

    def getGroupName(self):
        return self.str_groupName
    
    def getHeader(self):
        return self.strct_header

    def getThreadCode(self):
        return self.arr_threadCode

    def getTotalThread(self):
        return self.int_totalThread
    
    def getGroupName(self):
        return self.str_groupName

    def setGroupName(self,str_groupName):
        self.str_groupName=str_groupName
    
    def setHeader(self,strct_header):
        self.strct_header=strct_header

    def setThreadCode(self,arr_threadCode):
        self.arr_threadCode=arr_threadCode

    def setTotalThread(self,int_totalThread):
        self.int_totalThread=int_totalThread
    
    def setGroupName(self,str_groupName):
        self.str_groupName=str_groupName

    def getFragmentURL(self):
        return self.str_fragmentViewURL+self.str_groupName
    
    def getGroupURL(self):
        return self.str_ggroupURL+self.str_groupName

    def getThreadURL(self,str_threadCode):
        return self.getGroupURL()+'/c/'+str_threadCode
        pass

    def crawTotalThreadNumber(self):
        self.int_totalPost = int(re.findall(r'>1.30\s+of\s+(\d+)<',requests.get(self.getGroupURL(),headers= self.strct_header).text)[0])
        
        if(self.bool_debugMode):
            self.writeLog('=========crawTotalThreadNumber=========')
            self.writeLog('Output name:')
            self.writeLog('int_totalPost')
            self.writeLog('Output type:')
            self.writeLog(type(self.int_totalPost))
            self.writeLog('Output value:')
            self.writeLog(self.int_totalPost)
            self.writeLog('=========crawTotalThreadNumber=========')
        
        pass

    def crawThreadCode(self):
        if(self.bool_debugMode):
            self.writeLog('=========crawThreadCode=========')
        self.crawTotalThreadNumber()
        for int_threadIndex  in range(1,self.int_totalPost,30):
            str_tempFragmentURL=self.getFragmentURL()+'%5B'+str(int_threadIndex)+'-'+str(int_threadIndex+29)+'%5D'
            responese = requests.get(str_tempFragmentURL,headers = self.strct_header)
            str_pageData = responese.text
            arr_threadCode = self.extractThreadCode(str_pageData)
            self.arr_threadCode+=arr_threadCode

            if(self.bool_debugMode):
                self.writeLog('['+str(int_threadIndex)+'-'+str(int_threadIndex+29)+']'+'\t\t'+str(responese))
        self.arr_threadCode = set(self.arr_threadCode) 
        if(self.bool_debugMode):
            self.writeLog('=========crawThreadCode=========')
     
        pass

    def extractThreadCode(self,str_pageData):
        
        str_threadCode = re.findall(r'<td class="subject">.*'+self.str_groupName+'\/([^\"]*).*<\/td>',str_pageData)
        
        if(self.bool_debugMode):
            self.writeLog('=========crawTotalThreadNumber=========')
            self.writeLog('Output name:')
            self.writeLog('str_threadCode')
            self.writeLog('Output type:')
            self.writeLog(type(str_threadCode))
            self.writeLog('Output value:')
            self.writeLog(str_threadCode)
            self.writeLog('=========crawTotalThreadNumber=========')

        
        if(self.bool_debugMode):
            self.writeLog('=========crawThreadData=========')
            self.writeLog('Output name: ')
            self.writeLog('str_threadCode')
            self.writeLog('Output type: ')
            self.writeLog(type(str_threadCode))
            self.writeLog('Ouput Value: ')
            self.writeLog(str_threadCode)
            self.writeLog('=========crawThreadData=========')

        return str_threadCode

        pass

    def getRawPage(self,str_threadCode):
        str_threadURL = self.getThreadURL(str_threadCode)
        responese = requests.get(str_threadURL,headers=self.strct_header)
        str_rawPageData = responese.text
        
        return str_rawPageData

        pass

    def crawThreadData(self):
        if(self.bool_debugMode):
            self.writeLog('=========crawThreadData=========')

        for str_threadCode in self.arr_threadCode:
            str_rawHTMLData = self.getRawPage(str_threadCode)
            self.c_webParser.feed(str_rawHTMLData)
            dict_threadData = self.c_webParser.toDictionary()
            self.dict_groupData[str_threadCode] = dict_threadData
            if(self.bool_debugMode):
                self.writeLog('Thread Code: ')
                self.writeLog(str_threadCode)
                self.writeLog('Dictionary Thread Data: ')
                self.writeLog(dict_threadData)
                
        if(self.bool_debugMode):
            self.writeLog('=========crawThreadData=========')

        pass
    
    def crawThreadData(self,str_threadCode):
        if(self.bool_debugMode):
        self.writeLog('=========crawThreadData=========')


        str_rawHTMLData = self.getRawPage(str_threadCode)
        self.c_webParser.feed(str_rawHTMLData)
        dict_threadData = self.c_webParser.toDictionary()
        self.dict_groupData[str_threadCode] = dict_threadData
        if(self.bool_debugMode):
            self.writeLog('Thread Code: ')
            self.writeLog(str_threadCode)
            self.writeLog('Dictionary Thread Data: ')
            self.writeLog(dict_threadData)
                
        if(self.bool_debugMode):
            self.writeLog('=========crawThreadData=========')

    def exportJsonFile(self):
        if(not os.path.exists('data/')):
            os.mkdir('data/')
        str_date = str(date.today())
        str_dataPath = 'data/'+str_date+self.str_groupName+'.json'
        fs_outputFile = open(str_dataPath,'w')
        json.dump(self.dict_groupData,fs_outputFile)
        fs_outputFile.close()

        if(self.bool_debugMode):
            self.writeLog('=========exportJsonFile=========')
            self.writeLog('output was saved on file:')
            self.writeLog(str_dataPath)
            self.writeLog('=========exportJsonFile=========')
        pass


    def writeLog(self,str_logString):
        if(not os.path.exists('log/')):
            os.mkdir('log/')

        try:
            str_filePath = 'log/'+str(date.today())+'.log'
            fs_logStream = open(str_filePath,'a')
            str_date = '['+str(date.today())+'][Crawler.py] '
            fs_logStream.write(str_date+str(str_logString)+'\n')
            fs_logStream.close()

        except:
            print('=========self.writeLog=========')
            print('except call')
            print('=========self.writeLog=========')

        pass