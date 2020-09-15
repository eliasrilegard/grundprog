from tkinter import *         # * = allt
size = 400                    # Storlek på fönstret

class point:                  # Klass för att behandla två värden som en punkt med koordinater
	def __init__(self, x, y):  
		self.x, self.y = x, y   

def rect(img, TL, BR, color):
   for x in range(size):
      for y in range(size):
         if x < BR.x and x > TL.x and y < BR.y and y > TL.y:   # If pixel is in interval
            img.put(color, (x,y))                              # Color pixel white

def frame(img, TL, BR, w, colFrame, colCenter):                # Förutsätter jämn ram. Går att tweaka till att ta varje koordinat för sig, men vi tycker det här är snyggare :)
   rect(img, TL, BR, colFrame)
   innerTL = point(TL.x + w, TL.y + w)
   innerBR = point(BR.x - w, BR.y - w)
   rect(img, innerTL, innerBR, colCenter)

def triArea(p1,p2,p3):
   return abs(p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y)) / 2  # Not our work

def triangle(img, p1, p2, p3, color):
   for x in range(size):
      for y in range(size):
         p0 = point(x,y)
         a1 = triArea(p0,p2,p3)
         a2 = triArea(p1,p0,p3)
         a3 = triArea(p1,p2,p0)

         if triArea(p1,p2,p3) == a1+a2+a3:                                             # If current point is inside defined triangle
            img.put(color, (x,y))

def circle(img, origin, radius, color):
   for x in range(size):
      for y in range(size):
         if ((x - origin.x)**2 + (y - origin.y)**2 <= radius**2):
            img.put(color, (x,y))


# Main
window = Tk()
canvas = Canvas(window, width=size, height=size, bg="#000000")
canvas.pack()
img = PhotoImage(width = size, height = size)
canvas.create_image((size/2, size/2), image=img, state="normal")

while True:
	print("What would you like to draw?")
	print("1. Rectangle")
	print("2. Frame")
	print("3. Triangle")
	print("4. Circle")
	print("5. A picture")
	print("6. Exit")
	choice = int(input("Choose a number between 1 and 6: "))

	if choice == 1:
		rect(img, point(50,200), point(300,400), "#ffffff")
	elif choice == 2:
		frame(img, point(190,250), point(260,325), 8, "#000000", "#ff0000")
	elif choice == 3:
		triangle(img, point(50,200), point(300,200), point(175,100), "#ff642b")
	elif choice == 4:
		circle(img, point(390,10), 75, "#ffff00")
	elif choice == 5:
		rect(img, point(50,200), point(300,400), "#ffffff")
		frame(img, point(190,250), point(260,325), 8, "#000000", "#ff0000")
		triangle(img, point(50,200), point(300,200), point(175,100), "#ff642b")
		circle(img, point(390,10), 75, "#ffff00") 
	elif choice == 6:
		exit()
	else:
		print("Invalid input. Try again.")