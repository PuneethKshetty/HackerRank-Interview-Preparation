def countingValleys(n, s):
  v=m=0
  for i in s:
    if(i == 'U'):
        m=m+1
    else:
        m=m-1
    if(i == 'U' and m == 0):
       v+=1
  return(v)
 
