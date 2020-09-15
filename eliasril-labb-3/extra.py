# Viskspråket
def visk(string):
  for c in "aouåeiyäö":             # Loopa igenom och
    string = string.replace(c,"")   # ta bort alla vokaler
  return string


# Rövarspråket
def rovar(string):
  out = ""
  for c in string:
    if c.lower() in "bcdfghjklmnpqrstvwxyz": # Om konsonant
      out += c + "o" + c             # Lägg till 'o' och samma igen
    else:
      out += c
  return out

# Översättning
def translate(string):
  out = ""

  i = 0
  while i < len(string):
    out += string[i]
    if string[i].lower() in "bcdfghjklmnpqrstvwxz": # Om konsonant
      i += 3                                        # Hoppa över de nästa två bokstäverna
      continue                                      # restart loop
    i += 1
  return out

# Bebisspråket
def baby(string):
  words = string.split()           # Splitta upp meningen i ord
  out = ""

  for word in words:               # Gå igenom alla ord
    res = "" # finns möjlighet till att ta bort den här, men det är mer lättöverskådligt att inkludera den.
    for i in range(len(word)):    # Gå igenom alla bokstäver
        if word[i] in "aouåeiyäö": # Om bokstav vokal
          res = word[:i+1]        # [:i+1] avser alla bokstäver i ordet upp till och med i
          out += res*3 + " "      # +1 för att inkludera vokalen. Lägg till tre kopior + " " i resultat
          break                   # Nästa ord
  return out

# Allspråket
def alls(string):
  words = string.split()                    # Dela upp i ord
  out = ""

  for word in words:                        # Gå igenom alla ord
    for i in range(len(word)):             # Gå igenom varje bokstav
        if word[i] in "aouåeiyäö":          # Då en vokal träffas på...
          out += word[i:] + word[:i].lower() + "all "  # läggs den senare delen av ordet till först, sedan de första bokstäverna exkl. vokal till, följt av "all" och ett extra mellanslag.
          break                            # Börja jobba med nästa ord.
  return out

# Fikon
def fikon(string):
  words = string.split()
  out = ""

  for word in words:                        # Gå igenom alla ord
    for i in range(len(word)):             # Gå igenom varje bokstav
        if word[i] in "aouåeiyäö":          # Då den första vokalen träffas på,
          out += "fi" + word[i+1:] + word[:i+1].lower() + "kon " # "fi" läggs först till, sedan den senare delen av ordet, följt av den första delen INKL. vokal, följt av "kon" och ett mellanslag.
          break                            # Avsluta behandlingen av nuvarande ord, dvs bryt loopen och börja på nästa.
  return out

names = ["","Viskspråket","Rövarspråket","Översätt Rövarspråket","Bebisspråket","Allspråket","Fikonspråket"]
functions = ["",visk,rovar,translate,baby,alls,fikon]

def menu():
  print("MENY - Välj funktion")
  for i in range(1,7):
    print(i,". ",names[i],sep="")
  print("7. Avsluta")

while True:
  menu()
  choice = input()

  if choice == "7":
    print("Bye")
    exit()
  try:
    print(names[int(choice)])
  except ValueError:
    print("Expected number, got something else\n")
    continue
  
  string = input("Din mening: ")
  
  if int(choice) > 0 and int(choice) < 7:
    print(functions[int(choice)](string))
  else:
    print("You must pick a number between 1 and 6 (or 7).")
  print("\n") # Spacer
