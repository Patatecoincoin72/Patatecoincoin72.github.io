"""
Programme réalisé par Eli, BERTRAS, 1G7 et Dina, YASIN, 1G3
"""

import pygame

piece=0
mur=0
cle=0

#initialisation graphique
pygame.init()
fenetre=pygame.display.set_mode((900, 506))
pygame.display.set_caption("jeu de Patate")
font=pygame.font.Font('freesansbold.ttf', 20)

image1=pygame.image.load("entree.png")
image2=pygame.image.load("salle-a-manger.png")
image2_2=pygame.image.load("salle-a-manger2.png")
image3=pygame.image.load("buanderie.png")
image4=pygame.image.load("toilettes-patate.png")
image4_2=pygame.image.load("toilettes-patate2.png")
image5=pygame.image.load("cuvettes.png")
image6=pygame.image.load("chambre-patate.png")
image7=pygame.image.load("cuisine.png")
image8=pygame.image.load("passage-secret.png")
image9=pygame.image.load("chambre.png")
image10=pygame.image.load("penderie.png")
image11=pygame.image.load("sdb.png")
image12=pygame.image.load("toilettes.png")


text1=font.render("Vous vous trouvez dans l'entrée du gâteau", True, (0,255,0))
text2=font.render("Vous vous trouvez dans la salle à manger", True, (0,255,0))
text2_2=font.render("Patate est en train de manger le gâteau", True, (0, 0,0))
text3=font.render("Vous vous trouvez dans la buanderie", True, (0, 0, 0))
text4=font.render("Vous vous trouvez dans les toilettes de Patate (le canard jaune)", True, (0, 0, 0))
text4_2=font.render("Patate: Laisse moi faire caca. Vas me faire à manger femme.", True, (255, 0, 0))
text4_3=font.render("Vous vous trouvez dans les toilettes de Patate mais il n'est plus là", True, (0,0, 0))
text5=font.render("Vous vous trouvez dans les cuvettes des toilettes de Patate, sortez vite avant qu'il ne vous voie", True, (255, 0,0))
text5_2=font.render("Vous trouvez une clé", True, (0, 0, 0))
text6=font.render("Vous vous trouvez dans la chambre de Patate", True, (0, 0,0))
text7=font.render("Vous vous trouvez dans la cuisine", True, (0,255,0))
text8=font.render("Vous vous trouvez dans le passage secret", True, (0, 0,0))
text9=font.render("Vous vous trouvez dans la chambre", True, (0, 0,0))
text10=font.render("Vous vous trouvez dans la penderie", True, (0, 0,0))
text11=font.render("Vous vous trouvez dans la salle de bain", True, (0, 0,0))
text12=font.render("Bravo, vous vous trouvez dans les toilettes, vous avez fini le jeu !", True, (0, 0,0))
text12_2=font.render("Mais Patate sait que vous êtes allé dans ses cuvettes...", True, (255, 0,0))

dansQuellePieceEstLePersonnage=1


def decrireLaPiece(piece):
    global finito,cle
    if piece==1:
        fenetre.blit(image1,(0,0))
        fenetre.blit(text1,(0,440))
    elif piece==2:
        if finito==False:
            fenetre.blit(image2,(0,0))
            fenetre.blit(text2,(0,440))
        else:
            fenetre.blit(image2_2,(0,0))
            fenetre.blit(text2_2,(0,440))
    elif piece==3:
        fenetre.blit(image3,(0,0))
        fenetre.blit(text3,(0,445))
    elif piece==4:
        if finito==False:
            fenetre.blit(image4,(0,0))
            fenetre.blit(text4,(0,440))
            fenetre.blit(text4_2,(0,460))
        else:
            fenetre.blit(image4_2,(0,0))
            fenetre.blit(text4_3,(0,440))
    elif piece==5:
        cle+=1
        fenetre.blit(image5,(0,0))
        fenetre.blit(text5,(0,440))
        fenetre.blit(text5_2,(0,460))
    elif piece==6:
        fenetre.blit(image6,(0,0))
        fenetre.blit(text6,(0,440))
    elif piece==7:
        fenetre.blit(image7,(0,0))
        fenetre.blit(text7,(0,440))
    elif piece==8:
        fenetre.blit(image8,(0,0))
        fenetre.blit(text8,(0,440))
    elif piece==9:
        fenetre.blit(image9,(0,0))
        fenetre.blit(text9,(0,440))
    elif piece==10:
        fenetre.blit(image10,(0,0))
        fenetre.blit(text10,(0,445))
    elif piece==11:
        fenetre.blit(image11,(0,0))
        fenetre.blit(text11,(0,440))
    elif piece==12:
        fenetre.blit(image12,(0,0))
        fenetre.blit(text12,(0,440))
        fenetre.blit(text12_2,(0,460))



def decision(direction,piece):
    global mur,gateaup,finito
    print("Vous désirez allez au",direction)
    print()
    memorisePiece=piece

    #N
    if direction=='n':
        if piece==3:
            piece=1
        elif piece==5:
            piece=4
        elif piece==4:
            piece=2
        elif piece==2:
            piece=7
        elif piece==11:
            piece=9
        elif piece==12:
            piece=11

    #S
    elif direction=='s':
        if piece==1:
            piece=3
        elif piece==7:
            piece=2
        elif piece==2:
            piece=4
        elif piece==4:
            if finito==True:
                piece=5
            else:
                print("Patate: Je t'ai dit de me laisser tranquille, ne rentre pas dans mes cuvettes !!")
        elif piece==9:
            piece=11
        elif piece==11:
            piece=12

    #E
    elif direction=='e':
        if piece==2:
            piece=1
        elif piece==6:
            piece=2
        elif piece==8:
            piece=7
        elif piece==9:
            piece=8
        elif piece==10:
            piece=9

    #O
    elif direction=='o':
        if piece==1:
            piece=2
        elif piece==2:
            piece=6
        elif piece==7:
            if cle<1:
                print("Cette pièce est inaccessible, il faut une clé pour ouvrir la porte")
            else:
                piece=8
        elif piece==8:
            piece=9
        elif piece==9:
            piece=10


    if memorisePiece==piece:
        print("Vous vous mangez le mur du gâteau")
        mur+=1
    return piece


#recette
gateaup=False
finito=False
oeuf=farine=levure=sucre=chocolat=morts=trop=0

#programme gateau
def gateau(piece):
    global gateaup,finito,oeuf,farine,levure,sucre,chocolat,morts,trop
    if piece==4:
        gateaup=True
    if piece==7 and gateaup==True and finito==False:
        print("La recette d'un gateau:")
        print("   4 oeufs")
        print("   100g de farine")
        print("   un sachet de leuvure chimique")
        print("   200g de sucre")
        print("   tes grand morts˿k̤̼̞͍̳͎͚͈͕͔̲͔̘̦ͫ̓̄̉̅̇̓ͭ̆̃͢͞,̛ͫ̀̃̍ͬ̔͢͝͏͙̦̖͔̝̦̫̪̘̟̞͉̹͡")
        print("   une tablette de chocolat")

        while trop<=3 and (oeuf!=4 or farine!=100 or levure!=1 or sucre!=200 or morts<665 or chocolat!=1):
            recette=input("Ajoutez les ingédients: oeuf, farine, levure, sucre, chocolat, mes grands morts")
            if recette=="fast":
                oeuf=4
                farine=100
                levure=1
                sucre=200
                morts=666
                chocolat=1
            elif recette=="oeuf":
                if oeuf>4:
                    print("Il y a trop d'oeuf dans la recette")
                    trop+=1
                else:
                    oeuf+=1
            elif recette=="farine":
                if farine>100:
                    print("Il y a trop de farine")
                    trop+=1
                else:
                    farine+=100
            elif recette=="levure":
                if levure>1:
                    print("Il y a trop de levure")
                    trop+=1
                else:
                    levure+=1
            elif recette=="sucre":
                if sucre>200:
                    print("Il y a trop de sucre")
                    trop+=1
                else:
                    sucre+=100
            elif recette=="chocolat":
                if chocolat>1:
                    print("Il y a trop de chocolat")
                    trop+=1
                else:
                    chocolat+=1
            elif recette=="mes grands morts":
                morts+=666
                if morts>666:
                    print("Oui, toujours plus de mortsk̤̼̞͍̳͎͚͈͕͔̲͔̘̦ͫ̓̄̉̅̇̓ͭ̆̃͢͞,̛ͫ̀̃̍ͬ̔͢͝͏͙̦̖͔̝̦̫̪̘̟̞͉̹͡n̛̛̜̠̞̪͎̰̦̟̩̻̣̖̦͇̯̪̏ͣ́̂ͧͮͦ̈́̃ͧ̇̕͢͟")
            else:
                print("Ce n'est pas dans la recette, Patate n'est pas content")
                trop+=1
            print()
            print("oeuf=",oeuf,"sur 4")
            print("farine=",farine,"g sur 100g")
            print("levure=",levure,"sachet sur 1")
            print("sucre=",sucre,"g sur 200g")
            print("chocolat=",chocolat,"tablette sur 1")
            print("morts=",morts,"mort sur n̛̛̜̠̞̪͎̰̦̟̩̻̣̖̦͇̯̪̏ͣ́̂ͧͮͦ̈́̃ͧ̇̕͢͟o̩̩̠͇̖̮̝̟͙͔̞̻͓͂͗̋ͭ̓ͪ̎͆͐͠,̢̛̦̺͔̳̰̫̞͍͕͎̝ͣ̅̋̏̾͛ͨ̍ͦ̃̈̿̃̅̚͝l̨̛͍̼̹̯͎̥̻͎̣͙̠̪̜̂̔͐͂ͭ,̨̛̝͍̘̼̱̙͉̝͙̥̃̄ͣ̇͌ͬ̒͌͟͡l̵̢̤̝̠͓̯̥͉̘̹̮̭͖̞̝͚̮̐́̀̾͑͆̿͂̽̄̎̋ͫ͒̿ͮ")
            print()

        if trop>3:
            print("Vous n'avez pas respecté la recette, le gateau est raté...")
            oeuf=farine=levure=sucre=chocolat=morts=trop=0

        else:
            print("Vous avez réussi le gateau, Patate est content et vous laisse maintenant accès à ses toilettes")
            finito=True
    return finito, gateaup


loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            loop=False
        elif event.type==pygame.KEYDOWN:
            dansQuellePieceEstLePersonnage=decision(event.unicode,dansQuellePieceEstLePersonnage)
            if event.key==pygame.K_ESCAPE or event.unicode=='q':
                loop=False
            elif mur>5:
                print("Vous avez fini les murs du gâteau, la maison s'écroule")
                loop=False
    gateau(dansQuellePieceEstLePersonnage)
    decrireLaPiece(dansQuellePieceEstLePersonnage)

    pygame.display.flip()
pygame.quit()

