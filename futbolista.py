from deportista import Deportista
from persona import Persona

class Futbolista(Persona, Deportista):
    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)
    
    def getGolesMarcados(self):
        return self._golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil

    def setGolesMarcados(self, goles):
        self._golesMarcados = goles

    def setTarjetasRojas(self, rojas):
        self._tarjetasRojas = rojas

    def setPiernaHabil(self, pierna):
        self._piernaHabil = pierna

    
    def __str__(self):
        return f"Mi nombre es {Persona.getNombre} soy profesional en el deporte {Deportista.getDeporte} Tengo {Persona.getEdad} y llevo {Deportista.getAñosPracticando} años en el deporte"