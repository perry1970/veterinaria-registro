import json
import re
import duenos_mod
import mascotas_mod

datos=[]


menu=int(input("menu "))
while menu!=6:
    datos=[]
    match menu:
        case 1:
            
            clave_dueño=input("clave del dueño ")
            nombre=input("nombre ")
            porcentaje_descuento=input("porcentaje de descuento ")
            dia=input("dia ")
            mes=input("mes ")
            año=input("año ")
            fecha=[int(dia),int(mes),int(año)]
            
            duenos_mod.carga(clave_dueño,nombre,porcentaje_descuento,fecha)
            



            
                

        case 2:
            clave_confirmacion="n"
            clave_mascota=input("clave de la mascota ")
            nombre=input("nombre ")
            especie=input("especie ")
            edad_mascota=input("edad en meses ")
            peso_mascota=input("peso en kg ")
            
            datos=duenos_mod.lectura()
            while clave_confirmacion=="n":
                clave_dueño=input("clave del dueño ")
                for dueño in datos:
                    if dueño["clave"]==int(clave_dueño):
                        clave_confirmacion="s"
                if clave_confirmacion=="n":
                    print("no existe la clave")
                
                
            mascotas_mod.carga(clave_mascota,nombre,especie,edad_mascota,peso_mascota,clave_dueño)
            
            
            
            
        case 3:
            try:
                veterinarios_json=open(r"veterinarios.json","r")
                #aqui va la funcion
            except FileNotFoundError:
                print("archivo no encontrado, creando archivo")
                veterinarios_json=open(r"veterinarios.json","x")
            finally:
                veterinarios_json.close()
        case 4:
            print("aqui va la funcion")
        case 5:
            print("aqui va la funcion")
    menu=int(input("menu "))
