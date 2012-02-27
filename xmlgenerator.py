# -*- coding: utf-8 -*-

__author__ = "Diego Navarro"
__email__ = "dnmellen@gmail.com"
__version__ = 0.7


from lxml import etree
from lxml.builder import ElementMaker
import os

UBUNTU_WALLPAPERS = '/tmp/ubuntu-wallpapers.xml'
#UBUNTU_WALLPAPERS = '/usr/share/gnome-background-properties/ubuntu-wallpapers.xml'


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
                           self.E.hour("00"),
                           self.E.minute("00"),
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
                               )
                           )
            self.xml.append(self.E.transition(
                                self.E.duration(self.get_trans_duration()),
                                self.E('from', e),
                                self.E.to(
                                    self.items[(i + 1) % len(self.items)])
                               )
                           ) 

        f = open(path, 'w')
        f.write(etree.tostring(self.xml, xml_declaration=True, 
                               encoding='utf-8', pretty_print=True))
        f.close()


    @staticmethod
    def install_wallpaper(fname):
        '''
        For Ubuntu 11.10 and above it's needed to add .xml file in
        ubuntu-wallpapers.xml
        '''

        E = ElementMaker()
        if os.access(UBUNTU_WALLPAPERS, os.W_OK):
            wallpaper = E.wallpaper(
                            E.name('slideshow1'), 
                            E.filename(fname), 
                            E.options('zoom') 
                        )
            wallpaper.attrib['deleted'] = 'false'

            doc = None
            with open(UBUNTU_WALLPAPERS) as f:
                parser = etree.XMLParser(remove_blank_text=True)
                doc = etree.parse(f, parser)

            if doc:
                doc.getroot().append(wallpaper)
                data =  etree.tostring(doc, pretty_print=True,
                                       encoding='utf-8', 
                                       xml_declaration=True)

                with open(UBUNTU_WALLPAPERS, 'w') as f:
                    f.write(data)
                


