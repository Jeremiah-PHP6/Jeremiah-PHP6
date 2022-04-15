from abc import ABC
from misc_funcs import salto
from parametros import SALUDO, DESPEDIDA, SEPARADOR, SEPARADOR_LARGO
from gui.gui import Gui
from tabulate import tabulate

### Clase Menu ###
class Menu(ABC):
    # Constructor de la clase
    def __init__(self, opciones = dict(), encabezado = ''):
        # Se declara el atributo opciones
        self._opciones = opciones
        self.encabezado = encabezado

    @property
    def opciones(self):
        return self._opciones

    # Valida la opción ingresada en el input
    # Retorna un int con la opción (re)ingresada
    def validar_opcion(self)-> str:
        # Se obtiene un valor numérico del input
        
        opcion_invalida = True
        # Se crea un ciclo para validar la opcion
        while opcion_invalida:
            # Se obtiene la opcion del input
            opcion = input('Elige una de las opciones: ').upper()

            # Si la opción no está en la lista de opciones disponibles, se mantiene el ciclo
            if opcion not in self.opciones.keys():
                print('Opción ingresada inválida')
            # En otro caso, la opción es válida, se sale del ciclo
            else:
                opcion_invalida = False
        
        # Retorna la opción validada
        return opcion

    # Muestra las opciones disponibles
    # Retorna un int con la opción elegida en el input
    def mostrar_opciones(self)-> str:
        salto()
        print('Estas son las opciones:')

        # Secuencia que numera las opciones
        for llave, opcion in self.opciones.items():
            print(f'\t[{llave}]: {opcion.capitalize()}')

        
        
        # Se valida la opcion ingresada
        opcion = self.validar_opcion()
        # Se retorna la opcion elegida
        return opcion

    # Vuelve al menú anterior
    def volver(self):
        # Presionar enter para volver
        input('Presione enter para volver al menú anterior...')
        # Salto de linea
        salto()


    def mostrar_encabezado(self):
        salto()
        print(f'{SEPARADOR} {self.encabezado} {SEPARADOR}')
        print(SEPARADOR_LARGO)




### Clase Menu Inicio ###
class MenuInicio(Menu):
    # Constructor de la clase
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.encabezado = 'Menu de Inicio'

    # Muestra la bienvenida al menú de inicio
    def mostrar_encabezado(self):
        salto()
        # Se usa la clase Gui para manejar la interfaz gráfica
        # Se limpia la consola sólo si es primera vez que se accede al menu
        Gui.mostrar_gui('inicio.txt')
        # Muestra el mensaje de saludo
        print(SALUDO)

        super().mostrar_encabezado()

    # Muestra la despedida del programa
    def mostrar_despedida(self):
        print(DESPEDIDA)


### Clase Menu Principal ###
class MenuPrincipal(Menu):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.encabezado = 'Menu Principal'

    
    def mostrar_encabezado(self):
        salto()
        # Se usa la clase Gui para manejar la interfaz gráfica
        # Se limpia la consola sólo si es primera vez que se accede al menu
        Gui.mostrar_gui('principal.txt')
        super().mostrar_encabezado()


# Clase SubMenu ###
class SubMenu(Menu):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def mostrar_encabezado(self):
        salto()
        print(f'{SEPARADOR} {self.encabezado} {SEPARADOR}')
        print(SEPARADOR_LARGO)



# Clase SubMenu Macros ###
class SubMenuMacros(SubMenu):
    def __init__(self, activar_macros, **kwargs):
        super().__init__(**kwargs)
        
        self.encabezado = 'Activar macros' if activar_macros else 'Desactivar macros'


    def mostrar_opciones(self)-> str:
        print('Estas son las opciones:')
        salto()

        lista_opciones = [['N°', 'Nombre', 'Hotkey', 'Tipo', 'Ascii', 'Estado']]
        otras_opciones = ''

        for llave, opcion in self.opciones.items():
            if llave.isnumeric() and int(llave) > 0:
                activo = 'Activo' if opcion.activo else 'Inactivo'

                lista_macro = [f'[{int(llave)}]', opcion.nombre, opcion.hotkey, opcion.opcion, opcion.ascii.nombre, activo]
                lista_opciones.append(lista_macro)

            else:
                otras_opciones += f'[{llave}]: {opcion.capitalize()}\n'

        print(tabulate(lista_opciones, headers = 'firstrow'))
        salto()
        print(otras_opciones)
        
        
        # Se valida la opcion ingresada
        opcion = self.validar_opcion()
        # Se retorna la opcion elegida
        return opcion