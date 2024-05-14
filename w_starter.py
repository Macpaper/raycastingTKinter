# yes this code is bad but do it work? kinda

from tkinter import *
import requests
import time, math 
# plz install pillow for this to work
from PIL import Image # <-- need this because image.put is way too slow and I can't find a workaround. install pillow for this to work
from PIL import ImageTk as itk
# nvm can't figure it out in time
# import numpy as np
# from io import StringIO
                        
from tkinter import ttk
# Displays a window with weather information on the screen.
# my_image = canvas.create_image(0, 0, image=photo_image, anchor=NW)
# coordinates = canvas.coords(my_image)
# window.update()
# time.sleep(0.017)
def move_up(event):
    # someLabel.place(x=someLabel.winfo_x(), y=someLabel.winfo_y() - 1)
    ...
# moving stuff using canvas
def move_up(event, event2="lol"):
    # canvas.move(myImage, 0, -10)
    ...

class WeatherApp:
    def __init__(self):
        # Creates the main window and specifies the window title and dimensions (WxH).
        self.main_window = Tk()
        self.main_window.title("Here's the weather!")
        self.main_window.geometry("300x150")

        self.left_frame = Frame(self.main_window)
        self.right_frame = Frame(self.main_window)
        self.updateButton = Button(self.right_frame, text="update", command=self.get_weather_info, fg="green")
        self.deleteButton = Button(self.right_frame, text="Quit", command=self.main_window.destroy, fg='red')
        self.startButton = Button(self.right_frame, text="high res", command=self.start_game, fg='purple')
        self.startButton2 = Button(self.right_frame, text="low res (faster)", command=self.start_game2, fg='black')
        self.value = StringVar()
        self.value.set("No weather available!!")

        self.weather_label = Label(self.left_frame, textvariable=self.value, font=("monospace", 8))
        self.weather_label.pack(side="left", fill="x")
        self.updateButton.pack(side='top', fill='x')
        self.deleteButton.pack(side='bottom', fill='x')
        self.startButton.pack(side="bottom", fill='x')
        self.startButton2.pack(side="bottom", fill='x')
        self.left_frame.pack(side='left')
        self.right_frame.pack(side='left')
        # This loop hands off control of your program.  You will receive "callbacks"
        # based on the ones you have setup above.   In this program we have two, one
        # for each button.
        mainloop()
        

    # Query weather information from wttr.in service
    def get_weather_info(self):
        print('wtf boom')
        try:
            # This URL queries the current weather for
            # 94523 (Pleasant Hill, CA)
            # The '0T' characters at the end represent these options:
            # 0 - Display only the current weather (no forecast)
            # T - Don't use color codes (for use in repl.it)
            weather_url = "https://wttr.in/22206?0T"
            response = requests.get(weather_url)
            weather_info = response.text
        except Exception as e:
            weather_info = f"Error fetching weather: {e}"
        self.value.set(weather_info)
    def start(self, w, h, s):
        self.deleteButton.destroy()
        self.weather_label.destroy()
        self.startButton.destroy()
        self.updateButton.destroy()
        self.left_frame.destroy()
        self.right_frame.destroy()
        self.main_window.title("Here they come...")
        self.main_window.geometry("800x600")
        # self.canvas = Canvas(self.main_window,width=800,height=600)
        self.main_window.destroy()
        main(w, h, s)
    def start_game(self):
        self.start(400, 300, 2)

    def start_game2(self):
        self.start(200, 150, 4)

left, right, up, down = False, False, False, False

def update(deltaTime):
    global dirX, dirY, planeX, planeY, posX, posY
    moveSpeed = deltaTime * 15.0
    rotSpeed = deltaTime * 8.0
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

def init(window):
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

map = [
  [8,8,8,8,8,8,8,8,8,8,8,4,4,6,4,4,6,4,6,4,4,4,6,4],
  [8,0,0,0,0,0,0,0,0,0,8,4,0,0,0,0,0,0,0,0,0,0,0,4],
  [8,0,3,3,0,0,0,0,0,8,8,4,0,0,0,0,0,0,0,0,0,0,0,6],
  [8,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
  [8,0,3,3,0,0,0,0,0,8,8,4,0,0,0,0,0,0,0,0,0,0,0,4],
  [8,0,0,0,0,0,0,0,0,0,8,4,0,0,0,0,0,6,6,6,0,6,4,6],
  [8,8,8,8,0,8,8,8,8,8,8,4,4,4,4,4,4,6,0,0,0,0,0,6],
  [7,7,7,7,0,7,7,7,7,0,8,0,8,0,8,0,8,4,0,4,0,6,0,6],
  [7,7,0,0,0,0,0,0,7,8,0,8,0,8,0,8,8,6,0,0,0,0,0,6],
  [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,6,0,0,0,0,0,4],
  [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,6,0,6,0,6,0,6],
  [7,7,0,0,0,0,0,0,7,8,0,8,0,8,0,8,8,6,4,6,0,6,6,6],
  [7,7,7,7,0,7,7,7,7,8,8,4,0,6,8,4,8,3,3,3,0,3,3,3],
  [2,2,2,2,0,2,2,2,2,4,6,4,0,0,6,0,6,3,0,0,0,0,0,3],
  [2,2,0,0,0,0,0,2,2,4,0,0,0,0,0,0,4,3,0,0,0,0,0,3],
  [2,0,0,0,0,0,0,0,2,4,0,0,0,0,0,0,4,3,0,0,0,0,0,3],
  [1,0,0,0,0,0,0,0,1,4,4,4,4,4,6,0,6,3,3,0,0,0,3,3],
  [2,0,0,0,0,0,0,0,2,2,2,1,2,2,2,6,6,0,0,5,0,5,0,5],
  [2,2,0,0,0,0,0,2,2,2,0,0,0,2,2,0,5,0,5,0,0,0,5,5],
  [2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,5,0,5,0,5,0,5,0,5],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
  [2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,5,0,5,0,5,0,5,0,5],
  [2,2,0,0,0,0,0,2,2,2,0,0,0,2,2,0,5,0,5,0,0,0,5,5],
  [2,2,2,2,1,2,2,2,2,2,2,1,2,2,2,5,5,5,5,5,5,5,5,5]
]

class Sprite:
    def __init__(self, x, y, texture):
        self.x = x
        self.y = y
        self.texture = texture

numSprites = 19

sprites = [ 
            # green lights
           Sprite(20.5, 11.5, 10), 
           Sprite(18.5, 4.5, 10), 
           Sprite(10.5, 4.5, 10), 
           Sprite(10.0, 12.5, 10), 
           Sprite(3.5, 6.5, 10), 
           Sprite(3.5, 20.5, 10), 
           Sprite(3.5, 14.5, 10), 
           Sprite(14.5, 20.5, 10), 
           # pillars
           Sprite(18.5, 10.5, 9), 
           Sprite(18.5, 11.5, 9), 
           Sprite(18.5, 12.5, 9), 
           # barrels
           Sprite(21.5, 1.5, 8), 
           Sprite(15.5, 1.5, 8), 
           Sprite(16.0, 1.8, 8), 
           Sprite(16.2, 1.2, 8), 
           Sprite(3.5, 2.5, 8), 
           Sprite(9.5, 15.5, 8), 
           Sprite(10.0, 15.1, 8), 
           Sprite(10.5, 15.8, 8), 
        ]
spriteOrder = [0] * numSprites
spriteDistance = [0] * numSprites

# def sortSprites(order, dist, amt):
    

posX, posY = 22, 12
dirX, dirY = -1, 0
planeX, planeY = 0, 0.66
running = True
texWidth = 64
texHeight = 64
num_textures = 8
import random
textures = []

# TODO: Create an Enum so I can reference textures by an ID string instead of memorizing x and y
def create_texture(x, y, id, img, width = texWidth, height = texHeight, xoff = texWidth, yoff = texHeight):
    tex_x = x * xoff
    tex_y = y * yoff
    texture = [[0] * (texWidth) for _ in range(texHeight)]
    for i in range(width):
        for j in range(height):
            # FOR HEX VALUES
            # texture[i][j] = '#%02x%02x%02x' % img.get(j + tex_y, i + tex_x) # <-- switched bcuz i like texture[width][height] better
            # FOR INTEGER VALUES
            rgb_t = img.get(j + tex_y, i + tex_x)
            texture[j][i] = rgb_t[0] << 16 | rgb_t[1] << 8 | rgb_t[2] # <-- switched bcuz i like texture[width][height] better
            # print(texture[i][j])
            # FOR TUPLE RGB VALUES
            # texture[i][j] = img.get(j + tex_y, i + tex_x)
            # print(texture[i][j])
    return texture
def main(wid, hei, sc):
    global running

    S_WIDTH = wid
    S_HEIGHT = hei
    scaleFactor = sc

    w = S_WIDTH
    h = S_HEIGHT
    window = Tk()
    canv = Canvas(window, width=S_WIDTH * scaleFactor, height=S_HEIGHT * scaleFactor)
    canv.pack()
    ATLAS = PhotoImage(file="atlas.png") 
    SPRITE_ATLAS = PhotoImage(file="wolfAtlas.png")
    running = True

    ZBuffer = [0] * S_WIDTH
    # create buffer of data, put into image, display image on canvas. if this is slow then textures just can't be made or there needs to be a faster way. 
    # buffer = [ ['#333333'] * S_WIDTH for _ in range(S_HEIGHT) ]
    buffer = [0] * (S_WIDTH * S_HEIGHT)

    # creating a texture is similar. create_texture returns a 2d array of hex RGB colors. put this buffer into an image then display on canvas.
    tex1 = create_texture(0, 2, 1,  ATLAS)
    # WALLS
    textures.append(tex1)
    textures.append(create_texture(0, 0, 0, ATLAS))
    textures.append(create_texture(1, 1, 1, ATLAS))
    textures.append(create_texture(2, 0, 2, ATLAS))
    textures.append(create_texture(3, 4, 3, ATLAS))
    textures.append(create_texture(4, 0, 4, ATLAS))
    textures.append(create_texture(5, 3, 5, ATLAS))
    textures.append(create_texture(6, 3, 6, ATLAS))
    
    # SPRITES
    textures.append(create_texture(0, 0, 7, SPRITE_ATLAS))
    textures.append(create_texture(1, 0, 8, SPRITE_ATLAS))
    textures.append(create_texture(2, 2, 9, SPRITE_ATLAS))

    init(window)
    while running:
        canv.delete('all')
        canv.create_rectangle(0, 0, S_WIDTH, S_HEIGHT, fill="black")
        currTime = int(round(time.time() * 1000))

        # FLOORS # RAN TOO SLOW
        # for y in range(int(S_HEIGHT / 2 + 1), S_HEIGHT):
        #     rayDirX0 = dirX - planeX
        #     rayDirY0 = dirY - planeY
        #     rayDirX1 = dirX + planeX
        #     rayDirY1 = dirY + planeY

        #     p = y - S_HEIGHT / 2
        #     posZ = 0.5 * S_HEIGHT

        #     rowDistance = 1e30 if p == 0 else posZ / p

        #     floorStepX = rowDistance * (rayDirX1 - rayDirX0) / S_WIDTH
        #     floorStepY = rowDistance * (rayDirY1 - rayDirY0) / S_WIDTH

        #     floorX = posX + rowDistance * rayDirX0
        #     floorY = posY + rowDistance * rayDirY0

        #     for x in range(S_WIDTH):
        #         cellX = int(floorX)
        #         cellY = int(floorY)
        #         tx = int(texWidth * (floorX - cellX)) & (texWidth - 1)
        #         ty = int(texHeight * (floorY - cellY)) & (texHeight - 1)
        #         floorX += floorStepX
        #         floorY += floorStepY

        #         checkerBoardPattern = int(cellX + cellY) & 1
        #         if checkerBoardPattern == 0: floorTexture = 3
        #         else:                        floorTexture = 4

        #         ceilingTexture = 6
        #         color = textures[floorTexture][tx][ty]
        #         color = (color >> 1) & 8355711 
        #         index = int(y * S_WIDTH + x)
        #         # TOO SLOW :( 
        #         # buffer[index] = color 

                # color = textures[ceilingTexture][tx][ty]
                # color = (color >> 1) & 8355711
                # index = int(S_HEIGHT - y - 1) * S_WIDTH + x
                # buffer[index] = color
            
        
        for x in range(0, w):
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

            # texturing calculations 
            texNum = map[mapX][mapY] - 1
            wallX = 0 # <-- find EXACTLY where wall is hit now.
            if side == 0: wallX = posY + perpWallDist * rayDirY
            else:         wallX = posX + perpWallDist * rayDirX
            wallX -= math.floor(wallX)

            # x coordinate on the TEXTURE
            texX = int(wallX * texWidth)
            if side == 0 and rayDirX > 0: texX = texWidth - texX - 1
            if side == 1 and rayDirY < 0: texX = texWidth - texX - 1

            # no idea how this works but ill find out later
            step = 1.0 * texHeight / lineHeight
            texPos = (drawStart - h / 2 + lineHeight / 2) * step
            for y in range(int(drawStart), int(drawEnd)):
                index = int(y * S_WIDTH + x)
                texY = int(texPos) & (texHeight - 1)
                texPos += step
                color = textures[texNum][texX][texY]
                buffer[index] = color

            # if map[mapX][mapY] == 1: color = "red"
            # elif map[mapX][mapY] == 2: color = "green"
            # elif map[mapX][mapY] == 3: color = "blue"
            # elif map[mapX][mapY] == 4: color = "purple"
            # else: color = "yellow"
            # canv.create_line(x, drawStart, x, drawEnd, fill=color)

            ZBuffer[x] = perpWallDist

        for i in range(numSprites):
            spriteOrder[i] = i
            spriteDistance[i] = ((posX - sprites[i].x) * (posX - sprites[i].x) + (posY - sprites[i].y) * (posY - sprites[i].y))

        # ill review sorting algorithms later sry
        for i in range(len(spriteDistance) - 1):
            for j in range(i, len(spriteDistance)):
                if spriteDistance[j] < spriteDistance[i]:
                    temp = spriteDistance[j]
                    spriteDistance[j] = spriteDistance[i]
                    spriteDistance[i] = temp

                    temp2 = spriteOrder[j]
                    spriteOrder[j] = spriteOrder[i]
                    spriteOrder[i] = temp2
                    
        # i dont even remember why i did this. why not just sort from reverse up there????
        for i in range(math.floor(len(spriteDistance) / 2)):
            temp = spriteDistance[i] 
            spriteDistance[i] = spriteDistance[len(spriteDistance) - 1 - i]
            spriteDistance[len(spriteDistance) - 1 - i] = int(temp)

            temp2 = spriteOrder[i]
            spriteOrder[i] = math.floor(spriteOrder[len(spriteOrder) - 1 - i])
            spriteOrder[len(spriteOrder) - 1 - i] = int(temp2)
        

        # spriteDistance.sort(reverse=True)
        # spriteOrder.sort(reverse=True)

        for i in range(numSprites):
            spriteX = sprites[spriteOrder[i]].x - posX
            spriteY = sprites[spriteOrder[i]].y - posY
            invDet = 1.0 / (planeX * dirY - dirX * planeY)
            transformX = invDet * (dirY * spriteX - dirX * spriteY)
            transformY = invDet * (-planeY * spriteX + planeX * spriteY)

            spriteScreenX = int((w/2) * (1 + transformX / transformY))

            spriteHeight = abs(int(h / (transformY)))
            drawStartY = -spriteHeight / 2 + h / 2
            if drawStartY < 0: drawStartY = 0
            drawEndY = spriteHeight / 2 + h / 2
            if drawEndY >= h: drawEndY = h - 1

            spriteWidth = abs(int(h / (transformY)))
            drawStartX = -spriteWidth / 2 + spriteScreenX
            if drawStartX < 0: drawStartX = 0
            drawEndX = spriteWidth / 2 + spriteScreenX
            if drawEndX >= w: drawEndX = w - 1
            for stripe in range(int(drawStartX), int(drawEndX)):
                texX = int(256 * (stripe - (-spriteWidth / 2 + spriteScreenX)) * texWidth / spriteWidth) / 256

                if transformY > 0 and stripe > 0 and stripe < w and transformY < ZBuffer[stripe]:
                    for y in range(int(drawStartY), int(drawEndY)):
                        d = (y) * 256 - h * 128 + spriteHeight * 128
                        texY = ((d * texHeight) / spriteHeight) / 256
                        color = textures[sprites[spriteOrder[i]].texture][int(texX)][int(texY)]
                        index = int(y * S_WIDTH + stripe)
                        if (color & 0x00FFFF) != 0: buffer[index] = color


        # img = PhotoImage(width=S_WIDTH, height=S_HEIGHT)
        # img.put(buffer, (0, 0, S_WIDTH, S_HEIGHT)) # this is RIDICULOUSLY SLOW so I'm using pillow instead. is there a faster way?
        newimage = Image.new('RGB', (S_WIDTH, S_HEIGHT))
        newimage.putdata(buffer)
        newimage = newimage.resize((S_WIDTH * scaleFactor, S_HEIGHT * scaleFactor))
        realImg = itk.PhotoImage(newimage)
        canv.create_image(0, 0, image=realImg, anchor=NW)

        for y in range(h):
            for x in range(w):
                index = y * S_WIDTH + x
                buffer[index] = 0
        
        oldTime = currTime
        currTime = int(round(time.time() * 1000))
        frameTime = (currTime - oldTime) / 1000.0
        update(frameTime)
        window.update()

myApp = WeatherApp()