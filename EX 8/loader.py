tokens=[[] for x in range(4)]

with open('ocode.txt','r') as code:
    text=code.readlines()
    pos=0
    for lines in text:
        tokens[pos]=lines.split('^')
        pos+=1

print('The name of object code : '+tokens[0][1])

for lines in tokens[1:]:
    if lines[0]=='E':
        break
    counter=str(lines[1])
    counter2=counter[-2:]
    counter3=int(counter2)
    for elems in lines[3:]:
        print(hex(counter3)[2:],elems[0:2])
        counter3+=1
        print(hex(counter3)[2:],elems[2:4])
        counter3+=1
        print(hex(counter3)[2:],elems[4:])
        counter3+=1
