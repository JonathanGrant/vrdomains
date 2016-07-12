import xml.etree.ElementTree as ET
import requests

with open("testList.txt") as testList:
    words = testList.read().splitlines()
    vrwords = []
    availDomains = []
    url = "https://api.namecheap.com/xml.response?ApiUser=apiexample&ApiKey=52b4c87ef7fd49cb96a915c0db68124&UserName=JonnyAPI&Command=namecheap.domains.check&ClientIp=192.168.1.109&DomainList="
    for word in words:
        vrwords.append("vr" + word)
        vrwords.append(word + "vr")
    for domain in vrwords:
        r = requests.get(url+domain)
        print(r.text)
#        tree = ET.parse(r.text)
#        root = tree.getroot()
#        for child in root:
#            print(child)