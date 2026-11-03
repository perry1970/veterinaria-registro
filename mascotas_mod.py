import json
def carga(clave_mascota,nombre,especie,edad,peso,clave_dueño):
    datos=[]
    try:
        mascotas_json=open(r"mascotas.json","r")
        datos=json.load(mascotas_json)
        mascotas_json.close()
        
        
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        
        mascotas_json=open(r"mascotas.json","w")
        json.dump(datos,mascotas_json)
        mascotas_json.close()
    finally:
        datos.append({"clave mascota":int(clave_mascota),"nombre":nombre,"especie":int(especie),"edad":int(edad),"peso":float(peso),"clave dueño":int(clave_dueño)})
        mascotas_json=open(r"mascotas.json","w")
        json.dump(datos,mascotas_json)
        mascotas_json.close()