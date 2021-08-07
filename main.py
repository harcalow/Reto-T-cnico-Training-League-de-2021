import sqlite3
from interfaz_1 import *
from interfaz_2 import *
from interfaz_3 import *
class Configuracion():
    def __init__(self):
        pass
    def cantidad_jugadores_kilometros(self):
        app1=Interfaz1()
        self.nombres_de_jugadores(app1.datos_guardardos())
        self.jugadores=app1.datos_guardardos()[0]
        self.kilometros=app1.datos_guardardos()[1]
    def nombres_de_jugadores(self,datos):
        self.app=Interfaz2(datos)
        self.crear_base_de_datos()
    def cantidad_jugadores(self):
        return self.jugadores
    def cantidad_kilometros(self):
        return self.kilometros     
    def crear_base_de_datos(self):
        self.base_datos=sqlite3.connect("DatosDelJuego")
        self.cursor_tabla=self.base_datos.cursor() 
        self.cursor_tabla.execute("DROP TABLE IF EXISTS JUGADORES")
        self.cursor_tabla.execute("CREATE TABLE JUGADORES(ID INTEGER PRIMARY KEY AUTOINCREMENT,NOMBRE VARCHAR(50) UNIQUE, PUNTAJE INTEGER, VICTORIAS INTEGER,COLOR VARCHAR(7))")
        self.guardar_datos_iniciales()
    def guardar_datos_iniciales(self):
        datos=self.app.datos_guardados()
        datos_envio=[]
        for i in datos:
            datos_arreglo=[i,0,0,self.aleatorio_color()]
            datos_envio.append(datos_arreglo)
        self.cursor_tabla.executemany("INSERT INTO JUGADORES VALUES (NULL,?,?,?,?)",datos_envio)
        self.base_datos.commit()
    def aleatorio_color(self):
        posibles="0123456789ABCDF"
        numero_hex="#"
        for i in range(0,6):
            numero_hex+=posibles[random.randrange(0,14)]
        return numero_hex

class Juego(Configuracion):
    def __init__(self):
        pass
    def run(self,cantidad_jugadores,cantidad_kilometros):    
        run=Interfaz3(cantidad_jugadores,cantidad_kilometros)

def main():
    #configuracion=Configuracion()
    #configuracion.cantidad_jugadores_kilometros()
    juego=Juego()
    juego.cantidad_jugadores_kilometros()
    juego.run(juego.cantidad_jugadores(),juego.cantidad_kilometros())

if __name__=="__main__":
    main()