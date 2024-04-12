
                    
                    # Agregamos una mano al jugador
                    jugador.agregar_mano()
                    
                    separaciones(2)

                    print("REPARTO INICIAL")
                    # Inserto la primera carta al croupier y al jugador
                    croupier.mano.agregar_carta(mazo.pop())
                    jugador.agregar_carta_jugador(0,mazo.pop())
                    
                    # Muestra la informacion del croupier y el jugador
                    imprimeInfo(croupier, jugador)
                    
                    # Turno del jugador
                    print("TURNO DEL JUGADOR")
                    fin_jugador = False
                    while fin_jugador == False:
                        for i in range(len(jugador.manos)): # Recorro las manos del jugador
                            if jugador.estado_mano[i] == "Activa": # Si el estado de la mano no es Activa, no se podra editar
                                if compara_cartas(jugador, i) == False: # Compruebo si se activa la funcion para separar y mostrarla
                                    jugada = input(f"¿Jugada para {jugador.nombre_mano[i]}? [P]edir [D]oblar [C]errar  ")
                                    
                                    # Pedimos carta (agregamos carta a la mano i)
                                    if jugada == "P" or jugada == "p":
                                        jugador.agregar_carta_jugador(i, mazo.pop())
                                        
                                    
                                    # Cerramos la mano i
                                    elif jugada in ["C", "c"]:
                                        jugador.estado_mano[i] = "Cerrada"
                                    
                                    # Doblamos la apuesta de la mano i, sumamos una carta y si la suma > 21 -> PASADA; sino Cerrada
                                    elif jugada in ["D", "d"]:
                                        jugador.apuesta[i] = jugador.apuesta[i] * 2 # Doblamos la apuesta
                                        jugador.agregar_carta_jugador(i, mazo.pop()) # Agregamos una carta
                                        if jugador.calcular_valor_mano(i) > 21: # Si el valor de la mano supera 21
                                            jugador.estado_mano[i] = "PASADA" # El estado pasa a ser PASADA
                                        else:
                                            jugador.estado_mano[i] = "Cerrada" # Si no, se cierra la mano
                                        
                                        
                                    
                                    # Entrada no valida
                                    else:
                                        print("Entrada no valida, inserte de nuevo la accion que desea realizar...")
                                        jugada = input(f"¿Jugada para {jugador.nombre_mano[i]}? [P]edir [D]oblar [C]errar ")
                                        
                                        
                                # La opcion separar se activa ya que tiene 2 cartas con el mismo valor
                                else:
                                    jugada = input(f"¿Jugada para {jugador.nombre_mano[i]}? [P]edir [D]oblar [C]errar [S]eparar  ")
                                    # Pedimos carta (agregamos carta a la mano i)
                                    if jugada in ["P", "p"]:
                                        jugador.agregar_carta_jugador(i, mazo.pop())
                                        
                                    
                                    # Cerramos la mano i
                                    elif jugada in ["C", "c"]:
                                        jugador.estado_mano[i] = "Cerrada"
                                    
                                    # Doblamos la apuesta de la mano i, sumamos una carta y si la suma > 21 -> PASADA; sino Cerrada
                                    elif jugada in ["D", "d"]:
                                        jugador.apuesta[i] = jugador.apuesta[i] * 2 # Doblamos la apuesta
                                        jugador.agregar_carta_jugador(i, mazo.pop()) # Agregamos una carta
                                        if jugador.calcular_valor_mano(i) > 21: # Si el valor de la mano supera 21
                                            jugador.estado_mano[i] = "PASADA" # El estado pasa a ser PASADA
                                        else:
                                            jugador.estado_mano[i] = "Cerrada" # Si no, se cierra la mano
                                            
                                    # Separamos la mano ya que tiene 2 cartas con el mismo valor
                                    elif jugada in ["S", "s"]:
                                        jugador.separarMano(i, dime_carta_repetida(jugador, i))
                                        
                                    
                                    # Enrtada no valida, la pedimos de nuevo
                                    else:
                                        print("Entrada no valida, insertela de nuevo...")
                                        jugada = input(f"¿Jugada para {jugador.nombre_mano[i]}? [P]edir [D]oblar [C]errar [S]eparar  ")
                            # En caso de que el estado de la mano no sea Activo, no se podra modificar
                            else:
                                print(f"La mano {jugador.nombre_mano[i]} esta {jugador.estado_mano[i]}.")
                                i = i + 1
                            print()
                            jugador.imprime_jugador()
                else:
                    print("Apuesta no valida, inserte la apuesta de nuevo...")
                    valorApuesta = int(input("¿Apuesta? [2] [10] [50]  "))
            except ValueError:
                print("Por favor, ingresa un valor numerico valido")
        else:
            print("Apuesta no valida, inserte la apuesta de nuevo...")
            valorApuesta = int(input("¿Apuesta? [2] [10] [50]  "))
                
        contador_partidas += 1