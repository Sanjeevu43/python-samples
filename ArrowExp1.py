
def getMsg(msg: str = 'Hai', isMsg:bool = False) -> str:
    if isinstance(isMsg, bool):        
        print(isMsg)
        return 10
    else:
        raise NameError('isMsg should be bool type')

m = getMsg('Hello', 'Bye')
print(m,end=' ')
print(m)
