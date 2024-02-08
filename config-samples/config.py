import configparser
from ast import literal_eval

DEFAULT_CONFIG_FILE = 'test.prop'

def infer_type(v):
    try:
        res = literal_eval(v)
    except:
        res = v
    return res

def config_load(fileName : str=None) -> dict:
    config = configparser.ConfigParser()
    if fileName is None:
        fileName = DEFAULT_CONFIG_FILE
    
    config.read('C:\\PYTHON-GIT-PROJECT\\python-samples\\config-samples\\test.properties') #C:\PythonExps\SimpleExps\ConfigExps\test.properties
    print("META : ")
    print(config.get("META","tune"))
    print(config.sections())
    '''for s in config.sections():
        print('Section: ', s)
        for k,v in config[s].items():
             print('Key: ', k)
             print('V: ', v) '''

    return {s: {k: infer_type(v) for k, v in dict(config[s]).items()} for s in config.sections()}    

config = config_load()
print("Whole Config : ",config)
keys = list(config.keys())
print("Keys : ", keys)
keys.remove('META') # after remove META key from properties file
print("Keys : ", keys)

