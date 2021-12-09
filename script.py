import os
arr = []
f = open('ip.txt', 'r')

for line in f:
  arr.append(line)
  
f.close()

fw = open('out.txt', 'w')
for i in range(len(arr)):
  response = os.system("ping " + arr[i][0:-1])
  if response == 0:
    fw.write(arr[i][0:-1] + ' is up' + '\n')
    print(arr[i][0:-1], 'is up')
  else:
    fw.write(arr[i][0:-1] + ' is down' + '\n')
    print(arr[i][0:-1], ' is down')
   
fw.close()