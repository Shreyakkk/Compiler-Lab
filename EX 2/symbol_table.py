tokens=[' ']
ids = []
key_words = ['int','string','char','float','double']
operators = ['+','-','*','/','=','<']
punct = ['(',')', '{', '}' , '[' ,']',',']
with open("program1.txt") as t:
    a=t.readlines()
    for t in a:
        tokens=tokens + (t.split(" "))
print("id            data_types              value              rType            NoArgs               TArgs")
for pos, t in enumerate(tokens):
    for k in key_words:
        if(t==k):
            ids.append(tokens[pos + 1])
            if(tokens[pos + 2 ] == ','):
                print(tokens[pos + 1] + " " + tokens[pos] + "      " + "NULL")
                tokens.insert(pos + 3, tokens[pos])
            elif (tokens[pos + 2] =='('):
                end=tokens.index(')')
                para = tokens[pos + 3:end]
                kc=0;
                pt=[]
                for key in key_words:
                    kc = kc + para.count(key)
                    i=0
                    while(i < para.count(key)):
                        pt.append(key)
                        i = i + 1
                    print(tokens[pos + 1] + "              " + tokens[pos] + "         " + str(kc) + "          " + str(pt))
            elif (tokens[pos + 1] == '('):
                    countinue
            else:
                    print(tokens[pos + 1] + "               " + tokens[pos] + "       " + tokens[pos + 3])
