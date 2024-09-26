# Below code will work without any issue

# import __all__exp

# __all__exp.my_function1()
# __all__exp.my_function2()
# __all__exp.my_function3() 


from __all__exp import *

my_function1()
my_function2
my_function3() # NameError: name 'my_function3' is not defined. Did you mean: 'my_function1'?