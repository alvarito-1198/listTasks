from views_layer.Task_view import TaskView

import shutil
from os import system, name

class Menu:

    def __init__(self):
        self.task_menu = TaskView()

    def __option_menu(self):
        text = "Dime, ¿Qué opción eliges?"
        print(text)
        text = "1) ir al menú Tarea"
        print(text)
        text = "2) ir a las configuraciones "
        print(text)
        text = "3) Salir de la aplicación "
        print(text)
        text = "0) Ayuda "
        print(text)

    def show_menu(self):
        self.clear_screem()
        while True:
            self.__option_menu()
            opcion_cadena = input("Elige una opción:".center(10))
            if(opcion_cadena.isdigit() == True):
                opcion = int(opcion_cadena)
                if opcion == 1:
                    self.clear_screem()
                    self.task_menu.show_task_menu()
                elif opcion == 2:
                    pass
                elif opcion == 3:
                    break
                elif opcion >=4:
                    print("Opción incorrecta")
                elif opcion ==0:
                    pass
                   # help(self.__tarea_v)
                   # help(t)
            else:
                print("Opción incorrecta")

    def clear_screem(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
