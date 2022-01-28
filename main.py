from time import sleep
from html_module import create_html_pic, create_html_planet, create_html_earth
from validador import validate
from show import show_pics
from apod import pull_photos
from planet import pull_planets
from earth import pull_earth
import data as d
import os
import sys

clear = 'cls' if sys.platform == 'win32' else 'clear'

while True:
    os.system(clear)
    opcion = input(d.MENU)
    opcion = int(validate(['0', '1', '2', '3'], opcion))

    if opcion == 1:
        #OJO: La API APOD tiende a caerse.
        os.system(clear)
        n = input(d.APOD)
        print('Estamos procesando tus preferencias...')

        id_photo = pull_photos(n)
        html = create_html_pic(id_photo)
        show_pics(html, 'apod')
        sleep(2)

    elif opcion == 2:
        os.system(clear)
        planeta = input(d.PLANETA)
        planeta = int(validate(['1', '2', '3', '4', '5', '6', '7', '8'], planeta))
        n = int(input("¿Cuántas fotos quieres ver?\n> "))
        print('Estamos procesando tus preferencias...')

        titulos, descripciones, fotos = pull_planets(planeta, n)
        html = create_html_planet(titulos, descripciones, fotos)
        show_pics(html, 'planetas')
        sleep(2)

    elif opcion == 3:
        #OJO: No todos los días tienen fotos.
        os.system(clear)
        fecha = input(d.EARTH)
        
        fotos, hora = pull_earth(fecha)
        html = create_html_earth(fotos, hora)
        show_pics(html, 'tierra')
        sleep(2)

    else:
        print('Gracias por visitarnos.')
        sleep(2)
        os.system(clear)
        exit()

