import json
import time
import csv

def readData():
  fData = open('data.json')
  data = json.load(fData)
  fData.close()
  return data

data = readData()

mtnd = dict()

estados = data["estados"].split()
alfEntrada = data["alfabeto"].split()
alfFita = data["alfFita"].split()
simbEsquerda = data["simbEsquerda"]
simbBranco = data["simbBranco"]
nTransicoes = int(data["nTransicoes"])

for i in range(nTransicoes):
    origem, carAlf, destino, carFita, direcao = data["quintuplas"][i].split()
    key = (origem, carAlf)
    if key not in mtnd:
        mtnd[key] = []
    mtnd[key].append([destino, carFita, direcao])

estadoInicial = data["estadoInicial"]
estadosFinais = data["estadosFinais"].split()
palavras = data["palavras"].split()

def testaPalavra(palavra):

  fita=list((simbEsquerda+palavra+simbBranco))
  caminho=[(estadoInicial, 1, fita)]
  pValida=False
  
  while True:

    t=caminho.pop()
    estadoAtual=t[0]
    posicao=t[1]
    itensFita=t[2]  
      
    if (estadoAtual,itensFita[posicao]) in mtnd:

      for aux in mtnd[(estadoAtual,itensFita[posicao])]:
        aux2 = []
        for string in itensFita:
          aux2.append(string)
				
        if aux2[posicao] == simbBranco:
          aux2.append(simbBranco)
          itensFita.append(simbBranco)

        aux2[posicao] = aux[1]

        if aux[2] == 'D':
          caminho.append((aux[0], (posicao + 1), aux2))
			
        elif aux[2] == 'E': 
          caminho.append((aux[0], (posicao - 1), aux2))
			
        elif aux[2] == 'I':
          caminho.append((aux[0], posicao, aux2))
 
    else:
      if (estadoAtual in estadosFinais):
        return not pValida
      if (len(caminho)==0):
        return pValida

with open('dados.csv', 'w', newline='', encoding='utf-8') as dados:
  dados_csv = csv.writer(dados)
  dados_csv.writerow(['Palavra', 'Tamanho da palava', 'Tempo (s)'])

  for palavra in palavras: 
      tempo = []
      for t in range(0, 100):
          inicio = time.time()
          resultado = testaPalavra(palavra)
          fim = time.time()
          tempo.append((fim - inicio))

      if  resultado:
          print('S')
      else:
          print('N') 
      dados_csv.writerow([palavra, len(palavra), sum(tempo)/len(tempo)])
