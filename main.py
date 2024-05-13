from tkinter import *
import time, math
S_WIDTH = 800
S_HEIGHT = 600
window = Tk()
canv = Canvas(window, width=S_WIDTH, height=S_HEIGHT)
canv.pack()
running = True

left, right, up, down = False, False, False, False


def init():
  window.bind("<KeyPress>", keyPressEvent)
  window.bind("<KeyRelease>", keyReleaseEvent)

def keyPressEvent(e):
  handleKeyPress(e.char.lower(), True)
def keyReleaseEvent(e):
  handleKeyPress(e.char.lower(), False)

def handleKeyPress(key, pressed):
  global up, down, left, right
  if key == 'w':
    up = pressed 
  if key == 'a':
    left = pressed
  if key == 's':
    down = pressed
  if key == 'd':
    right = pressed



moveSpeed = 0.5
rotSpeed = 0.05
def update():
  global dirX, dirY, planeX, planeY, posX, posY
  if up:
    if map[int(posX + dirX * moveSpeed)][int(posY)] == False: posX += dirX * moveSpeed 
    if map[int(posX)][int(posY + dirY * moveSpeed)] == False: posY += dirY * moveSpeed 
  if down:
    if map[int(posX - dirX * moveSpeed)][int(posY)] == False: posX -= dirX * moveSpeed
    if map[int(posX)][int(posY - dirY * moveSpeed)] == False: posY -= dirY * moveSpeed
  if right:
    oldDirX = dirX
    # trig matrix for rotating 2d vector by rotSpeed angle
    dirX = dirX * math.cos(-rotSpeed) - dirY * math.sin(-rotSpeed)
    dirY = oldDirX * math.sin(-rotSpeed) + dirY * math.cos(-rotSpeed)
    oldPlaneX = planeX
    planeX = planeX * math.cos(-rotSpeed) - planeY * math.sin(-rotSpeed)
    planeY = oldPlaneX * math.sin(-rotSpeed) + planeY * math.cos(-rotSpeed)
  if left:
    oldDirX = dirX
    # trig matrix for rotating 2d vector by rotSpeed angle
    dirX = dirX * math.cos(rotSpeed) - dirY * math.sin(rotSpeed)
    dirY = oldDirX * math.sin(rotSpeed) + dirY * math.cos(rotSpeed)
    oldPlaneX = planeX
    planeX = planeX * math.cos(rotSpeed) - planeY * math.sin(rotSpeed)
    planeY = oldPlaneX * math.sin(rotSpeed) + planeY * math.cos(rotSpeed)
map = [
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,2,2,2,2,2,0,0,0,0,3,0,3,0,3,0,0,0,1],
  [1,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,2,0,0,0,2,0,0,0,0,3,0,0,0,3,0,0,0,1],
  [1,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,2,2,0,2,2,0,0,0,0,3,0,3,0,3,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,4,0,4,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,4,0,0,0,0,5,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,4,0,4,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,4,0,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

posX, posY = 22, 12
dirX, dirY = -1, 0
planeX, planeY = 0, 0.66
w = S_WIDTH
h = S_HEIGHT
init()
# plane is a bit smaller than direction so it is less than 90 deg FOV (~66 probably?)
while running:
  canv.delete('all')
  canv.create_rectangle(0, 0, S_WIDTH, S_HEIGHT, fill="black")
  for x in range(0, w, 2):
    cameraX = 2 * x / w - 1 # map the CURRENT X ON THE SCREEN SCREEN to 
                            # an X POS ON THE CAMERA PLANE
    rayDirX = dirX + planeX * cameraX # <-- this was the x component of the direction of 
                                      # the current ray being calculated. cameraX is like
                                      # the MAGNITUDE of the planeX. dirX is the x component
                                      # of the direction of the player.
    rayDirY = dirY + planeY * cameraX # <-- same for rayDirY ^^
    
    '''
    deltaDistX = sqrt(1 + rayDirY^2/rayDirX^2) # look at png to see how this is explained
    deltaDistY = sqrt(1 + rayDirX^2/rayDirY^2) # or look at https://gamedev.stackexchange.com/questions/45013/raycasting-tutorial-vector-math-question
    '''
    # to see why it simplifies look at 
    # https://stackoverflow.com/questions/55086770/raycastings-formula-understending
    
    mapX = int(posX)
    mapY = int(posY)
    # sideDistX = 0
    # sideDistY = 0
    # perpWallDist = 0
    # stepX = 0
    # stepY = 0
    
    deltaDistX = 1e30 if rayDirX == 0 else abs(1 / rayDirX)
    deltaDistY = 1e30 if rayDirY == 0 else abs(1 / rayDirY) 
    
    hit = 0
    # side = 0
    # come back to review this later
    if rayDirX < 0:
      stepX = -1
      sideDistX = (posX - mapX) * deltaDistX # diff from left side of
                                            # 'square' then just mult by ddx
    else:
      stepX = 1
      sideDistX = (mapX + 1.0 - posX) * deltaDistX # right side of square
      
    if rayDirY < 0:
      stepY = -1
      sideDistY = (posY - mapY) * deltaDistY
    else:
      stepY = 1
      sideDistY = (mapY + 1.0 - posY) * deltaDistY
    
    # doesn't calculate where the wall was hit but does find which wall and what side
    while hit == 0:
      if sideDistX < sideDistY:
        sideDistX += deltaDistX
        mapX += stepX
        side = 0
      else:
        sideDistY += deltaDistY
        mapY += stepY
        side = 1
      if map[mapX][mapY] > 0: hit = 1
    
    if side == 0: perpWallDist = (sideDistX - deltaDistX)
    else: perpWallDist = (sideDistY - deltaDistY)
    
    lineHeight = int(h / perpWallDist)
    drawStart = -lineHeight / 2 + h / 2
    if drawStart < 0: drawStart = 0
    drawEnd = lineHeight / 2 + h / 2
    if drawEnd >= h: drawEnd = h - 1

    if map[mapX][mapY] == 1: color = "red"
    elif map[mapX][mapY] == 2: color = "green"
    elif map[mapX][mapY] == 3: color = "blue"
    elif map[mapX][mapY] == 4: color = "purple"
    else: color = "yellow"
    if side == 1: color = "grey"
    canv.create_line(x, drawStart, x, drawEnd, fill=color)
   
  update()
  window.update()
  