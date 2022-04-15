from entidades.asc import Ascii
from entidades.macro import Macro

class Core:
    def __init__(self):
        self.asciis = Ascii.obtener_asciis()
        self.macros = Macro.obtener_macros()

    def anadir_macro(self, macro):
        if macro.nombre not in self.macros.keys():
            self.macros[macro.nombre] = macro

            print('Macro añadido exitosamente')
            return True
        else:
            print('Nombre del macro ya existente')
            return False