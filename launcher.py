# from Crawler import Crawler
import sys
import json
import io
from TextProcess import TextProcess

if __name__ == '__main__':
    # str_groupName = sys.argv[1]
    file_stream = open('iqtree.json')
    dict_data = json.load(file_stream)
    textProcess = TextProcess()
    dict_processData =textProcess.processData(dict_data)
    fs_fileStream = open('processText.json','w')
    json.dump(dict_processData,fs_fileStream)
    fs_fileStream.close()
