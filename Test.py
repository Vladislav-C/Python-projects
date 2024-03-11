n=int(input())
dest=[]
if n==1:
  t=0
  print(t)
else:
  m=int(input())
  if m==0:
    for i in range(1,n):
      dest+=['OPEN '+str(i+1),'PUT '+str(i)+' '+str(i+1),'CLOSE '+str(i+1)]
    t=len(dest)
    print(t)
    for i in range(len(dest)):
      print(dest[i])
  else:
    vloj=[]
    dest=[]
    for i in range(m):
      a=int(input())
      b=int(input())
      vloj.append(a)
      vloj.append(b)
    if (m==1) and vloj==[1,2]:
      t=0
      print(t)
    else:
      vloj.sort(reverse=True)
      for i in range(m):
        dest+=['OPEN '+str(vloj[i]),'PULL '+str(vloj[i])]
      del vloj[:m]
      for i in range(2,n+1):
        if ('OPEN '+str(i)) not in dest:
          dest+=['OPEN '+str(i)]
      for i in range(1,n):
        dest+=[ 'PUT '+str(i)+' '+str(i+1),'CLOSE '+str(i+1)]
      t=len(dest)
      print(t)
      for i in range(len(dest)):
        print(dest[i])
input()