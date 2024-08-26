from Controller.ControladorEmpleado import ControladorEmpleado
from View.Vista import Vista
import tkinter as tk


def main():
    root = tk.Tk()
    vista = Vista(root)
    controladorEmpleado = ControladorEmpleado(vista)
    controladorEmpleado.iniciar()
    root.mainloop()

if __name__ == '__main__':
    main()
