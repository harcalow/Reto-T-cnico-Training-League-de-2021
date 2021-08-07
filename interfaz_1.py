from tkinter import *
from tkinter import messagebox

class Interfaz1():
    def __init__(self):
        self.raiz=Tk()
        self.raiz.title("Configurar Juego")
        self.raiz.geometry("650x350")
        self.raiz.config(bg="#7E7E7E")
        self.cantidad_jugadores=StringVar()
        self.cantidad_kilometros=StringVar()
        self.miFrame=Frame(self.raiz)
        self.miFrame.config(bg="white",bd=20,relief="groove")
        Label(self.miFrame,text="Configuración del juego",fg="black",bg="white",font=("Comic Sans MS",18)).grid(row=0,column=1,padx=50,pady=10,sticky="e")
        Label(self.miFrame,text="N° de jugadores: ",fg="black",bg="white",font=("Comic Sans MS",18)).grid(row=1,column=0,padx=10,pady=10)
        Entry(self.miFrame,textvariable=self.cantidad_jugadores,fg="black",width=15,bg="white",font=("Comic Sans MS",18),justify="right").grid(row=1,column=1,padx=10,pady=10)
        Label(self.miFrame,text="Limite en Kilometros: ",fg="black",bg="white",font=("Comic Sans MS",18)).grid(row=2,column=0,padx=10,pady=10)
        Entry(self.miFrame,textvariable=self.cantidad_kilometros,fg="black",width=15,bg="white",font=("Comic Sans MS",18),justify="right").grid(row=2,column=1,padx=10)
        boton=Button(self.miFrame,text="Guardar",command= lambda:self.datos_cantidad())
        boton.config(width="10",height="2",bg="gray",bd=5,cursor="hand2")
        boton.grid(row=3,column=1,padx=10,pady=10)
        self.miFrame.pack(padx=10,pady=10)
        self.raiz.mainloop()
    def datos_cantidad(self):
        if self.cantidad_jugadores.get().isdigit() and self.cantidad_kilometros.get().isdigit():
            if int(self.cantidad_jugadores.get())>=3:
                self.raiz.destroy()
            else:
                messagebox.showinfo("Advertencia"," Para poder jugar tiene que ser 3 o mas jugadores")
        else:
            messagebox.showerror("Error"," Verifique los datos suministrados ya que no son numericos")
        

    def datos_guardardos(self):
        return self.cantidad_jugadores.get(),self.cantidad_kilometros.get()
