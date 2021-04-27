from requests.structures import CaseInsensitiveDict
import requests
import re
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
            self.writeLog(type(self.str_threadCode))
            self.writeLog('Output value:')
            self.writeLog(self.str_threadCode)
            self.writeLog('=========crawTotalThreadNumber=========')

        return str_threadCode

        pass

    def writeLog(self,str_logString):
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