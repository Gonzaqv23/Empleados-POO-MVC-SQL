import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Vista:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion Empleados")
        self.root.geometry("520x580+350+80")
        self.root.resizable(False, False)

        self.nuevo_nombre = None
        self.nuevo_cargo = None
        self.nuevo_salario = None
        self.ventana_emergente = None
        self.label_nuevo_nombre = None
        self.label_nuevo_cargo = None
        self.label_nuevo_salario = None
        self.entrada_nuevo_nombre = None
        self.entrada_nuevo_cargo = None
        self.entrada_nuevo_salario = None
        self.boton_guardar_cambios = None

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Inicio")
        self.notebook.add(self.tab2, text="Ayuda")

        self.label_nombre = tk.Label(self.tab1, text="Nombre:")
        self.label_nombre.place(x=30, y=20)
        self.nombre = tk.StringVar()
        self.entrada_nombre = tk.Entry(self.tab1, width=60, textvariable=self.nombre)
        self.entrada_nombre.place(x=90, y=20)

        self.label_cargo = tk.Label(self.tab1, text="Cargo:")
        self.label_cargo.place(x=30, y=45)
        self.cargo = tk.StringVar()
        self.entrada_cargo = tk.Entry(self.tab1, width=28, textvariable=self.cargo)
        self.entrada_cargo.place(x=90, y=45)

        self.label_salario = tk.Label(self.tab1, text="Salario:")
        self.label_salario.place(x=270, y=45)
        self.salario = tk.IntVar()
        self.entrada_salario = tk.Entry(self.tab1, textvariable=self.salario)
        self.entrada_salario.place(x=330, y=45)

        self.opcion = tk.IntVar()
        self.radioButton_crear = tk.Radiobutton(self.tab1, text="Crear Registro", value=1, variable=self.opcion, font=("Aerial", 9))
        self.radioButton_crear.place(x=20, y=100)
        self.radioButton_modificar = tk.Radiobutton(self.tab1, text="Actualizar Registro", value=2, variable=self.opcion, font=("Aerial", 9))
        self.radioButton_modificar.place(x=125, y=100)
        self.radioButton_actualizar = tk.Radiobutton(self.tab1, text="Refrescar Listado", value=3, variable=self.opcion, font=("Aerial", 9))
        self.radioButton_actualizar.place(x=255, y=100)
        self.radioButton_eliminar = tk.Radiobutton(self.tab1, text="Eliminar Registro", value=4, variable=self.opcion, font=("Aerial", 9))
        self.radioButton_eliminar.place(x=375, y=100)

        self.lista = tk.Listbox(self.tab1, width=75, height=20)
        self.lista.place(x=30, y=150)
        self.boton_confirmar = tk.Button(self.tab1, text="Confirmar", font=("Aerial", 11))
        self.boton_confirmar.place(x=210, y=500)

    def abrirVentanaModificarRegistro(self):
        self.ventana_emergente = tk.Toplevel(self.root)
        self.ventana_emergente.title("Modificar Empleado")
        self.ventana_emergente.geometry("310x270+300+210")
        self.label_nuevo_nombre = tk.Label(self.ventana_emergente, text="Nombre:")
        self.label_nuevo_nombre.pack(pady=10)
        self.nuevo_nombre = tk.StringVar()
        self.entrada_nuevo_nombre = tk.Entry(self.ventana_emergente, width=35, textvariable=self.nuevo_nombre)
        self.entrada_nuevo_nombre.pack()
        self.label_nuevo_cargo = tk.Label(self.ventana_emergente, text="Cargo:")
        self.label_nuevo_cargo.pack(pady=10)
        self.nuevo_cargo = tk.StringVar()
        self.entrada_nuevo_cargo = tk.Entry(self.ventana_emergente, width=30, textvariable=self.nuevo_cargo)
        self.entrada_nuevo_cargo.pack()
        self.label_nuevo_salario = tk.Label(self.ventana_emergente, text="Salario:")
        self.label_nuevo_salario.pack(pady=10)
        self.nuevo_salario = tk.IntVar()
        self.entrada_nuevo_salario = tk.Entry(self.ventana_emergente, textvariable=self.nuevo_salario)
        self.entrada_nuevo_salario.pack()
        self.boton_guardar_cambios = tk.Button(self.ventana_emergente, text="Guardar Cambios")
        self.boton_guardar_cambios.pack(pady=25)

    def setListaEmpleados(self, elemento):
        self.lista.insert(tk.END, elemento)

    def configurarBotonConfirmar(self, command):
        self.boton_confirmar.config(command=command)

    def configurarBotonGuardarCambios(self, command):
        self.boton_guardar_cambios.config(command=command)

    def cerrarVentanaEmergente(self):
        self.ventana_emergente.destroy()

    def getEmpleadoLista(self):
        empleado_seleccionado = self.lista.get(self.lista.curselection())
        return empleado_seleccionado

    def limpiarCampos(self):
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_cargo.delete(0, tk.END)
        self.entrada_salario.delete(0, tk.END)

    def limpiarLista(self):
        self.lista.delete(0, tk.END)

    def getNuevoEmpleado(self):
        nombre = self.entrada_nombre.get()
        cargo = self.entrada_cargo.get()
        salario = self.entrada_salario.get()
        return nombre, cargo, salario

    def getNuevosDatos(self):
        nombre = self.entrada_nuevo_nombre.get()
        cargo = self.entrada_nuevo_cargo.get()
        salario = self.entrada_nuevo_salario.get()
        return nombre, cargo, salario

    def getOpcion(self):
        opcion = self.opcion.get()
        return opcion

    def setEntradas(self, nombre, cargo, salario):
        self.nuevo_nombre.set(nombre)
        self.nuevo_cargo.set(cargo)
        self.nuevo_salario.set(int(salario))

    def mostrarErrorCamposIncompletos(self):
        self.mensaje_error_campos = tk.messagebox.showinfo("Campos Incompletos", "Por favor complete todos los datos\n"
                                                                                 " del Empleado")

    def mostrarMensajeNoEncontrado(self):
        self.mensaje_error_campos = tk.messagebox.showinfo("Empleado no encontrado", "El Empleado no se encuentra\n"
                                                                                     "en la base de datos")