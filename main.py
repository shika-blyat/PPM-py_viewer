import pygame
pygame.init()

screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
"""
img = img.read().split("\n")
wh = img[1].split(" ")
if img[0].lower() != "p3" or len(wh) != 2:
	return False
try :
	h = int(wh[0])
	w = int(wh[1])
except ValueError:
	return False
if len(img[1:]) < w*h:
	return False
rgb_value = [tuple([int(i) for i in i.split(" ")]) for i in img if len(i.split()) == 3] 
"""

def draw(ppm):
	with open(ppm,"r") as img:
		img = img.read().split("\n")
		wh = img[1].split(" ")
		w = int(wh[0]) 
		h = int(wh[1])
		img = img[3:]
		img = [tuple([int(i) for i in i.split(" ")]) for i in img if len(i.split()) == 3] 
		img = [img[i:i+w] for i in range(0, len(img), w)]
		print(img)
		print(w,h)
		print(len(img))
		for k,i in enumerate(img):
			for j in range(w-1):
				pygame.draw.rect(screen,i[j],(100+1*j,100+1*k,1,1))

draw("image.ppm")
while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #pygame.display.quit()
            pygame.quit()
    pygame.display.flip()