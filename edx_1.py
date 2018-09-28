# Paste your code into this box
# **Correct the code to support all possibilities**
s = 'bgeuloekdeuhdcp'
count = 1                             #  0 1 2 3 4 5 6 7
d = 0                                  # h g f e d c b a
index = 0
for i in range(len(s)-1):
  for j in range(i+1,len(s)):
    if s[j] >= s[j-1]:
      count += 1  # count = 4  j = 17
    else:
      break
  if d<count:    # d = 3
    d = count    # d = 4
    index = j-count   # index = 17 - 4 = 2
  count = 0  
    
print(d)
print(index)
if index==0:
  print('Longest substring in alphabetical order is: %s' % s[index:index+d])
else:
  print('Longest substring in alphabetical order is: %s' % s[index-1:index+d])
    
