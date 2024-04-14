# BLACKJACK-PAR-1

    2 MODOS DE EJECUCION
        - JUEGO
            1º valor apuesta -> entrada por teclado
            2º fin de partida -> volver a jugar?
            
        - ANALISIS
            1º indicar cuantas partidas va a jugar *unica entrada de teclado*
            misma salida de pantalla que en modo juego
            
    ENTRADAS DEL USUARIO:
        strings/ enter -> por defecto (modo juego, apuesta 10, accion pedir, jugar otra vez)
        string no valido -> vuelve a preguntar (no es necesario mensaje de error)
            
            
            
    - 4 palos 
    - 13 cartas por cada palo
        - total: 52 cartas en total
    - Orden de cartas: [1-10-J-Q-K]
    - As puede valer 1 u 11 en funcion de lo que más convenga para el jugador
    
    
    
    Juego:
    - Se mezclan 2 barajas -> 104 cartas en total
    - 1 vs Coupier
    - Se van sacando cartas hasta que se acaben -> nuevo mazo
    
    
    
    Mano -> conjunto de cartas que están jugando en ese momento
        (posibilidad de juar varias manos al mismo tiempo)
        (El coupier solo juega una mano SIEMPRE)
        
    Nombre de las manos -> cada mano tiene asociado un string (nombre)
        mano coupier -> "Croupier"
        Mano jugador -> "Mano" -> 'A' mano original; 'B' mano secundaria
        
    Puede tener 3 estados:
        - PASADA: mano > 21
        - ABIERTA: disponible de pedir cartas adicionales
        - CERRADA: jugador/coupier se planta
        
    Valor de una mano -> Suma de las cartas
        - Si hay un AS en la mano -> AS = 11, en caso de mano > 21 -> AS = 1
        - Si hay mas de un AS en la mano, solo 1 cuenta como 11 (2 ases de 11 = 22)
        
    CADA MANO TIENE UNA APUESTA DE DINERO
    
    Al principio de la partida, se elige el valor de la apuesta.
    Se inicia con SOLO una mano
    Valores de las apuestas:
        - BAJA: 2
        - MEDIA: 10
        - ALTA: 50
        
    Todas las cartas se reparten boca arriba (se sabe su valor INMEDIATAMENTE)
    
    Reparto inicial:
        - Coupier -> 1 carta
        - Jugador -> 2 cartas (si suman 21 -> blackjack -> fin partida -> beneficio 3/2 apuesta base)
        (solo es blackjack si se suman 21 en el reparto inicial)
        
    Si no se produce blackjack desarrollo normal de la partida
        3 fases:
            - turno jugador
                mientras mano abierta se pregunta para cada mano estas opciones
                    . pedir -> carta adicional -> recuento si > 21 -> mano estado a pasada -> sino, sigue abierta (== 21 incluido)
                    . doblar apuesta -> jugador dobla apuesta -> se añade carta si suma > 21 -> mano estado a pasada -> sino -> mano estado a cerrada ( doblar implica pedir una única carta)
                    . carrar mano -> no se añade carta -> mano estado a cerrada
                    . separar -> SOLO APARECE CUANDO -> exactamente 2 cartas del mismo valor facial -> crea nueva mano; contenido -> SOLO la segunda carta; desaparece de la mano original; ambas manos (antigua y nueva) estado abierto
            
            
            - turno croupier:
                caso 1: jugador se ha pasado en todas sus manos
                    el croupier no pide carta -> pasamos a la etapa de contabilizar resultados
                caso 2: Croupier pide cartas hasta >= 17 (no depende de las jugadas del jugador, es independiente aunq este supere su valor)
                
            
            - contabilizar resultados
                *Cada mano del jugador se compara de forma independiente con la mano del croupier*
                
                caso 1: si ambas manos estan pasadas o mismo valor -> ninguno tiene beneficio
                
                caso 2: croupier > 21 / jugador > croupier -> croupier paga apuesta de esa mano
                
                caso 3: jugador > 21 / jugador < croupier -> jugador paga al croupier la apuesta de esa mano
                
                beneficio o perdida del jugador en esa partida será la suma del resultado de todas su smanos
                
    Una vez hecho todo esto, se pregunta al jugador si desea volver a jugar 
        si. etapa 7
        no. fin del juego
        
        
        
    Criterio para pedir jugadas al jugador -> hay manos activas, se pregunta; no hay manos activas -> no se pregunta



Estructura del programa:

                      / - Juego -> Fin: no más partidas
- Pedir modo de juego |
                      \ - Analisis -> Fin: nº de partidas indicadas
                      
Partida:
    1º) Peticion apuesta
        Indicamos 
            JUEGO (nº partida, balance actual, indicar apuesta) 
            ANALISIS ()
                      
    2º) Reparto inicial
        - Repartimos: 1 carta coupier / 2 cartas jugador
        - Mostrar jugada
    
    3º) Turno jugador: bucle doble
        mientras mano activa
            peticiones correspondientes a cada mano actva
            mostrar estado manos
            
    4º) Turno coupier: bucle hasta mano >= 17
        pedir cartas y mostrar en pantalla
        
    5º) Resultados:
            mostramos estado final de las jugadas
            se desglosa cada mano (linea por mano)
            resultado de comparar la mano con la del coupier -> indicamos beneficio / perdida de la jugada
            mostrar balance total de la partida 












############################################
#### P L A N T I L L A #### C A R T A S ####
############################################

PALOS | ♠  ♥  ♦  ♣

+-----+
|  A  |
|  ♠  |
+-----+

+-----+
|  6  |
|  ♥  |
+-----+

+-----+
|  K  |
|  ♦  |
+-----+

+------+
|  5   |
|  ♣   |
+------+

+------+
|  10  |
|  ♣   |
+------+