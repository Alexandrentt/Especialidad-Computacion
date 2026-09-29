#class CuentaBancaria:
 #   def __init__(self, titular: str, saldo:float = 0.0): 
  #      self.titular = titular
   #     self._saldo = saldo
    #def depositar(self, monto:float):
     #   self._saldo += monto
    #def obtener_saldo(self): 
     #   return self._saldo

#class CuentaAhorro(CuentaBancaria):
 #   def __init__(self, titular: str, saldo: float, tasa: float):
 #       super().__init__(titular, saldo)
 #       self.tasa_interes = tasa
 #   def aplicar_interes(self): 
 #       interes = self.obtener_saldo() * self.tasa_interes 
 #       self.depositar(interes)
#ahorro = CuentaAhorro("Santiago", 600.00, 0.15)
#print(ahorro.obtener_saldo())
#ahorro.aplicar_interes()
#print(ahorro.obtener_saldo())







# Implementar la clase base Personaje con puntos de vida, nombre y el método recibir_dano().
# Crear la subclase Mago utilizando super() para inicializar el atributo adicional de puntos de mana.
# Agregar a la subclase el método lanzar_hechizo() que descuente mana y retorne el valor de impacto.
# Instanciar 1 objeto Mago, aplicarle daño heredado y ejecutar sus habilidades mágicas específicas.
#Convertirlo a una pequeña batalla por turnos insdtanciando un rival que herede de mago pero que agregue poder atacar aleatoria y automaticamente
class Personaje:
    def __init__(self, nombre: str, vida: int):
        if vida <= 0:
            raise ValueError("La vida inicial debe ser un número positivo.")
        self.nombre = nombre
        self.vida = vida
        self.esta_vivo = True

    def recibir_dano(self, cantidad: int) -> int:
        if cantidad < 0:
            raise ValueError("El daño recibido no puede ser negativo.")
        
        if not self.esta_vivo:
            return 0

        self.vida -= cantidad
        if self.vida <= 0:
            self.vida = 0
            self.esta_vivo = False
            
        return cantidad


class Mago(Personaje):
    def __init__(self, nombre: str, vida: int, mana: int):
        super().__init__(nombre, vida)
        if mana < 0:
            raise ValueError("El maná inicial no puede ser negativo.")
        self.mana = mana

    def lanzar_hechizo(self, costo_mana: int, potencia: int) -> int:
        if not self.esta_vivo:
            return 0

        if costo_mana < 0 or potencia < 0:
            raise ValueError("El costo y la potencia deben ser valores positivos.")

        if self.mana < costo_mana:
            return 0  # Maná insuficiente: el hechizo falla y no impacta

        self.mana -= costo_mana
        return potencia

class Caballero(Personaje):
    def __init__(self, nombre: str, vida: int):
        super().__init__(nombre, vida)
    def atacarAletorio(self, cantidad: int) -> int:
        if not self.esta_vivo:
            return 0
        daño = random.randint(1, cantidad)
        return daño



print("=== Batalla por turnos ===")
print("Ingresa el nombre de tu personaje: ")
nombre = input()
print("Ingresa el nombre de tu rival: ")
rival = input()

# --- Instanciación y Pruebas de Uso ---

# Creación de la instancia
gandalf = Mago(nombre=nombre, vida=100, mana=50)
rivalMaquina = Caballero(nombre=rival, vida=150)

# Aplicación de daño heredado
while gandalf.esta_vivo and rivalMaquina.esta_vivo:
    print(f"{gandalf.nombre} tiene {gandalf.vida} de vida")
    print(f"{rivalMaquina.nombre} tiene {rivalMaquina.vida} de vida")
    gandalf.recibir_dano(rivalMaquina.atacarAletorio(20))
    rivalMaquina.recibir_dano(gandalf.lanzar_hechizo(20, 60))

