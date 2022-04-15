from entidades.menu import MenuInicio, SubMenu, SubMenuMacros
from entidades.core import Core

from misc_funcs import salto, es_entero

### Flujo del programa ###
# Se definen funciones para ejecutar cada menú

core = Core()

# Menú de incio
def ejecutar_menu_inicio():
    # Se crea una instancia de MenuInicio para poder mostrar el contenido del menu
    opciones_menu_inicio = {
            '1': 'Nuevo macro',
            # Pueden estar activos o inactivos
            # Debe dirigir a un submenu con la opcion de activar alguno de los macros
            '2': 'Activar macros',
            '3': 'Desactivar macros',
            'X': 'Salir'
    }
    menu_inicio = MenuInicio(opciones = opciones_menu_inicio)

    # Se inicia un ciclo while para permanecer en el menu de inicio
    c_menu_inicio = True
    while c_menu_inicio:
        menu_inicio.mostrar_encabezado()

        # Se obtiene la opción seleccionada
        opc_menu_inicio = menu_inicio.mostrar_opciones()
        

        # Opción 1: Nuevo macro
        if opc_menu_inicio == '1':
            cerrar_programa = ejecutar_submenu_nuevo_macro()

            # Se eligió X
            if cerrar_programa:
                menu_inicio.mostrar_despedida()
                c_menu_inicio = False

            # Se eligió 0
            else:
                pass

        # Opción 2: Activar macros
        if opc_menu_inicio == '2':
            cerrar_programa = ejecutar_submenu_mostrar_macros()

            # Se eligió X
            if cerrar_programa:
                menu_inicio.mostrar_despedida()
                c_menu_inicio = False

            # Se eligió 0
            else:
                pass

        # Opción 3: Desactivar macros
        if opc_menu_inicio == '3':
            cerrar_programa = ejecutar_submenu_mostrar_macros(False)

            # Se eligió X
            if cerrar_programa:
                menu_inicio.mostrar_despedida()
                c_menu_inicio = False

            # Se eligió 0
            else:
                pass

        # Opción X: Salir del programa
        elif opc_menu_inicio == 'X':
            menu_inicio.mostrar_despedida()
            return True


def ejecutar_submenu_nuevo_macro():
    return False

def ejecutar_submenu_mostrar_macros(activar_macros = True):
    opciones_submenu = dict()
    i = 1
    for macro in core.macros.values():
        opciones_submenu[f'{i}'] = macro
        i += 1

    opciones_submenu.update({
        '0': 'Volver',
        'X': 'Salir'
    })

    submenu_mostrar_macros = SubMenuMacros(opciones = opciones_submenu, activar_macros = activar_macros)

    c_submenu_mostrar_macros = True
    while c_submenu_mostrar_macros:
        submenu_mostrar_macros.mostrar_encabezado()

        opc_submenu_mostrar_macros = submenu_mostrar_macros.mostrar_opciones()

        if es_entero(opc_submenu_mostrar_macros):
            indice = int(opc_submenu_mostrar_macros) - 1

            if indice in range(len(core.macros.items())):
                nombres_macros_ordenados = list(core.macros.keys())
                nombre_macro = nombres_macros_ordenados[indice]

                # Se activa / desactiva el macro
                core.macros[nombre_macro].activo = activar_macros

                ###

                submenu_mostrar_macros.volver()

                # Volver al submenu anterior
                pass

        # Opción 0: Volver
        if opc_submenu_mostrar_macros == '0':
            return False

        # Opción X: Salir
        elif opc_submenu_mostrar_macros == 'X':
            return True


    return False


if __name__ == '__main__':
    import keyboard

    def mifunc(evento):
        print(evento.scan_code)
        print(evento.name)

    keyboard.hook(mifunc)

    while True:
        pass