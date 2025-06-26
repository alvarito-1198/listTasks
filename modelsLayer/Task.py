import datetime
from helpers.Enum_state import Enum_state
from helpers.Enum_is_deleted import Enum_is_delete


class Task:

    def __init__(cls, id=0, description="sin descripcion"):
        cls.__id = id
        cls.__description = description
        cls.__state= Enum_state.PENDIENTE # terminado, en proceso, pendiente
        cls.__is_delete = Enum_is_delete.FALSE
        cls.__date_create = datetime.datetime.now()
        cls.__date_update = datetime.date(1900,1,1)
        cls.__date_delete = datetime.date(1900,1,1)

    @property
    def id(cls):
        return  cls.__id

    @id.setter
    def id(cls, id):
        cls.__id = id

    @property
    def description(cls):
        return cls.__description

    @description.setter
    def description(cls, description="sin descripcion"):
        cls.__description = description

    @property
    def state (cls):
        return cls.__state

    @state.setter
    def state (cls, value=Enum_state.PENDIENTE):
        cls.__state = value

    @property
    def is_delete(cls):
        return cls.__is_delete

    @is_delete.setter
    def is_delete(cls, value=False):
        value_enum = Enum_is_delete.FALSE
        if(value == True):
            value_enum = Enum_is_delete.TRUE
        cls.__is_delete = value_enum

    @property
    def date_create(cls):
        return cls.__date_create

    @date_create.setter
    def date_create(cls, value):
        cls.__date_create = value

    @property
    def date_update(cls):
        return cls.__date_update

    @date_update.setter
    def date_update(cls, value):
        cls.__date_update = value

    @property
    def date_delete(cls):
        return cls.__date_delete

    @date_delete.setter
    def date_delete(cls, value):
        cls.__date_delete = value

    # def __str__(cls):
    #     #cadena = "la tarea es identificador = {i}".format( i = self.__id)
    #     cadena = (f"la tarea es: identificador = {cls.__id}, descripcion = {cls.__description}, "
    #               f"estado = {cls.__state}, borrado = {cls.__is_delete.name}, "
    #               f"fecha creacion = {cls.__date_create}, fechaactualizacion = {cls.__date_update}, "
    #               f"fecha eliminacion = {cls.__date_delete}")
    #     return cadena

    # equals para saber si dos objetos tarea son el mismo
    def __eq__(cls, task):
        value = False
        if (cls.__id == task.id):
            value = True
        return value

