import requests
import urllib

class prefeitura:
    def __init__(self):
        self.s = requests.Session()
        self.url = 'http://portal.sme.prefeitura.sp.gov.br///School/List?AdministrativeUnitSuperiorId=&AdministrativeUnitTypeId=&port=:80&schoolName={0}'

    def getLatLng(self, nomeEscola):
        nomeEscola = urllib.quote(nomeEscola)
        r = self.s.get(self.url.format(nomeEscola))
        dados = r.json()[0]
        resultado = {'lat': dados['Latitude'], 'lng': dados['Longitude']}
        return resultado
        