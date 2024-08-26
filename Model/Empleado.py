

class Empleado:
    def __init__(self, legajo, nombre, cargo, salario):
        self.legajo = legajo
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def setAtributos(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def getLegajo(self):
        return self.legajo

    def __str__(self):
        return f"{self.legajo}---{self.nombre}---{self.cargo}---{self.salario}"

    def __repr__(self):
        return f"{self.legajo}---{self.nombre}---{self.cargo}---{self.salario}"