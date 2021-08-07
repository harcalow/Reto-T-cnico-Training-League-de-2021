from tkinter import *
from tkinter import messagebox

class Interfaz2():
    def __init__(self,datos):
        self.cantidad_nombres=datos[0]
        self.cantidad_de_nombres_ingresados=0
        self.nombres_ingresados=[]
        self.raiz=Tk()
        self.raiz.title("Configurar Juego")
        self.raiz.geometry("650x350")
        self.raiz.config(bg="#7E7E7E")
        self.nombre_escrito=StringVar()
        self.texto_cantidad=StringVar()
        self.miFrame=Frame(self.raiz)
        self.miFrame.config(bg="white",bd=20,relief="groove")
        Label(self.miFrame,text="Configuración del juego",fg="black",bg="white",font=("Comic Sans MS",18)).grid(row=0,column=1,padx=50,pady=10,sticky="e")
        self.texto_cantidad.set("Nombre del jugador 1")
        Label(self.miFrame,textvariable=self.texto_cantidad,fg="black",bg="white",font=("Comic Sans MS",18)).grid(row=1,column=0,padx=10,pady=10)
        Entry(self.miFrame,textvariable=self.nombre_escrito,fg="black",width=15,bg="white",font=("Comic Sans MS",18),justify="right").grid(row=1,column=1,padx=10,pady=10)
        boton=Button(self.miFrame,text="Guardar",command=lambda:self.nombres())
        boton.config(width="10",height="2",bg="gray",bd=5,cursor="hand2")
        boton.grid(row=3,column=1,padx=10,pady=10)
        self.miFrame.pack(padx=10,pady=50)
        self.raiz.mainloop()
    def nombres(self):
        if len(self.nombre_escrito.get())==0:
            messagebox.showerror("Error","No es posible guardar, debes ingreser un nombre")
        else:
            guardar=True
            for i in self.nombres_ingresados:
                if self.nombre_escrito.get()==i:
                    messagebox.showinfo("Error","No es posible El jugador ya existe")
                    guardar=False
            if guardar==True:
                self.nombres_ingresados.append(self.nombre_escrito.get())
                self.cantidad_de_nombres_ingresados+=1
                self.texto_cantidad.set("Nombre del jugador {}".format(self.cantidad_de_nombres_ingresados+1))
                self.nombre_escrito.set("")    
                if self.cantidad_de_nombres_ingresados==int(self.cantidad_nombres):
                    self.raiz.destroy()
    def datos_guardados(self):
        return self.nombres_ingresados
        