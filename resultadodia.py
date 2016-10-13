import xml.etree.ElementTree as ET
from datetime import datetime
import getxml as gtxml


class resultado:
    #agora -Pega o tempo no momento que o objeto eh criado
    #root -Objeto para tratar o texto xml
    #Temp -Vetor que fica armazenado todas as temperaturas
    #Max - Vetor que armazena as temperaturas maximas
    #Min - Vetor que armazena as temperaturas minimas
    #Cond - Vetor que armazena as condicoes de tempo
    def __init__(self):
        self.agora = datetime.now() #pega o dia e o horario da criacao do objeto
        tree = ET.parse('previsao.xml') #cria uma arvore com o xml
        self.root=tree.getroot() #pega a raiz de criacao
        self.Temp = []
        self.Max = []
        self.Min = []
        self.Cond = []
        for xmlgetter in self.root.iter('temperature'): #for que pega as temperaturas, maximos e minimos
            self.Temp.append(xmlgetter.attrib)
            self.Max.append(xmlgetter.get('max'))
            self.Min.append(xmlgetter.get('min'))

        for xmlgetter in self.root.iter('symbol'): #for que pega as condicoes atuais
            self.Cond.append(xmlgetter.get('name'))


#getters
    def getDate(self):
        return self.agora
    def getRoot(self):
        return self.root

    def getTemp(self,indice):
        if (indice<0):
            return self.Temp
        return self.Temp[indice]

    def getMax(self,indice):
        if(indice <0 ):
            return self.Max
        return self.Max[indice]


    def getMin(self,indice):
        if (indice < 0):
            return self.Min
        return self.Min[indice]

    def getCond(self,indice):
        if (indice<0):
            return self.Cond
        return self.Cond[indice]

