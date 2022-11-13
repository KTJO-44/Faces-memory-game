#Faces test

import random, pygame, sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 1500
WINDOWHEIGHT = 800
BGCOLOUR = (255, 255, 255)
REVEALSPEED = 8

pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,  WINDOWHEIGHT))
pygame.display.set_caption('Faces')

DARKPINK = (211, 0, 67)
WHITE = (255, 255, 255)

#DISPLAYSURF.fill(BGCOLOUR)

fontObj = pygame.font.SysFont('trebuchetms', 32) #setting the font for the program
text1 = "Hi, my name is Lisa."
text2 = "This is a test to see if the text works!"
text3 = "Awesome, now let's get on."
text4 = "Just seeing how this thing works"
textList = [text1, text2, text3, text4]


faceBase = pygame.image.load('faceBase1.png')
smallBase = pygame.transform.scale(faceBase, (100, 100))
##faceEyebrows = pygame.image.load('faceEyebrows1.png')
##smallEyebrows = pygame.transform.scale(faceBase, (100, 100))
##faceEyes = pygame.image.load('faceEyes1.png')
##smallEyes = pygame.transform.scale(faceEyes, (100, 100))
##faceHair = pygame.image.load('faceHair1.png')
##smallHair = pygame.transform.scale(faceHair, (100, 100))
##faceMouth = pygame.image.load('faceMouth1.png')
##smallMouth = pygame.transform.scale(faceMouth, (100, 100))
##faceNose = pygame.image.load('faceNose1.png')
##smallNose = pygame.transform.scale(faceNose, (100, 100))

Names = ['Amanda', 'Amy', 'Anna', 'Bella', 'Catherine', 'Corinna', 'Cathleen', 'Imogen', 'Isabella', 'Izzy', 'India', 'Idina', 'Lizzy', 'Lottie', 'Liza', 'Lorena']
Jobs = ['Teacher', 'Programmer', 'Doctor', 'Scientist', 'Researcher', 'Lab technician', 'Policeman', 'Nurse', 'Writer', 'Director', 'Journalist']
Likes = ['horses', 'ice skating', 'playing video games', 'drawing', 'watching movies', 'computers', 'chocolate', 'apples', 'rainy days', 'dogs']
Dislikes = ['sharks', 'hockey', 'reading', 'painting', 'going to the cinema', 'books', 'licorice', 'grapes', 'sunny days', 'cats']

Eyebrows = ['faceEyebrowsBlonde', 'faceEyebrowsBlue', 'faceEyebrowsBrown', 'faceEyebrowsGrey', 'faceEyebrowsLightBrown', 'faceEyebrowsMaroon', 'faceEyebrowsRed', 'faceEyebrowsThick', 'faceEyebrowsThin', 'faceEyebrowsWhite']
Eyes = ['faceEyesBlue', 'faceEyesBrown', 'faceEyesGreen', 'faceEyesLightBrown', 'faceEyesOrange', 'faceEyesPurple']
Hair = ['faceHairBlack', 'faceHairBlonde', 'faceHairBlue', 'faceHairDarkBrown', 'faceHairLightBrown', 'faceHairRed']
Mouths = ['faceMouthBlue', 'faceMouthBrightRed', 'faceMouthLemon', 'faceMouthLime', 'faceMouthNude', 'faceMouthOrange', 'faceMouthPink', 'faceMouthRed']
Noses = ['faceNoseHooked', 'faceNoseOval', 'faceNoseSharp', 'faceNoseTriangle', 'faceNoseUnshadedOval']


EyebrowImgs = []
EyeImgs = []
HairImgs = []
MouthImgs = []
NoseImgs = []

#import all images into their respective lists
for i in range(len(Eyebrows)):
    image = Eyebrows[i] + '.png'
    imported = pygame.image.load(image)
    EyebrowImgs.append(imported)

for i in range(len(Eyes)):
    image = Eyes[i] + '.png'
    imported = pygame.image.load(image)
    EyeImgs.append(imported)

for i in range(len(Hair)):
    image = Hair[i] + '.png'
    imported = pygame.image.load(image)
    HairImgs.append(imported)

for i in range(len(Mouths)):
    image = Mouths[i] + '.png'
    imported = pygame.image.load(image)
    MouthImgs.append(imported)

for i in range(len(Noses)):
    image = Noses[i] + '.png'
    imported = pygame.image.load(image)
    NoseImgs.append(imported)

random.shuffle(Names) #randomise the list
random.shuffle(Jobs) #instead of selecting a random choice from list
random.shuffle(Likes) #so that we can remove items as we go
random.shuffle(Dislikes) #and don't get any duplicate information
ALLFACES = [[], [], [], [], [], [], [], []]
BIGFACES = [[], [], [], [], [], [], [], []]
for i in range(8):
    randomFace = []
    randomFace.append(faceBase)
    randEyebrow = random.choice(EyebrowImgs)
    randomFace.append(randEyebrow)
    randEye = random.choice(EyeImgs)
    randomFace.append(randEye)
    randHair = random.choice(HairImgs)
    randomFace.append(randHair)
    randMouth = random.choice(MouthImgs)
    randomFace.append(randMouth)
    randNose = random.choice(NoseImgs)
    randomFace.append(randNose)

##    randName = random.choice(Names)
##    randJob = random.choice(Jobs)
##    randLikes = random.choice(Likes)
##    randDislikes = random.choice(Dislikes)

##    ALLFACES[i].append(randName)
##    ALLFACES[i].append(randJob)
##    ALLFACES[i].append(randLikes)
##    ALLFACES[i].append(randDislikes)
    
    ALLFACES[i].append(Names[0])
    ALLFACES[i].append(Jobs[0])
    ALLFACES[i].append(Likes[0])
    ALLFACES[i].append(Dislikes[0])


    BIGFACES[i].append(Names[0])
    BIGFACES[i].append(Jobs[0])
    BIGFACES[i].append(Likes[0])
    BIGFACES[i].append(Dislikes[0])
    BIGFACES[i].append(faceBase)
    BIGFACES[i].append(randEyebrow)
    BIGFACES[i].append(randEye)
    BIGFACES[i].append(randHair)
    BIGFACES[i].append(randMouth)
    BIGFACES[i].append(randNose)

    del Names[0] #delete used item from list so can't be used again
    del Jobs[0]
    del Likes[0]
    del Dislikes[0]

    smallRandomFace = []

    for x in range(6): #make thumbnail sized faces for the memory grid game
        smallFeature = pygame.transform.scale(randomFace[x], (150, 150))
        smallRandomFace.append(smallFeature)
        ALLFACES[i].append(smallFeature)

def getMouseClicked():
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
            return True
        else:
            return False


def speech(text, textcounter, facecounter):
##    textToSay = fontObj.render(text, True, DARKPINK, WHITE)
##    DISPLAYSURF.blit(textToSay, (0, 600))
    if textcounter == 0:
        textToSay = fontObj.render("Hi, I'm " + ALLFACES[facecounter][0] + ".", True, DARKPINK, WHITE)
        DISPLAYSURF.blit(textToSay, (0, 600))
    elif textcounter == 1:
        textToSay = fontObj.render("I work as a " + ALLFACES[facecounter][1] + ".", True, DARKPINK, WHITE)
        DISPLAYSURF.blit(textToSay, (0, 600))
    elif textcounter == 2:
        textToSay = fontObj.render("I like " + ALLFACES[facecounter][2] + ".", True, DARKPINK, WHITE)
        DISPLAYSURF.blit(textToSay, (0, 600))
    elif textcounter == 3:
        textToSay = fontObj.render("And I don't like " + ALLFACES[facecounter][3] + ".", True, DARKPINK, WHITE)
        DISPLAYSURF.blit(textToSay, (0, 600))
        
textcounter = 0
facecounter = 0
mouseClicked = False

while True:

    DISPLAYSURF.fill(BGCOLOUR)

    mouseClicked = False

##    DISPLAYSURF.blit(faceBase, (0, 0))
##    DISPLAYSURF.blit(faceEyebrows, (0, 0))
##    DISPLAYSURF.blit(faceEyes, (0, 0))
##    DISPLAYSURF.blit(faceHair, (0, 0))
##    DISPLAYSURF.blit(faceMouth, (0, 0))
##    DISPLAYSURF.blit(faceNose, (0, 0))
##
##    DISPLAYSURF.blit(smallBase, (600, 0))
##    DISPLAYSURF.blit(smallEyebrows, (600, 0))
##    DISPLAYSURF.blit(smallEyes, (600, 0))
##    DISPLAYSURF.blit(smallHair, (600, 0))
##    DISPLAYSURF.blit(smallMouth, (600, 0))
##    DISPLAYSURF.blit(smallNose, (600, 0))
    for i in range(6):
        DISPLAYSURF.blit(BIGFACES[facecounter][i+4], (0, 0))

    for i in range(6):
        #DISPLAYSURF.blit(smallRandomFace[i], (600,0))
        DISPLAYSURF.blit(ALLFACES[facecounter][(i+4)], (600,0))


    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONUP:
            mouseClicked = True

    if textcounter < len(textList): 
        text = textList[textcounter]
        speech(text, textcounter, facecounter)
        if mouseClicked == True:
            textcounter = textcounter + 1
    elif textcounter >= len(textList):
        textcounter = 0
        if facecounter < 7:
            facecounter = facecounter + 1
        else:
            print("Face memory game starts here")
        #print(facecounter)
        

    pygame.display.update()
    FPSCLOCK.tick(FPS)



