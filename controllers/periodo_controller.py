from classes.periodo import Periodo
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu


class Periodo_controller:
    def __init__(self):
        self.periodo = Periodo()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                ===============
                    Periodo
                ===============
                ''')
                menu = ['Listar Periodo', 'Buscar Periodo', "Nuevo Periodo", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_periodos()
                elif respuesta == 2:
                    self.buscar_periodo()
                elif respuesta == 3:
                    self.insertar_periodos()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_periodos(self):
        print('''
        =========================
            Lista de Periodos
        =========================
        ''')
        periodo = self.periodo.obtener_periodos('id_periodo')
        print(print_table(periodo, ['ID', 'Nombre periodo', 'fecha inicio', 'fecha fin']))
        input("\nPresione una tecla para continuar...")

    def buscar_periodo(self):
        print('''
        ======================
            Buscar Periodo
        ======================
        ''')
        try:
            id_periodo = input_data("Ingrese el ID del periodo >> ", "int")
            periodo = self.periodo.obtener_periodo({'id_periodo': id_periodo})
            print(print_table(periodo, ['ID', 'Nombre periodo', 'fecha inicio', 'fecha fin']))

            if periodo:
                if pregunta("¿Deseas dar mantenimiento al periodo?"):
                    opciones = ['Editar periodo', 'Eliminar periodo', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_periodo(id_periodo)
                    elif respuesta == 2:
                        self.eliminar_periodo(id_periodo)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_periodos(self):
        nombre = input_data("Ingrese el nombre del periodo >> ")
        fecha_desde = input_data("Ingrese fecha de inicio del periodo (formato DD-MM-AAAA) >> ","date")
        fecha_hasta = input_data("Ingrese fecha fin del periodo (formato DD-MM-AAAA) >> ","date")
        self.periodo.guardar_periodo({
            'nombre_periodo': nombre,
            'fecha_desde' : fecha_desde,
            'fecha_hasta' : fecha_hasta
        })
        print('''
        ==============================
            Nuevo Periodo agregado !
        ==============================
        ''')
        self.listar_periodos()

    def editar_periodo(self, id_periodo):
        nombre = input_data("Ingrese el nuevo nombre del periodo >> ")
        fecha_desde = input_data("Ingrese fecha de inicio del periodo (formato DD-MM-AAAA) >> ","date")
        fecha_hasta = input_data("Ingrese fecha fin del periodo (formato DD-MM-AAAA) >> ","date")
        self.periodo.modificar_periodo({
            'id_periodo': id_periodo
        }, {
            'nombre_periodo': nombre,
            'fecha_desde' : fecha_desde,
            'fecha_hasta' : fecha_hasta,
        })
        print('''
        ========================
            Periodo Editado !
        ========================
        ''')

    def eliminar_periodo(self, id_periodo):
        self.periodo.eliminar_periodo({
            'id_periodo': id_periodo
        })
        print('''
        ========================
            Periodo Eliminado !
        ========================
        ''')