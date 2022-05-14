mtnd = dict()

estados = input().split()
alfEntrada = input().split()
alfFita = input().split()
simbEsquerda = input()
simbBranco = input()
nTransicoes = int(input())

for i in range(nTransicoes):
    origem, carAlf, destino, carFita, direcao = input().split()
    key = (origem, carAlf)
    if key not in mtnd:
        mtnd[key] = []
    mtnd[key].append([destino, carFita, direcao])

estadoInicial = input()
estadosFinais = input().split()
palavras = input().split()

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

for palavra in palavras: 
    if  testaPalavra(palavra):
        print('S')
    else:
        print('N')