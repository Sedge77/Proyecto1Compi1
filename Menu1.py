from AnalizadorCss import *
from Token import *

print("")
print("=================MENU DE OPCIONES=================")
print("1-Analisis JS")
print("")
print("2-Analisis Css")
print("")
print("3-Analisis HTML")
print("")
print("4-SALIR")
print("")
opc=input("Introduce una opcion: ")

if opc == '1':
    print("Analizando JS")

elif opc=='2':

    
    text = "/*hola todo esto es un c******************omentario*//*Este es un segundo comentario*/ {Csdsdsd"
            
            
    analizarcss(text)
    print("Se termino el analisis")
    print('')
    for i in listaTok:
        i.miestado()
     
    

    print("Analizando CSS")   
elif opc=='3':
    print("Analizando HTML")
elif opc=='4':
    pass  