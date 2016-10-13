import resultadodia as res
import getxml as gxml

aux =1
while(aux!=0):
     aux = raw_input("Digite a opcao desejada\n")
     if(aux == "download"):
          gxml.downarquivo()
     elif(aux=="tratares"):
          x = res.resultado()
          print("Arquivo criado!")
          print( x.getCond(-1))
     else:
          print("Opcao inexistente")

