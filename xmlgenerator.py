#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

__author__ = "Diego Navarro"
__email__ = "dnmellen@gmail.com"
__version__ = 0.6


import codecs


class XmlGenerator:
    """This class generates a valid XML file in order to
    get autochanging wallpapers.

    """

    _HEADER = '<?xml version="1.0" encoding="UTF-8"?>\n'+\
              '<background>\n'+\
              '  <starttime>\n'+\
              '    <hour>0</hour>\n'+\
              '    <minute>00</minute>\n'+\
              '    <second>01</second>\n'+\
              '  </starttime>\n'

    _BOTTOM = '</background>\n'

    def __init__(self,items,slide = 300.0, trans = 1.5):
        
        self.items = items
        self.slide_duration = slide
        self.trans_duration = trans 

    def getSlideDuration(self):
        return self.slide_duration

    def getTransDuration(self):
        return self.trans_duration

    def saveTo(self,path):
    
        output = codecs.open(path,"w","utf-8")
        output.writelines(XmlGenerator._HEADER)

        for i in range(len(self.items)):
            output.writelines('  <static>\n'+
                              '    <duration>'+str(self.getSlideDuration())+
                              '</duration>\n'+
                              '    <file>'+(self.items[i])+'</file>\n'+
                              '  </static>\n'+
                              '  <transition>\n'+
                              '    <duration>'+str(self.getTransDuration())+
                              '</duration>\n'+
                              '    <from>'+(self.items[i])+'</from>\n'+
                              '    <to>'+(self.items[(i+1)%len(self.items)])+
                              '</to>\n'+
                              '  </transition>\n') 
        output.writelines(XmlGenerator._BOTTOM) 
        output.close()
