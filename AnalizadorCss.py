from Token import *

global listaTok
listaTok = list()

def analizarcss(Entrada):
    
    estado='0'
    Caracter=''
    Tipo=''
    EntradaEvv=Entrada+'@'

    ##mitoken = Token(Tipo,Caracter)
    for i in range(len(EntradaEvv)): ##FOr para recorrer una cadena
        C=EntradaEvv[i]
           
        ##print(i) 
        if estado=='0':
            if C=='/':
                estado='1'
            elif C==' ': ##Si encuentra un espacio en blanco
                estado='0' 
            elif C=='{': ##Abre Corchete
                estado='0' 
            elif C=='}': ##Cierra Corchete
                estado='0'            

        elif estado=='1':
            if C=='*':
                estado='2'   

        elif estado=='2':
            if C=='*':
                estado='3' 
            elif C!='*':
                estado='2'
                Caracter = Caracter+C
            

        elif estado=='3':
            if C=='/':
                estado='4' ##Aqui salta al siguiente caracter
                i=i-1
            elif C!='/':
                estado='2' 
                
        elif estado=='4':
            Tipo='COMENTARIO'
            mitoken = Token(Tipo,Caracter) ##Creando objeto comentario
            mitoken.setcaracter(Caracter)
            mitoken.setTipo(Tipo)
            print("Se ha guardado: "+Caracter)
            mitoken.miestado()
            
            Caracter=''
            listaTok.append(mitoken)
            
            estado='0'

        elif estado=='5':
            pass 
        elif estado=='6':
            pass 
        elif estado=='7':
            pass 
        elif estado=='8':
            pass 
        elif estado=='9':
            pass 
        elif estado=='10':
            pass 
        elif estado=='11':
            pass 
        elif estado=='12':
            pass 
        elif estado=='13':
            pass 
        elif estado=='14':
            pass 
        elif estado=='15':
            pass 
        else:
            print(i+"No es parte del lenguaje")
             
