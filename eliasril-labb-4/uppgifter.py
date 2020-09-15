def linsok(li, elem):
  for l in li:
    if l == elem:
      return True
  return False

def linsokkup(li):
  matches = []
  for word in li:
    term = word[2:] + word[:2]
    if linsok(li,term):
      matches.append((word, term))
  return matches

def binsok(li, x):
    lo = 0
    hi = len(li)-1
    while lo <= hi:
        mid = (lo+hi)//2
        # print(li[mid]) # Unexpected Wall of Text när denna funktion används i uppgift 6...
        if x < li[mid]:
            hi = mid - 1
        elif x > li[mid]:
            lo = mid + 1
        else:
            return True
    return False

def br_search(v, target):
  # Returns True if the sorted list v contains target and False otherwise. 
  # Undefined behaviour if v is not sorted
  return finder(v, target, 0, len(v)-1)

def finder(rows, target, low, high):
  #print(low,high,len(rows)) # Debug
  if low > high or low >= len(rows):            # Om sökgränserna korsat varandra eller om listan är slut
    return False                                # Ordet finns inte
  mid = (low + high) // 2                       # Beräkna värdet i mitten
  if rows[mid] == target:                       # Kolla om sökt ord befinner sig exakt i mitten av nuvarande sökintervall
    return True                                 # Ordet hittat
  if rows[mid] > target:                        # Om target är "mindre", dvs vi är för långt ner i listan, dela intervallet
    return finder(rows, target, low, mid-1)     # i två och upprepa processen i den "lägre" halvan.
  if rows[mid] < target:                        # Samma process om target är "större", men vi söker i den övre halvan
    return finder(rows, target, mid+1, high)    # av det delade intervallet.

def binsokkup(li):
  matches = []
  for word in li:
    term = word[2:] + word[:2]
    if binsok(li,term):
      matches.append((word,term))
  return matches

def extra1(li,algnr): # Algorithm number
  functionlist = [linsok,binsok] # 0 for lin, 1 for bin
  matches = []
  for word in li:
    term = word[2:] + word[:2]
    if functionlist[algnr](li,term):
      matches.append((word, term))
  return matches

def main():
  # Uppgift 1
  file = open("ordlista.txt")
  rows = file.readlines()
  for i in range(len(rows)):
    rows[i] = rows[i].strip()
  
  # Uppgift 2
  while True:
    elem = input("[U2] Enter an element to search (linear) for. Enter \"quit\" to exit loop: ")
    if elem == "quit":
      break
    if linsok(rows, elem):
      print(elem, "exists.")
    else:
      print(elem, "doesn't exist.")
  
  # Uppgift 3
  matches = linsokkup(rows)
  print(matches)
  print("Totalt {} matchningar".format(len(matches)))
  
  # Uppgift 4
  while True:
    elem = input("[U4] Enter an element to search (binary) for. Enter \"quit\" to exit loop: ")
    if elem == "quit":
      break
    if binsok(rows, elem):
      print(elem, "exists.")
    else:
      print(elem, "doesn't exist.")

  # Uppgift 5
  while True:
      elem = input("[U5] Enter an element to search (binary recursive) for. Enter \"quit\" to exit loop: ")
      if elem == "quit":
        break
      if br_search(rows, elem):
        print(elem, "exists.")
      else:
        print(elem, "doesn't exist.")
  
  # Uppgift 6
  matches = binsokkup(rows)
  print(matches)
  print("Totalt {} matchningar".format(len(matches)))

  # Extra 1
  matches = extra1(rows,1) # 1 for binary search, 0 for linear
  print(matches)
  print("EXTRA del 1: Totalt {} matchningar".format(len(matches)))


if __name__ == "__main__":
  main()