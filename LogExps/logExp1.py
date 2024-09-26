# log levels : DEBUG, INFO, WARNING, ERROR, CRITICAL

# defalut level is WARNING (it will work with log configuration)

import logging
import sys

# We can add log configuration in two ways

# option 1
'''
logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
level = 'DEBUG' if __name__ == "__main__" else 'INFO'
logger.setLevel(level)
handler.setLevel(level)

def printLogLevel():
    print(level)

printLogLevel()
logger.debug('Log level is debug') '''

lvl = logging.DEBUG if __name__ == '__main__' else logging.INFO

logging.basicConfig(level=lvl)
def printLogLevel():
    print(lvl)
    print(logging.getLevelName(lvl))

if __name__ == '__main__':
    printLogLevel()

logging.debug('Log level is debug')