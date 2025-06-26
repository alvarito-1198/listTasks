import logging

logger = logging.getLogger()
# logging set up
logging.basicConfig(filename='tasks_list_error.log', encoding='utf-8', level=logging.INFO)
log_format = logging.Formatter('%(asctime)-15s %(levelname)-2s %(message)s')
# sh = logging.StreamHandler()
# sh.setFormatter(log_format)
# # add the handler
# logger.addHandler(sh)
#logger.setLevel(logging.INFO)

def loggin_run(kind, error):
    # debug = 1, info = 2, warning = 3, error = 4>=
    if kind == 1 :
        logging.basicConfig(filename='tasks_list_error.log', encoding='utf-8', level=logging.DEBUG)
        logger.debug(error)
    elif kind == 2:
        logging.basicConfig(filename='tasks_list_error.log', encoding='utf-8', level=logging.INFO)
        logger.info(error)
    elif kind == 3:
        logging.basicConfig(filename='tasks_list_error.log', encoding='utf-8', level=logging.WARNING)
        logger.warning(error)
    else:
        logging.basicConfig(filename='tasks_list_error.log', encoding='utf-8', level=logging.ERROR)
        logger.error(error)



if __name__ == '__main__':
    loggin_run(1,"Inicio")
