from dotenv import load_dotenv,find_dotenv,dotenv_values
import os

# env = find_dotenv()
# print('***********************************************************************************************************')
# print("ENV FILE : ",env)

# env_details = load_dotenv()
# print(env_details)

PH_NO:str = os.getenv('PH_NO')
print('PH_NO : ', PH_NO)

#config = dotenv_values(".env")
config = dotenv_values(find_dotenv())
print(config)

MVN_HOME:str = os.getenv('MAVEN_HOME')
print('MVN_HOME : ', MVN_HOME)
