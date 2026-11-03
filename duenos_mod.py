import json
def carga(clave_dueño,nombre,porcentaje_descuento,fecha):
    datos=[]
    try:
        duenos_json=open(r"duenos.json","r")
        datos=json.load(duenos_json)
        duenos_json.close()
        
        
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        
        duenos_json=open(r"duenos.json","w")
        json.dump(datos,duenos_json)
        duenos_json.close()
    finally:
        datos.append({"clave":int(clave_dueño),"nombre":nombre,"porcentaje de descuento":float(porcentaje_descuento),"fecha":fecha})
        duenos_json=open(r"duenos.json","w")
        json.dump(datos,duenos_json)
        duenos_json.close()
        
def lectura():
    datos=[]
    try:
        duenos_json=open(r"duenos.json","r")
        datos=json.load(duenos_json)
        duenos_json.close()
        
        
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        
        duenos_json=open(r"duenos.json","w")
        json.dump(datos,duenos_json)
        duenos_json.close()
        
    return datos