# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

import PyQt4,PyQt4.QtGui,sys
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature
from Ui_DDishEPG import Ui_Dialog

class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
    @pyqtSignature("")
    def on_openEPG_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        dlg = PyQt4.QtGui.QFileDialog(self)  
        self.EPGFILE.setText(dlg.getOpenFileName())
        global EPGtxt 
        EPGtxt = str(self.EPGFILE.text())
    
    @pyqtSignature("")
    def on_openTem_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        dlg = PyQt4.QtGui.QFileDialog(self)  
        self.Channel_tem.setText(dlg.getOpenFileName())
        global Templatexml 
        Templatexml = str(self.Channel_tem.text())

    
    @pyqtSignature("")
    def on_Generate_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        import datetime
        import time
        import xml.etree.ElementTree as ET
        from xml.etree.ElementTree import Element
        import copy
        def parsetempxml(templatexml):
            temp = ET.parse(templatexml)
            return temp
            
        def readepgtxt(epgtxt):
            epgfile = open(epgtxt,"r+")
            epglines = epgfile.readlines()
            return epglines
            epgfile.close()
            
        def generatebeginTime(epglines):
            begin_time_list = list()
            for eachline in epglines:
                if eachline.startswith('201'):
                    neweachline = eachline.strip()
                    day = neweachline
                elif eachline.startswith('\n'):
                    neweachline = eachline.strip()
                    continue
                else:
                    neweachline = eachline.strip()
                    feachline = neweachline.split('\t ')
                    time = feachline[0]+':00'
                    begin_time = day+" "+time
                    begin_time_list.append(begin_time)
            return begin_time_list
            
        def generatebeginTimecode(begin_time_list):
            beginTimecode_list=list()
            for i in range(0, len(begin_time_list)):
                datetime = begin_time_list[i].split(' ')[0]
                time = begin_time_list[i].split(' ')[1]
                year = int(datetime.split('-')[0])
                month = int(datetime.split('-')[1])
                day = int(datetime.split('-')[2])
                hour = int(time.split(':')[0])
                minute = int(time.split(':')[1]) 
                second ='00'
                beginTimecode = str(year)+str('%02d'%month)+str('%02d'%day)+str('%02d'%hour)+str('%02d'%minute)+second
                beginTimecode_list.append(beginTimecode)
            return beginTimecode_list
            
        def generateendTime(begin_time_list):   
            end_time_list = copy.copy(begin_time_list)
            end_time_list.reverse()
            end_time_list.pop()
            end_time_list.reverse()
            last_time=end_time_list[-1].split(' ')[0]+' 23:59:59'
            end_time_list.append(last_time)
            return end_time_list
            
        def calduration(begin_time_list,end_time_list):
            duration_list=list()
            for i in range(0, len(begin_time_list)):
                begin=time.strptime(begin_time_list[i], "%Y-%m-%d %H:%M:%S")
                end=time.strptime(end_time_list[i], "%Y-%m-%d %H:%M:%S")
                begin=datetime.datetime(begin[0],begin[1],begin[2],begin[3],begin[4],begin[5])
                end=datetime.datetime(end[0],end[1],end[2],end[3],end[4],end[5])
                duration = (end-begin).seconds
                duration_list.append(duration)
            return duration_list
            
        def generateChannelbeginTime(beginTimecode_list):    
            ChannelbeginTime = beginTimecode_list[0]
            return ChannelbeginTime
            
        def generateChannelendTime(beginTimecode_list):    
            ChannelendTime = beginTimecode_list[-1]
            return ChannelendTime
            
        def generateName(epglines):
            name_list = list()
            for eachline in epglines:
                if eachline.startswith('201'):
                    continue
                elif eachline.startswith('\n'):
                    continue
                else:
                    neweachline = eachline.strip()
                    feachline = neweachline.split('\t ')
                    name = str(feachline[1])
                    name_list.append(name)
            return name_list
            
        def generateEventId(epglines):    
            eventId_list = list()
            for eachline in epglines:
                if eachline.startswith('201'):
                    continue
                elif eachline.startswith('\n'):
                    continue
                else:
                    neweachline = eachline.strip()
                    eventId_list.append(len(eventId_list))
            return eventId_list
        
        def writeXML(xml, elements, ChannelbeginTime, ChannelendTime):
            
            for element in elements:
                root = xml.getroot()
                ChannelPeriod = root.find(".//ScheduleData/ChannelPeriod")
                ChannelPeriod.set('beginTime', ChannelbeginTime)
                ChannelPeriod.set('endTime', ChannelendTime)
                event = Element("Event", {"beginTime":"", "duration":""})
                event.set('beginTime',element[2])
                event.set('duration',str(element[3]))
                ChannelPeriod.append(event)            
                eventID = Element("EventID")
                eventID.text = str(element[1])
                event.append(eventID)
                epgproduction = Element("EpgProduction")                
                event.append(epgproduction)
                epgtext = Element("EpgText",{"language":"mon"})
                epgproduction.append(epgtext)
                name = Element("Name")
                epgtext.append(name)
                name.text = element[0]
                
            import sys  
            reload(sys)
            sys.setdefaultencoding("utf-8")   
            xml.write("./out136.xml", encoding="utf-8", xml_declaration=True)
                
                
        xml = parsetempxml(Templatexml)
#        print xml
        epglines = readepgtxt(EPGtxt)
#        print epglines
        Name = generateName(epglines)
#        print len(Name)
        EventId = generateEventId(epglines)
#        print len(EventId)
        begin_time_list = generatebeginTime(epglines)
#        print len(begin_time_list)
        end_time_list = generateendTime(begin_time_list)
#        print len(end_time_list)
        duration = calduration(begin_time_list,end_time_list)
#        print len(duration)
        beginTimecode = generatebeginTimecode(begin_time_list)
#        print len(beginTimecode)
        ChannelbeginTime = generateChannelbeginTime(beginTimecode)
#        print len (ChannelbeginTime)
        ChannelendTime = generateChannelendTime(beginTimecode)
#        print len (ChannelendTime)
        elements = zip(Name,EventId,beginTimecode,duration)
#        print xmlelements
        writeXML(xml, elements, ChannelbeginTime, ChannelendTime)
        
        
        
if __name__ == "__main__":  
  
    app = PyQt4.QtGui.QApplication(sys.argv)  
  
    myapp = Dialog()  
  
    myapp.show()  
  
sys.exit(app.exec_())
