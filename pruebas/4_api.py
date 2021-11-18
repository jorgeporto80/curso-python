import requests

url = 'http://172.23.0.42:8087/api/comex/saldo?nroCuenta=1000008783&tipoDeCuenta=1'
resp = requests.get(url)
mi_diccionario = resp.json()

print (resp)
print(type(mi_diccionario))
print(mi_diccionario)
print("Valor:", mi_diccionario['saldoEfectivo'])

