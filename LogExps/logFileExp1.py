import logging

logging.basicConfig(filename = 'LogExps/test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

x = 50
y = 30

add_res = add(x,y)
logging.debug('Add : {} + {} = {}'.format(x,y,add_res))
sub_res = sub(x,y)
logging.debug('Sub : {} - {} = {}'.format(x,y,sub_res))

logging.debug(f'Sub :  {add_res}')