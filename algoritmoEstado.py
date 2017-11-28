# -*- coding: utf-8 -*-

import csv
import googleGeocoding
import consultaPrefeitura

p = consultaPrefeitura.prefeitura()
arquivo = open('./prefeitura.csv', 'r')
csvFile = csv.reader(arquivo, delimiter=';')
cabecalho = csvFile.next()
cabecalho

saida = open('./prefeitura_geo.csv', 'wb')
csvSaida = csv.writer(saida, delimiter=';')
cabecalhoSaida = cabecalho + ['lat', 'lng']
csvSaida.writerow(cabecalhoSaida)

for linha in csvFile:
    latLng = p.getLatLng('{0}'.format(linha[1])) 
    linhaSaida = linha + [latLng['lat'], latLng['lng']]
    csvSaida.writerow(linhaSaida)

arquivo.close()
saida.close()

