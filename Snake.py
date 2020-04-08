#SNAKE GAME
import turtle, random, time

#Marcador
marcador = 0
marcador_alto = 0

#delay del movimiento del cuerpo
delay = 0.1

#Configuracion de Pantalla
ancho = 500 #tamaño de la pantalla
tamano_cuerpo = 0.5
ventana = turtle.Screen() #inicializar ventana
ventana.title('Snake Game') #nombre de la ventana
ventana.setup(ancho,ancho) #configurar tamaño de ventana
ventana.bgcolor('white')  #configurar el color de fondo
ventana.tracer(0) #replica del screen
    
#cabeza de la serpiente
cabeza = turtle.Turtle() #inicio de la tortuga
cabeza.shape('square') #forma de la cabeza
cabeza.color('black')  #color de la cabeza
cabeza.shapesize(tamano_cuerpo,tamano_cuerpo) #tamaño del cuerpo
cabeza.penup() #levantar el lapiz
cabeza.home() #home lo manda a las coordenadad (0,0)
cabeza_direccion = 'stop' 

#CINFIGURACION DE LA COMIDA
comida = turtle.Turtle()
comida.shape('square')
comida.color('red')
comida.shapesize(tamano_cuerpo,tamano_cuerpo)
comida.penup()
comida.goto(0,100)

cuerpo = [] #lista cuerpo para agregar los segmentos de la vivora

#CONFIGURACION DEL MARCADOR
marcador = turtle.Turtle()
marcador.shape('square')
marcador.color('white')
marcador.penup()
marcador.hideturtle()
marcador.goto(0,230)
marcador.write('Marcador: 0    Marcador mas alto: 0' ,align = 'center', font = ('Courier', 20, 'normal'))

#mover la serpiente
#fundiones
def mov_arriba():
    global cabeza_direccion #se necesita el global para poder modificar el valor de la variable
    if cabeza_direccion != 'abajo': #hacer que no se pueda ir a una direccion contraria y perder 
        cabeza_direccion = 'arriba' #cambiar el valor a arriba

def mov_abajo():
    global cabeza_direccion
    if cabeza_direccion != 'arriba': 
        cabeza_direccion = 'abajo' #cambiar el valor a abajo

def mov_derecha():
    global cabeza_direccion
    if cabeza_direccion != 'izquierda':
        cabeza_direccion = 'derecha' #cambiar el valor a la derecha

def mov_izquierda():
    global cabeza_direccion
    if cabeza_direccion != 'derecha':
        cabeza_direccion = 'izquierda' #cambiar el valor a la izquierda

#setear los movientos del teclado
def mover():
    if cabeza_direccion == 'arriba': 
        y = cabeza.ycor() #tomar el valor de la coordenada Y de la cabeza
        cabeza.sety(y + 20) #hacer set a la suma de 20 coordenadas para que se mueva la cabeza hacia arriba

    if cabeza_direccion == 'derecha':
        x = cabeza.xcor() #tomar el valor de la coordenada X de la cabeza
        cabeza.setx(x + 20) #hacer set a la suma de 20 coordenadas para que se mueva la cabeza hacia la derecha

    if cabeza_direccion == 'abajo':
        y = cabeza.ycor() 
        cabeza.sety(y - 20) #hacer set a la suma de 20 coordenadas para que se mueva la cabeza hacia abajo
    
    if cabeza_direccion == 'izquierda':
        x = cabeza.xcor()
        cabeza.setx(x - 20) #hacer set a la suma de 20 coordenadas para que se mueva la cabeza hacia la izquierda

#eventos del teclado o raton
ventana.listen() #empieza a escuchar los eventos
ventana.onkeypress(mov_arriba, 'Up') #se activa la funcion mov_arriva si se presiona tecla arriba
ventana.onkeypress(mov_abajo, 'Down') #se activa la funcion mov_abajo si se presiona tecla abajo
ventana.onkeypress(mov_derecha, 'Right') #se activa la funcion mov_derecha si se presiona tecla derecha
ventana.onkeypress(mov_izquierda, 'Left') #se activa la funcion mov_izquierda si se presiona tecla izquierda

#la serpiente come comida
def comer_comida():
    if cabeza.distance(comida) < 20: #si cabeza se junta con comida
        x_comida = random.randint(-235,235) #numero ramdon dede (-235,235) y lo guarda en la variable x_comida
        y_comida = random.randint(-235,235)
        comida.goto(x_comida, y_comida) #poner las coordenadas random

        #configuración de la cola o cuerpo
        cola = turtle.Turtle()
        cola.shape('square')
        cola.color('black')
        cola.shapesize(tamano_cuerpo,tamano_cuerpo)
        cola.penup()
        cuerpo.append(cola)

#agregar cola
def agregar_cuerpo():
    #colocar el ultimo valor hacia adelante
    for index in range (len(cuerpo) - 1, 0, -1): 
        x_cuerpo = cuerpo[index - 1].xcor() 
        y_cuerpo = cuerpo[index - 1].ycor() 
        cuerpo[index].goto(x_cuerpo, y_cuerpo) 
    
    #colocar el cuerpo a donde iba la cabeza
    if len(cuerpo) > 0:
        x_cabeza = cabeza.xcor() #obtener la coordenada en el eje x de la cabeza
        y_cabeza = cabeza.ycor() 
        cuerpo[0].goto(x_cabeza, y_cabeza) #colocar el cuerpo donde estaba la cabeza
    
#PASAR DE LOS BORDES
def pasar_bordes():
    global cabeza_direccion 
    if cabeza.xcor() < -235 or cabeza.xcor() > 235 or cabeza.ycor() < -235 or cabeza.ycor() > 235:
        cabeza.home() #que se vaya al origen (0,0)
        cabeza_direccion = 'stop' #que no se mueva

        #desaparecer el cuerpo o cola de la apartida anterior
        for cuerpos in cuerpo: #separar los fragmentos para poder mandarlos a otro lado
            cuerpos.goto(1000,1000) #mandalos a esa direccion esos fragmentos

        cuerpo.clear() #limpiar la lista cuerpo para empezar con la cabeza solamente 

def chocar_cuerpo():
    global cabeza_direccion 
    for cuerpos in cuerpo: #separar los segmentos de la vibora (obtener especificaciones)
        if cuerpos.distance(cabeza) < 20: #si choca la cabeza con el cuerpo entra este codigo
            cabeza.goto(0,0)
            cabeza_direccion = 'stop'

            for cuerpos in cuerpo:
                cuerpos.goto(1000,1000)

            cuerpo.clear()

while True:  #mientras se ejectuten las siguientes funciones, que siga el programa
    ventana.update() #actuallizar la pantalla
    mover() #la funcion que hace que se muevan la cabeza
    pasar_bordes() #recinicio de juego por chocar con los bordes de la mantalla
    chocar_cuerpo() #recinicio de juego por chocar con el cuerpo de la serpiente
    comer_comida() #reedirecionar la comida cuado la serpiente llegue a ella
    agregar_cuerpo() #aumentar el largo de la serpiente cuenado coma 
    time.sleep(delay) #el delay que va tener el juego para poder jugar bien :D

ventana.mainloop() #Inicia el bucle eventos. Debe ser la última declaración en un programa de gráficos de tortugas.
