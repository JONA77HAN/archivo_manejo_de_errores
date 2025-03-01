import random

class Carta:
    def __init__(self, nombre, valor, tipo):
        self.nombre = nombre
        self.valor = valor
        self.tipo = tipo
    
    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - Valor: {self.valor}"

class Mazo:
    def __init__(self):
        self.cartas = self.generar_cartas()
        random.shuffle(self.cartas)
    
    def generar_cartas(self):
        nombres = ["Dragón", "Mago", "Guerrero", "Hechicero", "Bestia"]
        tipos = ["Fuego", "Agua", "Tierra", "Aire"]
        return [Carta(random.choice(nombres), random.randint(1, 10), random.choice(tipos)) for _ in range(20)]
    
    def robar_carta(self):
        return self.cartas.pop() if self.cartas else None

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []
    
    def robar(self, mazo):
        carta = mazo.robar_carta()
        if carta:
            self.mano.append(carta)
    
    def mostrar_mano(self):
        return "\n".join(str(carta) for carta in self.mano)

# Configuración del juego
mazo = Mazo()
jugador1 = Jugador("Jugador 1")
jugador2 = Jugador("Jugador 2")

# Cada jugador roba 3 cartas
for _ in range(3):
    jugador1.robar(mazo)
    jugador2.robar(mazo)

# Mostrar las manos de los jugadores
print(f"Mano de {jugador1.nombre}:")
print(jugador1.mostrar_mano())
print("\n---\n")
print(f"Mano de {jugador2.nombre}:")
print(jugador2.mostrar_mano())
