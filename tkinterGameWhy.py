from tkinter import *
import time
import random

WIDTH = 800
HEIGHT = 600
window = Tk()
# window.geometry(f'{WIDTH}x{HEIGHT}')
window.title("Hi ball game :)")
running = True

C = Canvas(window, width=WIDTH, height=HEIGHT)
C.pack()

class RectGuy:
  def __init__(self, x, y, canvas):
    self.x = x
    self.y = y
    self.dx = random.randint(-10, 10)
    self.dy = random.randint(-10, 10)
    self.size = 50
    self.color = "red"
  def update(self):
    self.x += self.dx
    self.y += self.dy
    if self.x < 0 or self.x + self.size > WIDTH:
      self.dx = -self.dx
    if self.y < 0 or self.y + self.size > HEIGHT:
      self.dy = -self.dy
    
  def draw(self, canvas):
    canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, fill=self.color, width=0)
rect_guys = []
for i in range(100):
  rect_guys.append(RectGuy(random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50), C))
while running:
  C.delete('all')
  for g in rect_guys:
    g.update()
    g.draw(C)
  # guy1.update()
  # guy1.draw(C)
  window.update()
  time.sleep(0.01)
window.mainloop()