import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from analisis_whatsapp import *
from graficas_whatsapp import *

class AnalisisWhatsappGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador de Logs de Whatsapp")
        self.root.geometry("400x200")

        # Botón para seleccionar archivo
        self.boton_seleccionar = tk.Button(root, text="Seleccionar Archivo", command=self.seleccionar_archivo)
        self.boton_seleccionar.pack(pady=10)

        # Etiqueta para la lista desplegable
        self.etiqueta_usuario = tk.Label(root, text="Usuario")
        self.etiqueta_usuario.pack(pady=5)
        self.etiqueta_usuario.pack_forget()

        # Lista desplegable para usuarios
        self.lista_usuarios = ttk.Combobox(root)
        self.lista_usuarios.pack(pady=10)
        self.lista_usuarios.bind("<<ComboboxSelected>>", self.usuario_seleccionado)
        self.lista_usuarios.pack_forget()

        # Botón para generar informe
        self.boton_informe = tk.Button(root, text="Generar Informe", command=self.generar_informe)
        self.boton_informe.pack(pady=10)
        self.boton_informe.pack_forget()

        # Botón para generar nube de palabras
        self.boton_nube = tk.Button(root, text="Generar Nube de palabras", command=self.generar_nube)
        self.boton_nube.pack(pady=10)
        self.boton_nube.pack_forget()

        # Variables de instancia para almacenar datos
        self.datos_log = [] 
        self.usuarios = []

    def seleccionar_archivo(self):
        archivo = filedialog.askopenfilename(title="Seleccionar archivo de log")
        if archivo:
            self.datos_log = carga_log(archivo)
            self.usuarios = calcula_usuarios(self.datos_log)
            self.lista_usuarios['values'] = ["TODOS"] + self.usuarios

             # Mostrar lista desplegable y etiqueta
            self.etiqueta_usuario.pack()
            self.lista_usuarios.pack()
            self.boton_informe.pack()
            self.boton_nube.pack()

            messagebox.showinfo("Log cargado", f"Se han leído {len(self.datos_log)} mensajes.")
    
    def usuario_seleccionado(self, event):
        # Activar el botón de informe cuando un usuario es seleccionado
        self.boton_informe['state'] = tk.NORMAL

    def generar_informe(self):
        usuario_seleccionado = self.lista_usuarios.get()
        if usuario_seleccionado:
            if usuario_seleccionado == "TODOS":
                genera_informe(self.datos_log, titulo = "Informe completo")
            else:
                genera_informe(self.datos_log, titulo = "Informe " + usuario_seleccionado, usuario = usuario_seleccionado)

    def generar_nube(self):
        usuario_seleccionado = self.lista_usuarios.get()
        if usuario_seleccionado and usuario_seleccionado != "TODOS":
            muestra_word_cloud(self.datos_log, usuario_seleccionado)
            

# Crear ventana principal
root = tk.Tk()
app = AnalisisWhatsappGUI(root)
root.mainloop()
