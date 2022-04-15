from parametros import __GUI__
from misc_funcs import limpiar_consola

class Gui:
    def __init__(self):
        pass
    
    @staticmethod
    def mostrar_gui(ruta_archivo, limpiar = False):
        f = open(__GUI__ + ruta_archivo, 'r', encoding = 'utf-8')
        lineas = f.readlines()

        if limpiar:
            limpiar_consola()
        
        for linea in lineas:
            linea = linea.rstrip()
            print(linea)
        
        print('\n')

        f.close()