import pygame #Impordime pygame'i
import sys #Impordime sys'i

pygame.init() #Algatan pygame'i
screen=pygame.display.set_mode([640,480]) #Muutuja screen saab väärtuseks pygame.display.set_mode([640,480])
pygame.display.set_caption('2') #Määrab praeguse akna pealkirja

screen.fill([204, 255, 204]) #Täidab ekraani

#Lisame tausta
bg = pygame.image.load("bg_shop.WEBP") #Muutja bg saab väärtuse pygame.image.load("bg_shop.WEBP")
screen.blit(bg,[0,0]) #Tausta asetus ekraanil (laius,kõrgus)

#Lisame inimese
seller = pygame.image.load("seller.WEBP") #Muutuja seller saab väärtuse pygame.image.load("seller.WEBP")
seller = pygame.transform.scale(seller, [258, 305]) #Muutuja seller saab väärtuse pygame.transform.scale(seller, [258, 305])
screen.blit(seller,[103,159]) #Inimese asetus ekraanil (laius,kõrgus)

#Lisame jutumulli
chat = pygame.image.load("chat.WEBP") #Muutuja chat saab väärtuse pygame.image.load("chat.WEBP")
chat = pygame.transform.scale(chat, [255, 201]) #Muutuja chat saab väärtuse pygame.transform.scale(chat, [255, 201])
screen.blit(chat,[246,66]) #Jutumulli asetus ekraanil (laius,kõrgus)

#Lisame teksti
font = pygame.font.Font(None, 30) #Muutuja font saab väärtuse pygame.font.Font(None, 30)
text = font.render("Tere, olen Kermo", True, [255,255,255]) #Muutuja text saab väärtuse font.render("Tere, olen Kermo", True, [255,255,255])
screen.blit(text, [290,140]) #Teksti asetus ekraanil (laius, kõrgus)

pygame.display.flip() #Kuvab lisatud objektid ekraanile

#Pygame exit
while True: #Kui on True
    for event in pygame.event.get(): #For iga event in pygame.even.get()
        if event.type == pygame.QUIT: #Kui event.type == pygame.QUIT
             sys.exit(0) #Lahkub programmist, kui on 0
             