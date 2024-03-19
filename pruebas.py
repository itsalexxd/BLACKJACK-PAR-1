"""
Practica 1 - Paradigmas de Programacion
Garcí­a Lavandera, Alejandro
Garcí­a del Caz, Carla
Curso 2023-2024
"""

import externo
    
def Main():
    #elegir modo de juego
    continuar_modo=True
    
    while continuar_modo:
        ejecucion=input('¿Modo de ejecución? [J]uego [A]nálisis: ')
        ejecucion.upper()
        
        if ejecucion=='J':
            '''
            ejecutar modo juego
                (pedir apuesta)
                (iniciar bucle while que se rompe cuando la respuesta es no)
                (hacer balance)
                (mostrar todos los resultados al final)
            '''
            continuar_modo= False
            
            partida=0
            balance=0
            continuar_partida= True
            apuesta_correcta=True
            respuesta_correcta=True
            continuar_jugador=True
            continuar_croupier=True
            jugada_correcta=True
                
            while continuar_partida:
                partida=+1
                print(f'--- INICIO DE LA PARTIDA {partida}--- BALANCE {balance} € ')
                    
                while apuesta_correcta:
                    apuesta=input('¿Apuesta?')
                        
                    if apuesta==2:
                        apuesta_correcta= False
                        
                    elif apuesta==10:
                        apuesta_correcta= False
                        
                    elif apuesta==50:
                        apuesta_correcta=False
                        
                    else:
                        apuesta_correcta=True
                        
                print('REPARTO INICIAL')
                #repartir cartas
                
                
                #if valor de las cartas son iguales y solo hay dos cartas
                while jugada_correcta:
                    jugada=input('¿Jugada para mano? [P]edir [D]oblar [C]errar [S]eparar')
                    jugada.upper()
                            
                    if jugada=='P' or jugada=='D' or jugada=='C' or jugada=='S':
                        jugada_correcta==False
                        
                    else:
                        jugada_correcta==True
                            
                while continuar_jugador:
                    if jugada=='P':
                        #dar otra carta
                        #evaluar estado mano(pasada o abierta)
                        continuar_jugador=True
                        
                    elif jugada=='D':
                        apuesta=apuesta*2
                        #dar otra carta
                        #evaluar estado mano (pasada o cerrada)
                        continuar_jugador=False
                                
                    elif jugada=='C':
                        #cambiar estado de mano(cerrada)
                        continuar_jugador=False
                            
                    elif jugada=='S':
                        #crear dos manos, una con la primera carta y la otra con la segunda
                        #estado de mano abierto
                        continuar_jugador=True
                            
                while continuar_croupier:
                    '''
                    -todas las manos del jugador pasadas, no se piden cartas
                        -contar resultados
                    -caso contrario
                        -pedir hasta >= 17
                    '''
                        
                #contabilizar resultados
                    '''
                    -Ambas manos pasadas o mismo valor: ninguno obtiene beneficio
                    -croupier pasada o <jugador: el croupier paga al jugador la apuesta
                    -jugador pasada o <croupier: el jugador paga
                        
                    -resultado: suma de todas las manos
                    '''
                        
                while respuesta_correcta:
                    respuesta=input('¿Otra partida? [S/N]')
                    respuesta.upper()
                        
                    if respuesta=='S' or respuesta=='N':
                        respuesta_correcta=False
                            
                    else:
                        respuesta_correcta=True
                            
                if respuesta=='S':
                    continuar_partida=True
                        
                else:
                    print('BALANCE FINAL{}')
                    continuar_partida=False
                        
                        
                            
                
                
                
                
                
        
        elif ejecucion=='A':
            '''
            ejecutar modo analisis
                (pedir número de partidas)
                (hacer balance)
                (mostrar todos los resultados al fina)
            '''
            continuar_modo= False
                
        elif ejecucion=='':
            '''
            ejecutar modo juego
            apuesta 10
            primera accion pedir
            jugar otra partida
            '''
            continuar_modo=False
                
        else:
            continuar_modo=True
        
        
 
if __name__=='__main__':
    Main()