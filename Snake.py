#<<<<<<< HEAD
import turtle, random, time

#Marcador
marcador = 0
marcador_alto = 0



#Configuracion de Pantalla
def pantalla():
    tamaño_pantalla =[500, 500] #tamaño de la pantalla
    ventana = turtle.Screen() #inicializar ventana
    ventana.title('Snake Game') #nombre de la ventana
    ventana.setup(tamaño_pantalla) #configurar tamaño de ventana
    ventana.bgcolor('white')
    ventana.tracer(0)

def cabeza_serpiente():
    cabeza = turtle.Turtle()
    cabeza.speed(0)
    cabeza.shape('square')
    cabeza.color('black')
    cabeza.penup()
    cabeza.goto(0,0)
    cabeza.direccion = 'stop'

def comida():
    comida = turtle.Turtle()
    comida.speed(0)
    comida.shape('square')
    comida.color('red')
    comida.penup()
    comida.goto(0,200)



def main():
    #pantalla()
    cabeza_serpiente()
    comida()
    return

main()

#>>>>>>> 9b486889a3285bbfb68d2c5034c22f3acf8a8024
