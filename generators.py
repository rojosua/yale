b=8589934609 
#m=8589934621
m=10007

list=[]
orig=[]
dados=[]

for i in range(3000,12999):
   r=pow(b,i,m)
   r=r % 10000
   list.append(r)
   orig.append(i)
   dados.append([i,r])
   
list.sort()
j=0   
q=0   


for i in range(1,9999):
   if list[i]!=list[i-1]:
      q=q+1
   if list[i]==list[i-1]:
      j= j+1
 
print(q)     
print(j)     
 
#print(*dados)
print(*list)