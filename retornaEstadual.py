from escolasMapa import a

def getLatLng(escola):
    resultado=[i for i in a if i['e'] == escola][0]
    resultado = {'lat': resultado['lt'], 'lng': resultado['ln']}
    return resultado