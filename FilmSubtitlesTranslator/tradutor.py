#!/usr/bin/python
# -*- coding: utf-8 -*-

import goslate

gs = goslate.Goslate()

print('Ingles;Portugues')

try:
    f = open('arquivo_2.txt')
    texto=1
    frase=''
    for linha in f.readlines():
        limpa = linha.strip('\n')
        limpa = limpa.replace('-', '')
        if len(limpa)>0:
        	if limpa[0].isdigit():
        		texto=0
        		if len(frase)>0:
        			print(frase+';'+gs.translate(frase,'pt'))
        		frase=''
        	else:
        		frase=frase+' '+limpa
        		texto=1
        		#print(limpa)
    f.close()
except IOError:
    print('Não foi possível abrir arquivo')
    sys.exit(1)