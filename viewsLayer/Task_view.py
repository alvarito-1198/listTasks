from controllerslayer.TaskController import TaskController
import keyboard


class TaskView:

    def __init__(cls):
        cls.controller = TaskController()

    def __continue(cls):
        print("Presiona la tecla Enter para continuar...")
        keyboard.wait('enter')

    def show_task_menu(cls):
        opcion = 0
        while True:
            print("""
                        Dime, ¿Qué opción eliges?
                        1) Insertar una nueva Tarea
                        2) Modificar una nueva Tarea
                        3) Eliminar una nueva Tarea
                        4) Buscar una Tarea
                        5) Listar tareas                        
                        6) Volver al menu principal
                        0) Ayuda
                    """)
            opcion = 0
            opcion_cadena = input("Elige una opción: ")
            if (opcion_cadena.isdigit() == True):
                opcion = int(opcion_cadena)
                if opcion == 1:
                   description = input("Ingresa la descripcion de la tarea: ")
                   cls.controller.add_task(description)
                   print("lista de tareas: ")
                   tasks = cls.controller.list_tasks()
                   if tasks != None and len(tasks) != 0:
                       for task in tasks.values():
                           print(task.__str__())
                   else:
                       print("no hay ninguna tarea registrada")
                   cls.__continue()
                elif opcion == 2:
                   pass
                elif opcion == 3:
                    id = int(input("Ingresa el identificador de la tarea a eliminar: "))
                    value = cls.controller.delete_task_logical(id)
                    if value == True :
                        print("La tarea fue eliminada")
                    else:
                        print("La tarea no se pudo eliminar por que no existe en la lista")
                    cls.__continue()
                elif opcion == 4:
                    id = int(input("Ingresa el identificador de la tarea a buscar: "))
                    task = cls.controller.search_task_by_id(id)
                    if task is not None:
                        print(task.__str__())
                    else:
                        print("La tarea no existe")
                    cls.__continue()
                elif opcion == 5:
                    print("lista de tareas: ")
                    tasks = cls.controller.list_tasks()
                    if tasks != None and len(tasks)!=0:
                        for task in tasks:
                            print(task.__str__())
                    else:
                        print("no hay ninguna tarea registrada")
                    cls.__continue()
                elif opcion == 6:
                    break
                elif opcion >= 7:
                    print("Opción incorrecta")
                elif opcion == 0:
                    pass
            else:
                print("Opción incorrecta")


