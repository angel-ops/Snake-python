<<<<<<< HEAD
import ramdom
import pygame as pg
import math
import tkinter as tk
from tkinter import messagebox

#CARARCTERISTICAS DE LA VIBORA
class snake(object):
    def _init_(self, color, posicion):
        pass

#redibujar la pantalla 
def actualizar_pantalla(surface):
    screen.fill((0,0,0))
    drawGrids(surface)
    pg.display.update()

#CORRER EL PROGRAMA EN EL MAIN 
def main():
    rojo = (255, 0, 0)
    white = (255, 255, 255)
    screen_size = [500, 500]
    screen = pg.display.set_mode(screen_size)
    s = snake(white, (10, 10))
    flag = True    
    clock = pg.time.Clock()

    #PARA QUE CORA EL PROGRAMA
    while flag:
        pg.time.delay(50)
        clock.tick(10)
        actualizar_pantalla(screen)


#prueba lol
#segunda prueba



main()


=======
import ramdom
import pygame as pg
import math
import tkinter as tk
from tkinter import messagebox


#CARARCTERISTICAS DE LA VIBORA
class snake(object):
    def _init_(self, color, posicion):
        pass

#redibujar la pantalla 
def actualizar_pantalla(surface):
    screen.fill((0,0,0))
    drawGrids(surface)
    pg.display.update()

#CORRER EL PROGRAMA EN EL MAIN 
def main():
    rojo = (255, 0, 0)
    white = (255, 255, 255)
    screen_size = [500, 500]
    screen = pg.display.set_mode(screen_size)
    s = snake(white, (10, 10))
    flag = True    
    clock = pg.time.Clock()

    while flag:
        pg.time.delay(50)
        clock.tick(10)
        actualizar_pantalla(screen)



main()


>>>>>>> 9b486889a3285bbfb68d2c5034c22f3acf8a8024
