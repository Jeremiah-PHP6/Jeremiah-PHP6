if __name__ == '__main__':
    import sys, os
    
    nombre_archivos = os.listdir('ascii')

    for nombre_archivo in nombre_archivos:
        nombre_ascii = nombre_archivo[:-4]
        print(nombre_ascii)

    sys.exit()

import os
from parametros import __ASCII__

class Ascii:
    def __init__(self, nombre, simbolo = '.'):
        self.nombre = nombre
        self.archivo = f'{self.nombre}.txt'
        self.simbolo = simbolo
        self.contenido = self.obtener_ascii()

    def obtener_ascii(self)-> list:
        asc = []
        with open(__ASCII__ + self.archivo) as f:
            lineas = f.readlines()
            for linea in lineas:
                asc.append(linea.rstrip())

        return asc


    def espaciar_ascii(self):
        ascii_nuevo = []
        for linea in ascii:
            linea_m = list(linea)
            if linea_m[0] == ' ':
                linea_m[0] = self.simbolo
            linea = ''.join(linea_m)
            ascii_nuevo.append(linea)
        
        self.ascii = ascii_nuevo


    @staticmethod
    def obtener_asciis() -> dict:
        '''
        Obtengo los asciis disponibles para el macro, en formato de diccionario
        {nombre_ascii => Ascii}
        '''
        asciis = dict()

        nombre_archivos = os.listdir(__ASCII__)

        for nombre_archivo in nombre_archivos:
            nombre_ascii = nombre_archivo[:-4]
            asc = Ascii(nombre_ascii)

            asciis[nombre_ascii] = asc

        return asciis