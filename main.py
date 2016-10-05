import xml.etree.ElementTree as ET
from datetime import datetime
import getxml as gtxml

gtxml.downarquivo()


agora = datetime.now()

tree = ET.parse('previsao.xml')
root = tree.getroot()

print root[4][1]
for neighbor in root.iter('temperature'):
     print neighbor.attrib
for neighbor in root.iter('precipitation'):
     print neighbor.attrib




'''maxima = []
minima = []

for x in range(3, 7):
    maxima.append(root[x][2].text)
    minima.append(root[x][3].text)

a = str(agora.day) +"." + str(agora.month) + "." + str(agora.hour) + "." + str(agora.minute)

texto = open("Previsoes/"+a,'w')
texto.write("Maxima \n")
for x in range (0,4):
    texto.write(maxima[x]+ "\n")
texto.write("Minima\n")
for x in range (0,4):
    texto.write(minima[x]+"\n")
'''