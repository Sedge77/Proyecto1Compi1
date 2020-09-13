from Token import *

global listaTok ##liSTA GLOBAL DE TOKENS
listaTok = list()




listaPropiedades=['color','border ','text-align','font-weight','padding-left','padding-top','line-height','margin-top','margin-left','display',
                    'top ','float ','min-width','background-color','Opacity','font-family','font-size','padding-right','padding','width','margin-right',
                    'margin','position','right','clear','max-height','background-image','background','font-style','font','padding-bottom ','display ',
                    'height ','margin-bottom','border-style','bottom ','left ','max-width','min-height ']

def analizarcss(Entrada):
    
    estado='0'
    Caracter=''
    Tipo=''
    Recorrido=''
    EntradaEvv=Entrada+'@'
    contador = 0

    ##mitoken = Token(Tipo,Caracter)
    while contador <= range(len(EntradaEvv):
        
        pass
    for i in range(len(EntradaEvv)): ##FOr para recorrer una cadena
        C=EntradaEvv[i]
           
        ##print(i) 
        if estado=='0':
            if C=='/': #Comentario
                estado='1'
                Recorrido = Recorrido+"Estado 0---->"
            elif C==' ': ##Si encuentra un espacio en blanco
                estado='0' 
            elif C=='{': ##Abre Corchete
                Tipo='SIGNO DELIMITADOR'
                
                mitoken = Token(Tipo,Caracter) ##Creando objeto comentario
                mitoken.setcaracter(C)
                mitoken.setTipo(Tipo)
                print("Estado 0---->Estado #"+C+ " ACEPTADO")
                estado='0' 
                Caracter=''
                listaTok.append(mitoken)
                
                
            elif C=='}': ##Cierra Corchete
                estado='0'     
                      
            

        elif estado=='1':
            if C=='*':
                estado='2'  
                Recorrido = Recorrido + "Estado 1---->" 
                
            

        elif estado=='2':
            if C=='*':
                estado='3' 
                Recorrido = Recorrido + "Estado 2---->"
                
            elif C!='*':
                estado='2'
                Caracter = Caracter+C
                Recorrido = Recorrido + "Estado 2---->"
                 
             

        elif estado=='3':
            if C=='/':
                estado='4' ##Aqui salta al siguiente caracter
                Recorrido = Recorrido + "Estado 3---->"
                
                i=i-1
            elif C!='/':
                estado='2' 
                Recorrido = Recorrido + "Estado 3---->"
                
            

        elif estado=='4':
            Recorrido = Recorrido + "Estado 4---->"
            Tipo='COMENTARIO'
            mitoken = Token(Tipo,Caracter) ##Creando objeto comentario
            mitoken.setcaracter(Caracter)
            mitoken.setTipo(Tipo)
            print("Se ha guardado: "+Caracter)
            print(Recorrido+Caracter+ " ACEPTADO")
            
            mitoken.miestado()
            print('')
            
            Caracter=''
            Recorrido=''
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
             
