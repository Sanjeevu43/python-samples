
_dict = {101:'Sanjeevu',102:'Bittu',103:'Bindu',104:'Lucky'}
print(max(_dict.items()))

for k,v in _dict.items():
    pass
    #print(k)
    #print(v)

message_l = ['come','to','office','to','meet']
messge_s = set(message_l)
#print(message_l)
#print(messge_s)

msg_dict = {}
for word in message_l:
    if word not in msg_dict:
        msg_dict[word]=1
    else:
        msg_dict[word]+=1
print(msg_dict)
print(max(msg_dict.items()))

for _ in range(7):
    pass

print('Range Value :', _)