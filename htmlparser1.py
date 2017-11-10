# -*- coding: utf-8 -*-
from html.parser import HTMLParser  #package

class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print("encounter a astart tag",tag)
        
    def handle_endtag(self,tag):
        print("encounter a end tag",tag)    

    def handle_data(self,data):
        print("encounter some data",data)
        
parser= MyHTMLParser()  #execution of html instance in python
parser.feed('<html><head><title>test</title></head>'
            '<body><h1>parse me!</h1></body></html>')        