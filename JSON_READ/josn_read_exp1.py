import json
import pandas as pd

f = open('C:/Users/PenikalS/Desktop/RaFTS/LaC_Viewer/sample_rule.json', "r", encoding="utf-8")

# returns JSON object as 
# a dictionary
data = json.load(f)
#print(data)
rule = data['rule']
#print('rule type :', type(rule))
rules = rule.get('rules')
#print('rules :', type(rules))
#print(rules)
#print(rules[0])
#print(len(rules))

rule_info={}
condition_info={}
 
for eachEleemt in rules:    
    rule_name=eachEleemt.get('name')    
    print(rule_name)
    rule_score=eachEleemt.get('score')
    print(rule_score)
    rule_operator=eachEleemt.get('operator')
    print(rule_operator)
    conditions = eachEleemt.get('conditions')
    rule_info['rule_name'] = rule_name
    rule_info['rule_score'] = rule_name
    rule_info['rule_operator'] = rule_name
    for eachCondition in conditions:
        entity_name = eachCondition.get('entity').get('value')
        print(entity_name)

        comparisonEntity = eachCondition.get('comparisonEntity').get('value')
        print(comparisonEntity)

        condition = eachCondition.get('condition').get('value')
        print(condition)        

        field = eachCondition.get('field').get('value')
        print(field)
        condition_info['entity_name'] = entity_name
        condition_info['comparisonEntity'] = comparisonEntity
        condition_info['condition'] = condition
        condition_info['field'] = field
    
print(rule_info) 
print(condition_info)









       
        





  
# Iterating through the json
# list
for i in data['rule']:
    pass

     


        
        

# df_records = pd.read_json(data, orient='table')
# print(df_records)
  
# Closing file
f.close()