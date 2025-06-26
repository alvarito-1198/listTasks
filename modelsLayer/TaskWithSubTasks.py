from Task import Task

class TaskWithSubTasks(Task):

    def __init__(cls, id=0, description="sin descripcion"):
         cls.__list_sub_tasks = []
