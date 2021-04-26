from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import json
import re 
import nltk
import io

class TextProcess:
    def __init__(self,bool_debugMode = False):
        self.bool_debugMode = bool_debugMode
        self.c_stemmer = PorterStemmer()
        self.arr_stopWords = set(stopwords.words('english'))
        self.c_lemma = WordNetLemmatizer()
        self.arr_month=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Dec', 'Nov', 'Oct']
        pass

    def cleanURL(self,str_line):
        str_urlClear= re.sub(r'http\S+',' ',str_line)

        if(self.bool_debugMode):
            writeLog('=========cleanURL=========') 
            writeLog('Input name:')
            writeLog('str_line')
            writeLog('Input type:')
            writeLog(type(str_line))
            writeLog('Input value:')
            writeLog(str_line)
            writeLog(' ')
            writeLog('Output name:')
            writeLog('str_urlClear')
            writeLog('Output type:')
            writeLog(type(str_urlClear))
            writeLog('Output value:')
            writeLog(str_urlClear)
            writeLog('=========cleanURL=========')  

        return str_urlClear
        pass

    def cleanSymbol(self,str_line):
        str_symbolClear= re.sub(r'[^a-zA-Z]',' ',str_line)

        if(self.bool_debugMode):
            writeLog('=========cleanSymbol=========') 
            writeLog('Input name:')
            writeLog('str_line')
            writeLog('Input type:')
            writeLog(type(str_line))
            writeLog('Input value:')
            writeLog(str_line)
            writeLog(' ')
            writeLog('Output name:')
            writeLog('str_symbolClear')
            writeLog('Output type:')
            writeLog(type(str_symbolClear))
            writeLog('Output value:')
            writeLog(str_symbolClear)
            writeLog('=========cleanSymbol=========')  

        return str_symbolClear
        pass
    
    def cleanStopWord(self,arr_token):
        arr_clearStopwords =[ token for token in arr_token if token not in self.arr_stopWords ]

        
        if(self.bool_debugMode):
            writeLog('=========cleanStopWord=========') 
            writeLog('Input name:')
            writeLog('cleanStopWord')
            writeLog('Input type:')
            writeLog(type(cleanStopWord))
            writeLog('Input value:')
            writeLog(cleanStopWord)
            writeLog(' ')
            writeLog('Output name:')
            writeLog('arr_clearStopwords')
            writeLog('Output type:')
            writeLog(type(arr_clearStopwords))
            writeLog('Output value:')
            writeLog(arr_clearStopwords)
            writeLog('=========cleanStopWord=========')  


        return arr_clearStopwords

    def tokenize(self,str_line):
        arr_token = word_tokenize(str_line)
        
        if(self.bool_debugMode):
            writeLog('=========tokenize=========') 
            writeLog('Input name:')
            writeLog('str_line')
            writeLog('Input type:')
            writeLog(type(str_line))
            writeLog('Input value:')
            writeLog(str_line)
            writeLog(' ')
            writeLog('Output name:')
            writeLog('arr_token')
            writeLog('Output type:')
            writeLog(type(arr_token))
            writeLog('Output value:')
            writeLog(arr_token)
            writeLog('=========tokenize=========')  


        return arr_token

        pass

    def stemming(self,arr_token):
        arr_stemming = [self.c_stemmer.stem(token) for token in arr_token]
        
        if(self.bool_debugMode):
            writeLog('=========stemming=========') 
            writeLog('Input name:')
            writeLog('arr_token')
            writeLog('Input type:')
            writeLog(type(arr_token))
            writeLog('Input value:')
            writeLog(arr_token)
            writeLog(' ')
            writeLog('Output name:')
            writeLog('arr_stemming')
            writeLog('Output type:')
            writeLog(type(arr_stemming))
            writeLog('Output value:')
            writeLog(arr_stemming)
            writeLog('=========stemming=========')  
        
        return arr_stemming 

        pass

    def lengthFilter(self,arr_token):
        arr_filterToken = [token for token in arr_token if len(token) > 2]

        if(self.bool_debugMode):
            writeLog('=========LengthFilter=========') 
            writeLog('Input name:')
            writeLog('arr_token')
            writeLog('Input type:')
            writeLog(type(arr_token))
            writeLog('Input value:')
            writeLog(arr_token)
            writeLog(' ')
            writeLog('Output name:')
            writeLog('arr_filterToken')
            writeLog('Output type:')
            writeLog(type(arr_filterToken))
            writeLog('Output value:')
            writeLog(arr_filterToken)
            writeLog('=========LengthFilter=========')  
        
        return arr_filterToken

        pass
    
    def lemmatization(self,arr_token):
        arr_lemma=  [self.c_lemma.lemmatize(word=str_word,pos='v') for str_word in arr_token] 

        if(self.bool_debugMode):
            writeLog('=========lemmatization=========') 
            writeLog('Input name:')
            writeLog('arr_token')
            writeLog('Input type:')
            writeLog(type(arr_token))
            writeLog('Input value:')
            writeLog(arr_token)
            writeLog(' ')
            writeLog('Output name:')
            writeLog('arr_lemma')
            writeLog('Output type:')
            writeLog(type(arr_lemma))
            writeLog('Output value:')
            writeLog(arr_lemma)
            writeLog('=========lemmatization=========')  
        
        return arr_lemma

        pass
   
    def processText(self,str_line):
        str_textData= str_line.lower()
        str_textData = cleanURL(str_textData)
        str_textData=cleanSymbol(str_textData)
        arr_token=tokenize(str_textData)
        arr_token = cleanStopWord(arr_token)
        arr_token = lemmatization(arr_token)
        arr_token = lengthFilter(line)
        str_textData = ' '.join(arr_token)

        if(self.bool_debugMode):
            writeLog('=========processText=========') 
            writeLog('Input name:')
            writeLog('str_line')
            writeLog('Input type:')
            writeLog(type(str_line))
            writeLog('Input value:')
            writeLog(str_line)
            writeLog(' ')
            writeLog('Output name:')
            writeLog('arr_lemma')
            writeLog('Output type:')
            writeLog(type(arr_lemma))
            writeLog('Output value:')
            writeLog(arr_lemma)
            writeLog('=========processText=========')  
        

        return str_textData

        pass

    def convertTime(self,str_line):
        arr_time=re.findall(r'(\w+)\s+(\d+),\s+(\d+),\s+(\d+):\d+:\d+\s+(\w+)',str_line)[0]
        int_time = (self.arr_month.index(arr_time[0]))*30*24+int(arr_time[1])*24+int(arr_time[2])*365*24+int(arr_time[3])
        if(arr_time[4]=='PM'):
            int_time+=12

        if(self.bool_debugMode):
            writeLog('=========convertTime=========') 
            writeLog('Input name:')
            writeLog('str_line')
            writeLog('Input type:')
            writeLog(type(str_line))
            writeLog('Input value:')
            writeLog(str_line)
            writeLog(' ')
            writeLog('Output name:')
            writeLog('int_time')
            writeLog('Output type:')
            writeLog(type(int_time))
            writeLog('Output value:')
            writeLog(int_time)
            writeLog('=========convertTime=========')  
        
        return int_time

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