# -*- coding: utf-8 -*-
import datetime
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
fp = open("bloombreg.txt","r+") 
epg = ET.parse("./epg.xml")
period = list()
for eachline in fp.readlines():
    
    if eachline.startswith('201'):
        newStr = eachline.strip()
        year = int(newStr.split('-')[0])
        month = int(newStr.split('-')[1])
        day = int(newStr.split('-')[2])
        profix_day = str(year)+str('%02d'%month)+str('%02d'%day)
    elif eachline.startswith('\n'):
        newStr = eachline.strip()
        continue
    elif eachline.startswith('	'):
        newStr = eachline.strip()
        continue
    else:
        newStr = eachline.strip()
        fstr = newStr.split('\t ')
        time = int(fstr[0].replace(':', ''))
        timecode = '%04d'%time+'00'
        begin_time = profix_day+timecode
        period.append(begin_time)
        root = epg.getroot()
        ChannelPeriod = root.find(".//ScheduleData/ChannelPeriod")
        ChannelPeriod.set('beginTime', period[0])
        ChannelPeriod.set('endTime', period[-1])
        event = Element("Event", {"beginTime":"", "duration":""})
        ChannelPeriod.append(event)
        eventID = Element("EventID")
        eventID.text = "09"
        epgproduction = Element("EpgProduction")
        event.append(eventID)
        event.set('beginTime',begin_time)
        event.append(epgproduction)
        epgtext = Element("EpgText",{"language":"mon"} )
        epgproduction.append(epgtext)
        name = Element("Name")
        epgtext.append(name)
        name.text = fstr[1]
        import sys  
        reload(sys)
        sys.setdefaultencoding("utf-8")   
        epg.write("./out34.xml", encoding="utf-8",xml_declaration=True)
fp.close()

