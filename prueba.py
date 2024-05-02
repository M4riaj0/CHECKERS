import matplotlib.pyplot as plt

# Datos proporcionados
total_juegos = 300
ganados_jugador1 = 150
ganados_jugador2 = 100
empates = 50

# Calcular porcentajes
porcentaje_jugador1 = (ganados_jugador1 / total_juegos) * 100
porcentaje_jugador2 = (ganados_jugador2 / total_juegos) * 100
porcentaje_empates = (empates / total_juegos) * 100

# Crear la gráfica
plt.figure(figsize=(8, 6))
plt.plot([0, total_juegos], [porcentaje_empates, porcentaje_empates], color='red', label='Empate')
plt.plot([0, total_juegos], [porcentaje_jugador1, porcentaje_jugador1], color='green', label='Jugador 1 ganó')
plt.plot([0, total_juegos], [porcentaje_jugador2, porcentaje_jugador2], color='blue', label='Jugador 2 ganó')

# Etiquetas y leyenda
plt.xlabel('Número de juegos')
plt.ylabel('Resultado del juego en %')
plt.title('Gráfica de partidas ganadas y empates')
plt.legend()

# Mostrar la gráfica
plt.grid(True)
plt.show()
