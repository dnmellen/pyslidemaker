# -*- coding: utf-8 -*-

__author__ = "Diego Navarro"
__email__ = "dnmellen@gmail.com"
__version__ = 0.7


from lxml import etree
from lxml.builder import ElementMaker


class XmlGenerator:
    """
    This class generates a valid XML file in order to
    get autochanging wallpapers.
    """


    def __init__(self,items,slide = 300.0, trans = 1.5):
        '''
        Constructor

        '''
        
        self.items = items
        self.slide_duration = slide
        self.trans_duration = trans 

        # Initialize XML
        self.E = ElementMaker()
        self.xml = self.E.background(
                       self.E.starttime(
                           self.E.hour("00")
                           self.E.minute("00")
                           self.E.second("01")
                       )
                   )

    def get_slide_duration(self):
        return unicode(self.slide_duration)


    def get_trans_duration(self):
        return unicode(self.trans_duration)


    def save_to(self,path):
        '''
        Saves the xml to a file
        '''   


        for i, e in enumerate(self.items):
            self.xml.append(self.E.static(
                               self.E.duration(self.get_slide_duration()),
                               self.E.file(e)
                               ),
                            self.E.transition(
                                   self.E.duration(self.get_trans_duration()),
                                   self.E.from(e),
                                   self.E.to(
                                       self.items[(i + 1) % len(self.items)])
                               )
                           ) 

        f = open(path, 'w')
        f.write(etree.tostring(self.xml, xml_declaration=True, 
                               encoding='utf-8', pretty_print=True))
        f.close()

