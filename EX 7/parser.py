stack=[];st=[];ky=[]
f=open('table.txt','r').readlines()
g=f[2].split(' ')
l=0
for char in f[0].split():
    st.append(char)
for char in f[1].split():
    ky.append(char)
k=[0 for i in range(len(st))]
for i in range(len(st)):
    k[i]=[0 for j in range(len(ky))]
    for j in range(len(ky)):
        k[i][j]=g[l]
        l+=1
def disp():
    s=str(''.join(stack));v=str(''.join(x))
    print(s.ljust(10)+v.ljust(10))
stack.append('$')
stack.append(st[0])
x=input('enter the string: ')+' $'
for i in x:
    if i in ky:
        continue
    if i==' ':
        continue
    x=x.replace(i,'id')
x=x.split()
try:
    while True:
        while x[0]!=stack[-1]:
            disp()
            m=''
            m=k[st.index(stack[-1])][ky.index(x[0])]
            if m=='e':
                print(stack[-1]+'-------->'+m)
                stack.pop()
                continue
            print(stack[-1]+'----->'+m)
            stack.pop()
            if m==x[0]:
                stack.append(m)
            else:
                for j in m[::-1]:
                    stack.append(j)
        if x[0]==stack[-1]:
            disp()
            if x[0]=='$' and stack[-1]=='$':
                print('Expression accepted by Grammar...')
                break
            stack.pop()
            x.pop(0)
except:
    if(ValueError):
        print("Expression not accepted by this Grammar")
        
        
            
