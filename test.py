import json
import duenos_mod

clave_confirmacion="n"

mascotas_json=open(r"mascotas.json","r")
datos=json.load(mascotas_json)
print(datos)
print(datos[0]["clave dueño"])


datos=duenos_mod.lectura()
print(datos)
print(datos[0])
print(datos[0]["clave"])

while clave_confirmacion!="s":
    clave_dueño=input("clave del dueño ")
    print(clave_confirmacion)
    if datos[0]["clave"]==int(clave_dueño):
        print("true")
        clave_confirmacion="s"
        
    else:
        print("false")
        
    print(clave_confirmacion)    


        
