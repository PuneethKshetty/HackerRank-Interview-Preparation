def SockMerchant(n,arr):
  pairs = 0
  for i in set(arr):
      pairs = pairs + arr.count(i)//2   
  return (pairs)
  
  Explaination :
  Here what i have done is I have initialised pair to be zero and i have used for loop for iterating through set(arr), Now what set(arr) does is it removes the duplicates in an array
  For Ex :
     No of socks is : 7
     Think we have color of each stock as i.e arr : 10 20 30 50 20 30 10
     Here set(arr) removes the duplicates an we have as arr:  10 20 30 50
     Through my for loop iteration takes place and what count does is it counts the no of occurrences hence from the examples it will check 10 is been repeated 2 times and // will consider only the whole numbers
     hence count is divided by 2 which leaves 1 as a pair and hence pair is updated to 1 .
     Hence 1 pair of color of stocks of (10) is present.
