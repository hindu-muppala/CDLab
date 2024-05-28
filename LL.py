nT=[]
T=[]
table =[]

for i in len(nT):
    table.apppend([])
    
for j in table:
    
    for i in len(T):
        
        j.append([])
    j.append('$')
# created a matrix
d={}
n=0
for i in nT:
    
    d[i]=n
    n+=1
n=0
for j in T:
    
    d[j]=n
    n+=1
# created a dictionary of the 

# algorithm says that for every terminal in the node
# do the following things
# for every rul
# first of it to the table



for i in P:
    
    for j in P[i]:
        
        if j[0] =='':
            
            # add the follow
            
        else:
            
            s = first(j[0])
            
            # getting first
            
            if '' in s :
                
                
                s.append(follow(s))
                
            for k in s:
                
                M[i][k] = ''.join(j)
u = ['r', 't', 'l']

print(''.join(u))



