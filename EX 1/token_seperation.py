tokens=[' ']
ids = []
key_words = ['int','string','char','float','double']
operators = ['+','-','*','/','=','<']
punct = ['(',')', '{', '}' , '[' ,']',',']
with open("program.txt") as t:
    a=t.readlines()
    for t in a:
        tokens=tokens + (t.split(" "))
print(tokens)

kw=0
op=0
pn=0
for k in key_words:
    kw=kw+tokens.count(k)
print("Key Count: " ,kw)
k=set(tokens).intersection((key_words))

for o in operators:
    op=op+tokens.count(o)
print("Operator Count: ",op)
o=set(tokens).intersection(operators)

for p in punct:
    pn=pn+tokens.count(p)
print("Punctuation Count : ",pn)
p=set(tokens).intersection((punct))

print("Keywords are : ")
for kk in k:
    print(kk)


print("\nKeywords are : ")
for oo in o:
    print(oo)

print("\nKeywords are : ")
for pp in p:
    print(pp)


