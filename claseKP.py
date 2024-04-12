    while control_jugador:      # Bucle para llevar a cabo el turno del jugador para cada mano
        for i in range(len(jugador.manos)):     # Recorro todas las manos del jugador
            if jugador.estado_mano[i] in ["Cerrada", "PASADA"]:     # En este caso, el jugador no podra gestionar la mano en cuestion y lo mostramos por pantalla
                print(f"La mano {jugador.nombre_mano[i]} esta {jugador.estado_mano[i]} y no puede ser modificada.")
            
            else:       # En este caso la mano esta abierta y puede ser modificada
                control_accion = True      # Variable que lleva el control del bucle para las acciones del jugador y tratar los errores
                while control_accion:
                    if compara_cartas(jugador, i) == False:
                        # En caso de que no haya dos cartas con el mismo valor(Ej: 7 y 7), no se muestra la opcion para separar la mano
                        accion = input(f"¿Jugada para {jugador.nombre_mano[i]}? [P]edir [D]oblar [C]errar ")        # Pido al jugador que inserte la jugada que desea realizar
                        
                        if accion not in ["P", "p", "C", "c", "D", "d"]:        # Si la accion insertada no es valida, mostramos el error por pantalla y lo volvemos a pedir
                            print(f"Entrada no valida, por favor, inserte de nuevo la accion que desea realizar para la {jugador.nombre_mano[i]}")
                            #Optimizable 1.1
                        else
                    
                            accion = input(f"¿Jugada para {jugador.nombre_mano[i]}? [P]edir [D]oblar [C]errar [S]eparar ")        # Pido al jugador que inserte la jugada que desea realizar

                        if accion not in ["P", "p", "C", "c", "D", "d", "S", "s"]:        # Si la accion insertada no es valida, mostramos el error por pantalla y lo volvemos a pedir
                            print(f"Entrada no valida, por favor, inserte de nuevo la accion que desea realizar para la {jugador.nombre_mano[i]}")
                            #Optimizable 1.2, requiere un array con los caracteres validos en cada caso
                    
                if accion in ["P", "p"]:        # Pedimos y agregamos una carta a la mano en cuestion
                    jugador.agregar_carta_jugador(i, mazo.pop())        # i hace referencia a la mano, mazo.pop() inserta una carta del mazo
                
                elif accion in ["D", "d"]:      # Doblamos la apuesta del jugador, agregamos una carta y cambiamos el estado de la mano correspondiente
                    jugador.apuesta[i] += jugador.apuesta[i] * 2        # Doblamos la apuesta de la mano correspondiente
                    jugador.agregar_carta_jugador(i, mazo.pop())        # Agregamos una carta a la mano correspondiente
                    
                    if jugador.calcular_valor_mano(i) > 21:     # Si el valor total de la mano es valor > 21 -> PASADA
                        jugador.estado_mano[i] = "PASADA"
                        #Aqui se cambiaran cosas a futuro
                    else:       # valor < 21 -> Cerrada
                        jugador.estado_mano[i] = "Cerrada"
                        #Aqui tambien
                
                elif accion in ["C", "c"]:      # Accion insertada = "C" o "c"
                    jugador.estado_mano[i] = "Cerrada"      # Cambiamos el estado de la mano a Cerrada
                
                else    #Caso separar: S/s
                    jugador.separarMano(i, dime_carta_repetida(jugador, i))     # Separamos la mano cuando haya 2 cartas con el mismo valor (Ej: 7 y 7)
                
                
            jugador.imprime_jugador()
            #Optimizacion alta, pero falta optimizar en distinto nivel