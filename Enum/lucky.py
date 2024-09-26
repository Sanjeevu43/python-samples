
ls = ['HIMALAYA','NILGIRI','ALASKA','ALPS']

D = {}

# res = 8%4
# print(res)

for s in ls:
    if len(s) % 4 == 0:
        D[s]=len(s)

for k,v in D.items():
    #print(k,D[k], sep='-')
    print(k,v, sep='-')

ll= [12,32,65,26,80,10]
ll.sort()
print(ll)

lll= [12,32,65,26,80,10]
lll = sorted(lll)
print(lll)


a = 3.142*(10**2)
print(a)

def find_area_of_circle(radious : float):
    area = 3.141*(radious ** 2)
    circum_fe = 2*3.141*radious

    # print(f'area of circle for {radious}: {int(area)}')
    # print(f'circum of circle for {radious}: {circum_fe}')

    return [area,circum_fe]

radious = 7
area, circum_fe =  find_area_of_circle(7)

print(f'area of circle for {radious}: {area}')
print(f'circum of circle for {radious}: {circum_fe}')

num = input("Enter number:")  #"876"

print(type(num))

for ch in num:
    print(int(ch))