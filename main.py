s="madam"

string="abaab"
cnt=0
for i in  range(len(string)):
  
  ##odd
   l,r=i,i
   while l>0 and r<len(string):
     if string[l]==string[r]:
       l-=1
       r+=1
       cnt+=1
       
  ## Even
   l=i
   r=i+1
   while l>0 and r<len(string):
     if string[l]==string[r]:
       l-=1
       r+=1
       cnt+=1
print(cnt) 