from Model.Empleado import Empleado
import sqlite3 as sql
import random

class ControladorEmpleado:
    def __init__(self, vista):
        self.vista = vista
        self.lista_empleados = []
        self.vista.configurarBotonConfirmar(self.elegirOpcion)

    def elegirOpcion(self):
        opcion = self.vista.getOpcion()
        if opcion == 1:
            self.crearNuevoEmpleado()
        elif opcion == 2:
            self.actualizarEmpleado()
        elif opcion == 3:
            self.verEmpleados()
        elif opcion == 4:
            self.eliminarEmpleado()

    def buscarEmpleado(self, legajo):
        for emp in self.lista_empleados:
            if int(emp.getLegajo()) == int(legajo):
                return emp

    def eliminarEmpleadoLista(self, legajo):
        for emp in self.lista_empleados:
            if int(emp.getLegajo()) == int(legajo):
                self.lista_empleados.remove(emp)
                break

    def cargarEmpleados(self):
        db_file = "empleados.db"
        conn = sql.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM empleados")
        resultados = cursor.fetchall()
        conn.close()
        for registro in resultados:
            legajo, nombre, cargo, salario = registro
            nuevo_empleado = Empleado(legajo, nombre, cargo, salario)
            self.lista_empleados.append(nuevo_empleado)

    def crearNuevoEmpleado(self):
        legajo = random.randint(15500, 18500)
        nombre, cargo, salario = self.vista.getNuevoEmpleado()
        if nombre and cargo and salario:
            db_file = "empleados.db"
            conn = sql.connect(db_file)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO empleados (legajo, nombre, cargo, salario)"
                           "VALUES (?, ?, ?, ?)",
                           (legajo, nombre, cargo, salario))
            conn.commit()
            conn.close()
            nuevo_empleado = Empleado(legajo, nombre, cargo, salario)
            self.lista_empleados.append(nuevo_empleado)
            self.vista.limpiarCampos()
        else:
            self.vista.mostrarErrorCamposIncompletos()

    def verEmpleados(self):
        self.vista.limpiarLista()
        for empleado in self.lista_empleados:
            self.vista.setListaEmpleados(empleado)

    def getEmpleadoSeleccionado(self):
        datos = self.vista.getEmpleadoLista().split("-")
        empleado_seleccionado = datos[0]
        return empleado_seleccionado

    def actualizarEmpleado(self):
        self.vista.abrirVentanaModificarRegistro()
        legajo, nombre, cargo, salario = self.extraerDatosEmpleado()
        self.vista.setEntradas(nombre, cargo, salario)
        self.vista.configurarBotonGuardarCambios(self.guardarCambios)


    def actualizarEmpleadoExistente(self, legajo, nombre, cargo, salario):
        empleado = self.buscarEmpleado(legajo)
        empleado.setAtributos(nombre, cargo, salario)

    def guardarCambios(self):
        legajo, a, b, c = self.extraerDatosEmpleado()
        nombre, cargo, salario = self.vista.getNuevosDatos()
        if nombre and cargo and salario:
            db_file = "empleados.db"
            conn = sql.connect(db_file)
            cursor = conn.cursor()
            cursor.execute("UPDATE empleados SET nombre=?, cargo=?, salario=? WHERE legajo=?",
                           (nombre, cargo, salario, legajo))
            conn.commit()
            conn.close()
            self.actualizarEmpleadoExistente(legajo, nombre, cargo, salario)
            self.vista.cerrarVentanaEmergente()
        else:
            self.vista.mostrarErrorCamposIncompletos()


    def eliminarEmpleado(self):
        legajo_empleado = self.getEmpleadoSeleccionado()
        if legajo_empleado:
            self.eliminarEmpleadoLista(legajo_empleado)
            db_file = "empleados.db"
            conn = sql.connect(db_file)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM empleados WHERE legajo=?", (legajo_empleado,))
            conn.commit()
            conn.close()
        else:
            self.vista.mostrarMensajeNoEncontrado()

    def extraerDatosEmpleado(self):
        datos = self.vista.getEmpleadoLista().split("-")
        datos_extraidos = []
        for dato in datos:
            if dato:
                datos_extraidos.append(dato)
        return datos_extraidos

    def iniciar(self):
        self.cargarEmpleados()