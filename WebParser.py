from html.parser import HTMLParser
import json
import io
import re

class WebParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.initialize()
        pass

    def initialize(self):
        self.int_commentSectionCounter =0
        self.bool_inCommentSection = False

        self.int_dateSectionCounter =0
        self.bool_inDateSection=False

        self.int_topicSectionCounter =0
        self.bool_inTopicSection=False
        
        self.arr_postData =[] 
        self.arr_date=[]
        self.arr_topic=[]
        
        self.str_comment=''
        self.str_date=''
        self.str_topic=''

    def feed(self,str_data):
        self.initialize()
        HTMLParser.feed(self,str_data)
        pass
    
    def handleStartDiv(self, arr_attribute):
        for attribute in arr_attribute:
            if(attribute[0]=='class' and attribute[1]=='ptW7te'): 
                self.bool_inCommentSection = True

        if(self.bool_inCommentSection):
            self.int_commentSectionCounter+=1

        pass

    def handleEndDiv(self):
        if(self.bool_inCommentSection):
            self.int_commentSectionCounter-=1
            if(not self.int_commentSectionCounter):
                self.bool_inCommentSection=False
                self.arr_postData.append(self.str_comment)
                self.str_comment=''
        pass

    def handleDivData(self,str_data):
        str_data = str_data.strip().replace('\n',' ')
        str_data = re.sub(r'\s+',' ',str_data)
        if(len(str_data)>2):
            self.str_comment +=str_data+' '

        pass

    def handleStartSpan(self,arr_attribute):
        for attribute in arr_attribute:
            if(attribute[0]=='class' and attribute[1]=='zX2W9c'):
                self.bool_inDateSection = True
            if(self.bool_inDateSection):
                self.int_dateSectionCounter +=1
        pass

    def handleEndSpan(self):
        if(self.bool_inDateSection):
            self.int_dateSectionCounter-=1
            if(not self.int_dateSectionCounter):
                self.bool_inDateSection=False
                self.arr_date.append(self.str_date)
                self.str_date=''
        pass

    def handleSpanData(self,str_data):
        self.str_date+=str_data
        pass

    def handleStartTopic(self,arr_attribute):
        for attribute in arr_attribute:
            if(attribute[0]=='class' and attribute[1]=='KPwZRb'):
                self.bool_inTopicSection = True
            if(self.bool_inTopicSection):
                self.int_topicSectionCounter +=1
        pass

    def handleEndTopic(self):
        if(self.bool_inTopicSection):
            self.int_topicSectionCounter-=1
            if(not self.int_topicSectionCounter):
                self.bool_inTopicSection=False
                self.arr_topic.append(self.str_topic)
                self.str_topic=''
        pass

    def handleTopicData(self,str_data):
        self.str_topic+=str_data
        pass

    def handle_starttag(self,str_tag,arr_attribute):
        if(str_tag =='div'):
            self.handleStartDiv(arr_attribute)
        elif(str_tag=='span'):
            self.handleStartSpan(arr_attribute)
        elif(str_tag =='h1'):
            self.handleStartTopic(arr_attribute)
        pass

    def handle_endtag(self,str_tag):
        if(str_tag =='div'):
            self.handleEndDiv()
        elif(str_tag=='span'):
            self.handleEndSpan()
        elif(str_tag=='h1'):
            self.handleEndTopic()
        pass

    def handle_data(self,str_data):
        if(self.bool_inCommentSection):
            self.handleDivData(str_data)
        elif(self.bool_inDateSection):
            self. handleSpanData(str_data)
        elif(self.bool_inTopicSection):
            self.handleTopicData(str_data)
        pass

    def toDictionary(self):
        dict_data = {
            'topic':self.arr_topic[0],
            'initializeDate':self.arr_date[0],
            'timeStamp':self.arr_date[-1],
            'content':self.arr_postData
        }

        return dict_data

