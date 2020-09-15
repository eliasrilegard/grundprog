'''Om man upprepar en perfekt riffelblandning av 
   en vanlig kortlek med 52 kort ett antal gånger
   så kommer man att återfå den ursprungliga
   ordningen mellan korten.
   Hur många gånger behövs?'''

cards = 52 # Jämt antal

def shuffle(arr):
  arr1 = arr[:cards//2]         # Split the array in two
  arr2 = arr[cards//2:]
  res = []                # Create a result array to store in
  for i in range(cards//2):
    res.append(arr1[i])   # Add one from each every iteration
    res.append(arr2[i])
  return res


arr = []
for i in range(1,cards +1):  # Fill with numbers
  arr.append(i)
ref = arr

arr = shuffle(arr)        # First shuffle manually
c = 1                     # Keep count

while arr != ref:         # Until array is back to normal
  arr = shuffle(arr)
  c += 1
  #print(arr)

print("{} iterations to return to original.".format(c))