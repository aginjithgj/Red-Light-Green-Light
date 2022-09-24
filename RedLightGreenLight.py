

x = int(input())
y = int(input() or exit())


shot = 0
for i in range(x) :
    
    z = int(input() or 0)
    if z>y:
        shot+=1
print(shot)
