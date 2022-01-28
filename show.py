import webbrowser
import time
import os

def show_pics(html, nombre):
    with open(f'{nombre}.html', 'w') as f:
        f.write(html)
    print('Las fotos se mostrarán en tu navegador.')
    time.sleep(2)
    webbrowser.open(f'{nombre}.html')
    time.sleep(5)
    #os.remove(f'{nombre}.html')

if __name__ == '__main__':
    from planet import pull_planets
    from html_module import create_html_planet
    titulos, descripciones, fotos = pull_planets(5,2)
    html = create_html_planet(titulos, descripciones, fotos)
    show_pics(html, 'planetas')