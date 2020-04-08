#SNAKE GAME
import turtle, random, time

#Marcador
marcador = 0
marcador_alto = 0

#delay del movimiento del cuerpo
#delay = 0.1
delay = 0.1
#Configuracion de Pantalla
ancho = 500 #tamaño de la pantalla
tamano_cuerpo = 0.5
ventana = turtle.Screen() #inicializar ventana
ventana.title('Snake Game') #nombre de la ventana
ventana.setup(ancho,ancho) #configurar tamaño de ventana
ventana.bgcolor('white') 
ventana.tracer(0)
    
#cabeza de la serpiente
cabeza = turtle.Turtle() #inicio de la tortuga
cabeza.speed(0)
cabeza.shape('square') #forma de la cabeza
cabeza.color('black')  #color de la cabeza
cabeza.shapesize(tamano_cuerpo,tamano_cuerpo)
cabeza.penup() 
cabeza.home()
cabeza_direccion = 'stop'

#CINFIGURACION DE LA COMIDA
comida = turtle.Turtle()
comida.speed(0)
comida.shape('square')
comida.color('red')
comida.shapesize(tamano_cuerpo,tamano_cuerpo)
comida.penup()
comida.goto(0,100)

cuerpo = []

#CONFIGURACION DEL MARCADOR
#marcador = turtle.Turtle()
#marcador.shape()
#marcador.color('white')
#marcador.penup()
#marcador.hideturtle()
#marcador.goto(0,230)
#marcador.write('Marcador: 0    Marcador mas alto: 0 ,align = 'center', font = ('Courier', 20, 'normal'))

#mover la cabeza de la serpiente con los eventos
def mov_arriba():
    global cabeza_direccion
    if cabeza_direccion != 'abajo':
        cabeza_direccion = 'arriba'

def mov_abajo():
    global cabeza_direccion
    if cabeza_direccion != 'arriba': 
        cabeza_direccion = 'abajo'

def mov_derecha():
    global cabeza_direccion
    if cabeza_direccion != 'izquierda':
        cabeza_direccion = 'derecha'

def mov_izquierda():
    global cabeza_direccion
    if cabeza_direccion != 'derecha':
        cabeza_direccion = 'izquierda'

#setear los movientos del teclado
def mover():
    if cabeza_direccion == 'arriba':
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza_direccion == 'derecha':
        x = cabeza.xcor()
        cabeza.setx(x + 20)

    if cabeza_direccion == 'abajo':
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    
    if cabeza_direccion == 'izquierda':
        x = cabeza.xcor()
        cabeza.setx(x - 20)

#eventos del teclado o raton
ventana.listen() #empieza a escuchar los eventos
ventana.onkeypress(mov_arriba, 'Up') 
ventana.onkeypress(mov_abajo, 'Down') 
ventana.onkeypress(mov_derecha, 'Right') 
ventana.onkeypress(mov_izquierda, 'Left') 

#la serpiente come comida
def comer_comida():
    if cabeza.distance(comida) < 20:
        x_comida = random.randint(-235,235)
        y_comida = random.randint(-235,235)
        comida.goto(x_comida, y_comida)

        #configuración de la cola o cuerpo
        cola = turtle.Turtle()
        cola.speed(0)
        cola.shape('square')
        cola.color('black')
        cola.shapesize(tamano_cuerpo,tamano_cuerpo)
        cola.penup()
        cuerpo.append(cola)

#agregar cola
def agregar_cuerpo():
    for index in range (len(cuerpo) - 1, 0, -1):
        x_cuerpo = cuerpo[index - 1].xcor()
        y_cuerpo = cuerpo[index - 1].ycor()
        cuerpo[index].goto(x_cuerpo, y_cuerpo)

    if len(cuerpo) > 0:
        x_cabeza = cabeza.xcor()
        y_cabeza = cabeza.ycor()
        cuerpo[0].goto(x_cabeza, y_cabeza)
    
#PASAR DE LOS BORDES
def pasar_bordes():
    global cabeza_direccion
    if cabeza.xcor() < -235 or cabeza.xcor() > 235 or cabeza.ycor() < -235 or cabeza.ycor() > 235:
        cabeza.home()
        cabeza_direccion = 'stop'

        for cuerpos in cuerpo:
            cuerpos.goto(1000,1000)

        cuerpo.clear()

def chocar_cuerpo():
    global cabeza_direccion 
    for cuerpos in cuerpo:
        if cuerpos.distance(cabeza) < 20:
            cabeza.goto(0,0)
            #cabeza_direccion = 'stop'

            for cuerpos in cuerpo:
                cuerpos.goto(1000,1000)

            cuerpo.clear()

while True: 
    ventana.update()
    mover()
    pasar_bordes()
    chocar_cuerpo()
    comer_comida()
    agregar_cuerpo()
   
    time.sleep(delay)

ventana.mainloop()
