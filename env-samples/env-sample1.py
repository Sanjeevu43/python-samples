from dotenv import load_dotenv,find_dotenv
import os

env_file = find_dotenv() # return env file
print('***********************************************************************************************************')
print("ENV FILE : ",env_file)

env = load_dotenv() # return bool
print(env)

# once .env loads then we can get env variables
NAME:str = os.getenv('NAME')
PH_NO:str = os.getenv('PH_NO')
API_KEy:str = os.getenv('API_KEy')
PASS_WORD:str = os.getenv('PASS_WORD')
print('NAME : ', NAME)
print('PH_NO : ', PH_NO)
print('API_KEy : ', API_KEy)
print('PASS_WORD : ', PASS_WORD)
