while True:
    print("\nFIFA")
    print("1: Me encantaría")
    print("2: Sí")
    print("3: ¡Claro que sí!")
    print("4: NO")
    respuestaa = input("Elige una opción (1-4): ")

    if respuestaa == "1":
        print("¡Fantástico! Prepárate para una experiencia emocionante.")
        break  
    elif respuestaa == "2":
        print("¡Perfecto! Vamos a empezar el juego.")
        break  
    elif respuestaa == "3":
        print("¡Genial! ¡Esto va a ser divertido!")
        break  
    elif respuestaa == "4":
        print("La única opción es jugar >:|")
    else:
        print("ERROR: Creo que te equivocaste. Por favor, elige una opción válida.")

print("""
Eres un jugador del Hull City y estás peleando el ascenso a la Premier League contra el
Bristol City. El partido va 0:0. Si empatan o pierden, no lograrán ascender. 
Uno de tus compañeros te da un pase filtrado, te llevas a la defensa y vas solo contra el portero.

Debes meter el gol, pero necesitas calcular el impulso necesario para superar al arquero.
Le pegaste al balón con una fuerza de 2500 N durante 0.002 segundos. ¿Cuál es el impulso dado a la pelota?
""")

# Fórmula del impulso: I = F * Δt
fuerza = 2500  # Newtons
tiempo = 0.002  # segundos
impulso_correcto = fuerza * tiempo

while True:
    try:
        respuesta = float(input("¿Cuál es el impulso dado a la pelota? (en Ns): "))
        if abs(respuesta - impulso_correcto) < 0.001:  # Acepta pequeñas variaciones
            print("¡Respuesta correcta! ¡Golazo! ¡Ascendieron a la Premier League!")
            break
        else:
            print("Fallaste el gol ¡Perdiste!.")
    except ValueError:
        print("Vuelve a intentarlo.")

print("""
Es 2026. El Hull City tuvo una gran temporada. Ahora, en la Premier League, están peleando por ganar
la Premier League. El equipo va 2:1 contra el Liverpool. Si pierden el partido, el Manchester City se proclamará campeón, pero es el minuto 87.
El equipo ya está cansado y da por perdido el partido. El Liverpool se ha encerrado en su defensa. 
Aunque aún no te das por vencido, no quieres dejar ese sueño de ganar la Premier. 
Así que, sacas una actuación individual casi maradoniana. Te llevas a todo el mediocampo, haces un túnel a un defensa, 
luego te llevas a otro defensa. Estás en el punto penal, debes hacer el tiro.

Sientes cómo, antes de hacer el tiro, se para el tiempo. Le pegas al balón que pesa 0.45 kg, 
sale de tu pie a 20 m/s. Tu pie solo estuvo en contacto con el balón por 0.002 s. 
¿Qué fuerza promedio actuó sobre la pelota?
""")

# Fórmula de fuerza promedio: F = (m * v) / Δt
masa = 0.450  # kg
velocidad = 20  # m/s
tiempo = 0.002  # s
fuerza_promedio_correcta = (masa * velocidad) / tiempo

while True:
    try:
        respuesta = float(input("¿Cuál es la fuerza promedio aplicada a la pelota? (en N): "))
        if abs(respuesta - fuerza_promedio_correcta) < 0.001:  # Acepta pequeñas variaciones
            print("¡Respuesta correcta! ¡Golazo! ¡Ganaste la Premier League!")
            break
        else:
            print("Fallaste el gol ¡Perdiste!.")
    except ValueError:
        print("Vuelve a intentarlo.")
