import keyboard, time, os
from entidades.asc import Ascii
from parametros import __CSV__
from misc_funcs import es_entero

class Macro:

    def __init__(self, nombre, asc, hotkey, scancode, opcion, activo = False):
        self.nombre = nombre
        self.ascii = asc
        self.hotkey = hotkey
        self.scancode = int(scancode)
        self.opcion = opcion
        self._activo = activo

        self.valor_remover_hotkey = None
    
    @property
    def activo(self):
        return self._activo

    
    @activo.setter
    def activo(self, es_activo):
        if not self.activo and es_activo:
            self._activo = True
            self.activar_macro()
        elif self.activo and not es_activo:
            self._activo = False
            self.desactivar_macro()
        elif self.activo and es_activo:
            print('El macro ya se encuentra activo')
        elif not self.activo and not es_activo:
            print('El macro ya se encuentra inactivo')


    def all_chat(self):
        for linea in self.ascii.contenido:
            keyboard.press_and_release('shift+enter')
            time.sleep(0.05)
            keyboard.write(linea)
            time.sleep(0.05)
            keyboard.press_and_release('enter')
            time.sleep(0.05)


    def pm_chat(self, nickname):
        for linea in self.ascii.contenido:
            keyboard.press_and_release('enter')
            time.sleep(0.05)
            keyboard.write(f'/msg "{nickname}" {linea}')
            time.sleep(0.05)
            keyboard.press_and_release('enter')
            time.sleep(0.05)

    
    def activar_macro(self):
        if self.opcion == 'all chat':
            valor_remover_hotkey = keyboard.add_hotkey(self.scancode, self.all_chat)
        elif self.opcion == 'pm chat':
            valor_remover_hotkey = keyboard.add_hotkey(self.scancode, self.pm_chat)

        self.desactivar_hotkey = valor_remover_hotkey

        print('Macro activado!')


    def desactivar_macro(self):
        keyboard.remove_hotkey(self.desactivar_hotkey)
        print('Macro desctivado!')


    @staticmethod
    def obtener_macros():
        macros = dict()

        with open(__CSV__ + 'macros.csv') as f:
            lineas = f.readlines()
            
            for linea in lineas[1:]:
                nombre, nombre_asc, hotkey, scancode, opcion = linea.rstrip().split(',', 4)

                asc = Ascii(nombre_asc)

                macro = Macro(nombre, asc, hotkey, scancode, opcion)
                
                macros[nombre] = macro

        return macros