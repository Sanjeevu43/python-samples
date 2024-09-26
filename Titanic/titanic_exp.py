import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

titanic_data = pd.read_csv('C:/Users/PenikalS/Desktop/Unisys/Python/KagleData/titanic/train.csv')
#print(titanic_data.head())
titanic_data.shape
age_mean = titanic_data['Age'].mean()
print(age_mean)
#titanic_data['Age'].fillna(titanic_data['Age'].mean(), inplace=True)
embarked = titanic_data['Embarked'].mode()[0]
print(embarked)
titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode([0]), inplace=True)
sns.countplot('',data=titanic_data)

titanic_data.replace({'Sex':{'male':0,'female':1},'Embarked':{'S':0,'C':1,'Q':2}})

