# -*- coding: utf-8 -*-

import chave
import requests
import urllib

googleKey = chave.chaveAcesso
s = requests.Session()

apiUrl = 'https://maps.googleapis.com/maps/api/geocode/json?address={{0}}&key={0}'.format(googleKey)
endereco = urllib.quote('EMEF JOSE PEDRO LEITE CORDEIRO, DR., São Paulo, SP')


def retornaLatLng(endereco):
    r = s.get(apiUrl.format(endereco), verify=False)
    resposta = r.json()
    resultados = resposta['results']
    return resultados[0]['geometry']['location']
