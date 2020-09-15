# Viskspråket
string = input("Enter string: ")

for c in "aouåeiyäö":            # Loopa igenom och
   string = string.replace(c,"") # ta bort alla vokaler

print(string)


# Rövarspråket
string = input("Enter string: ")
out = ""

for c in string:
   if c in "bcdfghjklmnpqrstvwxyz": # Om konsonant
      out += c + "o" + c            # Lägg till 'o' och samma igen
   else:
      out += c

print(out)

# Översättning
string = input("Enter string: ")
out = ""

i = 0
while i < len(string):
   out += string[i]
   if string[i].lower() in "bcdfghjklmnpqrstvwxz": # Om konsonant
      i += 3                                       # Hoppa över de nästa två bokstäverna
      continue                                     # restart loop
   i += 1

print(out)

# Bebisspråket
string = input("Enter string: ")
words = string.split()           # Splitta upp meningen i ord
out = ""

for word in words:               # Gå igenom alla ord
   for i in range(len(word)):    # Gå igenom alla bokstäver
      if word[i] in "aouåeiyäö": # Om bokstav vokal
         res = word[:i+1]        # [:i+1] avser alla bokstäver i ordet upp till och med i
         out += res*3 + " "      # +1 för att inkludera vokalen. Lägg till tre kopior + " " i resultat
         break                   # Nästa ord

print(out)

# Allspråket
string = input("Enter string: ")
words = string.split()                    # Dela upp i ord
out = ""

for word in words:                        # Gå igenom alla ord
   for i in range(len(word)):             # Gå igenom varje bokstav
      if word[i] in "aouåeiyäö":          # Då en vokal träffas på...
         out += word[i:] + word[:i].lower() + "all "  # läggs den senare delen av ordet till först, sedan de första bokstäverna exkl. vokal till, följt av "all" och ett extra mellanslag.
         break                            # Börja jobba med nästa ord.

print(out)

# Fikon
string = input("Enter string: ")
words = string.split()
out = ""

for word in words:                        # Gå igenom alla ord
   for i in range(len(word)):             # Gå igenom varje bokstav
      if word[i] in "aouåeiyäö":          # Då den första vokalen träffas på,
         out += "fi" + word[i+1:] + word[:i+1].lower() + "kon " # "fi" läggs först till, sedan den senare delen av ordet, följt av den första delen INKL. vokal, följt av "kon" och ett mellanslag.
         break                            # Avsluta behandlingen av nuvarande ord, dvs bryt loopen och börja på nästa.

print(out)