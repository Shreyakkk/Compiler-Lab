w=open('one.txt','r').read()
q=g=w.splitlines()
name=[]
para=[]
func=[]
var={}
for line in g:
    if '#define' in line:
        if '(' in line:
            g=line.replace('#define','').replace(' ','').replace(';','')
            name.append(g[:g.find('(')])
            func.append(g[g.find('{')+1:g.find('}')])
            para.append(dict([(x,'') for x in g[g.find('(')+1:g.find(')')].replace(' ','').split(',')]))
        else:
            g=line.replace('#define','').replace(';','').split()
            var.update({g[0]:g[1]})
    else:
        fn=line[:line.find('(')]
        if fn in name:
            for v1,v2 in zip(para[name.index(fn)],line[line.find('(')+1:line.find(')')].replace(' ','').split(',')):
                para[name.index(fn)][v1]=v2
            for word in func[name.index(fn)]:
                if word in para[name.index(fn)]:
                    func[name.index(fn)]=func[name.index(fn)].replace(word,para[name.index(fn)][word])
for line in q:
    if '#define' in line:
        continue
    else:
        if line[:line.find('(')] in name:
            print(func[name.index(line[:line.find('(')])])
        else:
            for val in var:
                line=line.replace(val,var[var])
            print(line)
            
                    
            
                
