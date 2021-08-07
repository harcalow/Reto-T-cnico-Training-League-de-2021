from tkinter import *
import sqlite3
import random


class Pista():
    def dimensiones(self):
        return (1400,550)

class Jugador():          
    def dame_nombre(self,id):
        self.base_datos=sqlite3.connect("DatosDelJuego")
        self.cursor_tabla=self.base_datos.cursor()     
        self.cursor_tabla.execute("SELECT NOMBRE FROM JUGADORES WHERE ID={}".format(id))
        nombre=self.cursor_tabla.fetchone()
        return(nombre[0])    
    def puntaje_actual(self,id):
        self.base_datos=sqlite3.connect("DatosDelJuego")
        self.cursor_tabla=self.base_datos.cursor() 
        self.cursor_tabla.execute("SELECT PUNTAJE FROM JUGADORES WHERE ID={}".format(id))
        puntuacion=self.cursor_tabla.fetchone()
        return(puntuacion[0])
    def puntaje_nuevo(self,id,valor):
        self.base_datos=sqlite3.connect("DatosDelJuego")
        self.cursor_tabla=self.base_datos.cursor() 
        self.cursor_tabla.execute("UPDATE JUGADORES SET PUNTAJE={} WHERE ID={}".format(valor,id) )
        self.base_datos.commit()
    def borrar_Puntajes(self,total_jugadores):
        for i in range (1,total_jugadores+1):
            self.base_datos=sqlite3.connect("DatosDelJuego")
            self.cursor_tabla=self.base_datos.cursor()
            self.cursor_tabla.execute("UPDATE JUGADORES SET PUNTAJE=0 WHERE ID={}".format(i) )
            self.base_datos.commit()
    def victorias_anteriores(self,id):
        self.base_datos=sqlite3.connect("DatosDelJuego")
        self.cursor_tabla=self.base_datos.cursor() 
        self.cursor_tabla.execute("SELECT VICTORIAS FROM JUGADORES WHERE ID={}".format(id))
        puntuacion=self.cursor_tabla.fetchone()
        return(puntuacion[0])
    def guardar_victoria(self,victoria,id):
        self.base_datos=sqlite3.connect("DatosDelJuego")
        self.cursor_tabla=self.base_datos.cursor()
        self.cursor_tabla.execute("UPDATE JUGADORES SET VICTORIAS={} WHERE ID={}".format(victoria,id) )
        self.base_datos.commit()
        
class Carro(Jugador):
    def dame_color(self,id):
        self.base_datos=sqlite3.connect("DatosDelJuego")
        self.cursor_tabla=self.base_datos.cursor()     
        self.cursor_tabla.execute("SELECT COLOR FROM JUGADORES WHERE ID={}".format(id))
        color=self.cursor_tabla.fetchone()
        return(color[0])

class Podio(Jugador):
    def __init__(self,ganadores,cantidad_jugadores,cantidad_kilometros):
        jugador=Jugador()
        self.ganadores=ganadores
        self.cantidad_jugadores=cantidad_jugadores
        self.cantidad_kilometros=cantidad_kilometros
        self.root=Tk()
        self.root.title("Podio")
        self.root.geometry("650x350")
        self.root.config(bg="#7E7E7E")
        self.miFrame=Frame(self.root)
        self.miFrame.config(bg="white",bd=20,relief="groove")
        Label(self.miFrame,text="Primer Puesto: {}".format(jugador.dame_nombre(ganadores[0])),fg="black",bg="white",font=("Comic Sans MS",18)).grid(row=0,column=1,padx=50,pady=10)
        Label(self.miFrame,text="Segundo Puesto: {}".format(jugador.dame_nombre(ganadores[1])),fg="black",bg="white",font=("Comic Sans MS",18)).grid(row=1,column=1,padx=50,pady=10)
        Label(self.miFrame,text="Tercer Puesto: {}".format(jugador.dame_nombre(ganadores[2])),fg="black",bg="white",font=("Comic Sans MS",18)).grid(row=2,column=1,padx=50,pady=10)
        boton=Button(self.miFrame,text="Jugar de Nuevo",command=lambda:self.reinicio())
        boton.config(width="20",height="2",bg="yellow",bd=5,cursor="hand2")
        boton.grid(row=4,column=1,padx=10,pady=10)
        self.miFrame.pack(padx=10,pady=50)
        self.root.mainloop()
    def reinicio(self):
        self.root.destroy()
        self.borrar_Puntajes(int(self.cantidad_jugadores))
        acumulado_victorias=self.victorias_anteriores(int(self.ganadores[0]))
        acumulado_victorias+=1
        self.guardar_victoria(acumulado_victorias,int(self.ganadores[0]))
        nuevaInterfaz=Interfaz3(self.cantidad_jugadores,self.cantidad_kilometros)
    

class Interfaz3():
    def __init__(self,cantidad_jugadores,cantidad_kilometros):
        self.cantidad_jugadores=cantidad_jugadores
        self.cantidad_kilometros=cantidad_kilometros
        self.ganadores=[0,0,0]
        self.num_ganadores=0
        self.puntaje=0
        self.turno=1
        self.raiz=Tk()
        self.texto_cantidad=StringVar()
        self.raiz.title("Juego")
        self.raiz.geometry("1500x700")
        self.nombre(1)
        Label(self.raiz,textvariable=self.texto_cantidad,fg="black",bg="white",font=("Comic Sans MS",18)).grid(row=1,column=0,padx=10,pady=10)
        self.dado=Canvas(self.raiz,width=60,height=60,bg="black")
        self.numero(["black","black","black","black","black","black","black"])
        boton=Button(self.raiz,text="Girar",command= lambda:self.girar_dado())
        boton.config(width="10",height="2",bg="gray",bd=5,cursor="hand2")
        boton.grid(row=1,column=2,padx=5,pady=5)
        self.dibujar() 
        self.raiz.mainloop()
    def nombre(self,id):
        self.nombre_del_jugador=Jugador
        self.texto_cantidad.set("Turno del jugador {}".format(self.nombre_del_jugador.dame_nombre(self,id)))
    def girar_dado(self):
        if self.flag==False:
            self.flag=True
            self.valor_dado=random.randrange(1,7)
            if self.valor_dado==1:
                self.numero(["black","black","black","black","black","black","white"])
            elif self.valor_dado==2:
                self.numero(["black","black","white","white","black","black","black"])
            elif self.valor_dado==3:
                self.numero(["black","black","white","white","black","black","white"])            
            elif self.valor_dado==4:
                self.numero(["white","black","white","white","black","white","black"])
            elif self.valor_dado==5:
                self.numero(["white","black","white","white","black","white","white"])
            elif self.valor_dado==6:
                self.numero(["white","white","white","white","white","white","black"])
            if self.ganadores[0]!=self.turno and self.ganadores[1]!=self.turno : 
                self.puntuacion()
            self.turno_siguiente()
    def turno_siguiente(self):
        if self.turno>=int(self.cantidad_jugadores):
            self.turno=1
        else:
            self.turno+=1
        if self.ganadores[0]==self.turno or self.ganadores[1]==self.turno:
            self.turno+=1
        if self.turno>int(self.cantidad_jugadores):
            self.turno=1
        self.dibujar()
        self.nombre(self.turno)

    def numero(self,color):
        self.dado.create_oval(10,10,20,20,fill=color[0])
        self.dado.create_oval(10,25,20,35,fill=color[1])
        self.dado.create_oval(10,40,20,50,fill=color[2])
        self.dado.create_oval(40,10,50,20,fill=color[3])
        self.dado.create_oval(40,25,50,35,fill=color[4])
        self.dado.create_oval(40,40,50,50,fill=color[5])
        self.dado.create_oval(25,25,35,35,fill=color[6])
        self.dado.grid(row=1,column=1,padx=10,pady=5)
    def dibujar(self):
        self.pista()
        self.carriles()
    def pista(self):
        self.dibujarpista=Pista()
        ancho,alto=self.dibujarpista.dimensiones()
        self.framePista=Frame(self.raiz)
        self.framePista.config(width=ancho,height=alto,bg="gray")
        self.framePista.grid(row=2,column=0,padx=20,pady=10,columnspan=3)
    
    def carriles(self):
            for i in range(1,int(self.cantidad_jugadores)+1):
                self.canvas1=Canvas(self.framePista, width=1200, height=100, background="gray")
                self.posicionv=i
                self.carro(i)
    def carro(self,id):
        self.carrera=Carro()
        puntaje=self.carrera.puntaje_actual(id)
        cantidad_en_metros=int(self.cantidad_kilometros)*1000
        movimiento=puntaje*1200/cantidad_en_metros
        self.canvas1.create_rectangle(10,10,10+movimiento,90,fill=self.carrera.dame_color(id))
        self.canvas1.grid(row=self.posicionv,column=0,padx=0,pady=0)####
        self.dibujo_carro(id,movimiento)
        self.datos_carril(id)
    def dibujo_carro(self,id,movimiento):
        self.canvas1.create_rectangle(0+movimiento,50,20+movimiento,70,fill="green")
        self.canvas1.create_rectangle(0+movimiento,70,30+movimiento,90,fill="red")
        self.canvas1.create_oval(0+movimiento,85,10+movimiento,95,fill="black")        
        self.canvas1.create_oval(20+movimiento,85,30+movimiento,95,fill="black")        
    
        self.canvas1.grid(row=self.posicionv,column=0,padx=0,pady=0)###
    
    def datos_carril(self,id):
        self.canvas2=Canvas(self.framePista, width=200, height=100, background="blue")
        self.canvas2.create_text(50, 10, text=self.carrera.dame_nombre(id), fill="white", font="Arial")
        kilometros=round(float(self.carrera.puntaje_actual(id))/1000,2)
        falta_en_kilometros=round(float(self.cantidad_kilometros)-kilometros,2)
        if self.ganadores[0]==id:
            self.canvas2.create_text(55, 40, text="Primer Puesto".format(kilometros), fill="white", font="Arial")
            self.canvas2.grid(row=self.posicionv,column=1,padx=0,pady=0)
        elif self.ganadores[1]==id:
            self.canvas2.create_text(55, 40, text="Segundo Puesto".format(kilometros), fill="white", font="Arial")
            self.canvas2.grid(row=self.posicionv,column=1,padx=0,pady=0)
        else:
            self.canvas2.create_text(55, 40, text="Tienes:{} Km".format(kilometros), fill="white", font="Arial")
            self.canvas2.create_text(60, 70, text="Te faltan:{} Km".format(falta_en_kilometros), fill="white", font="Arial")  
            self.canvas2.create_text(60, 90, text="Victorias:{}".format(self.carrera.victorias_anteriores(id)), fill="white", font="Arial")  
            
            self.canvas2.grid(row=self.posicionv,column=1,padx=0,pady=0)
        self.flag=False
        self.verificar_podio()    
    def puntuacion(self):
        puntaje_actual=self.nombre_del_jugador.puntaje_actual(self,self.turno)
        total=puntaje_actual+self.valor_dado*100 #Recorrido en metros
        self.nombre_del_jugador.puntaje_nuevo(self,self.turno,total)
        self.verificar_ganador(total)
    def verificar_ganador(self,total):
        if (total/1000) >=int(self.cantidad_kilometros):
            self.ganadores[self.num_ganadores]=self.turno
            self.num_ganadores+=1
        self.verificar_podio()
    def verificar_podio(self):
        if self.num_ganadores==2 and int(self.cantidad_jugadores)==3:
            if 1 in self.ganadores and 2 in self.ganadores:
                self.ganadores[2]=3
            elif 1 in self.ganadores and 3 in self.ganadores:
                self.ganadores[2]=2
            else:
                self.ganadores[2]=1
            self.raiz.destroy()
            podio=Podio(self.ganadores,self.cantidad_jugadores,self.cantidad_kilometros)
        if self.num_ganadores==3:
            self.raiz.destroy()
            podio=Podio(self.ganadores,self.cantidad_jugadores,self.cantidad_kilometros)
        