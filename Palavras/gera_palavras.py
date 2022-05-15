import csv

A = []
B = []

with open('palavras.csv', 'w', newline='', encoding='utf-8') as palavras:
  dados_csv = csv.writer(palavras, delimiter=' ')
  for i in range(0,100):
    A.append('a')
    B.append('b')
    result = ''.join(A+B)
    dados_csv.writerow(''.join(A+B))

