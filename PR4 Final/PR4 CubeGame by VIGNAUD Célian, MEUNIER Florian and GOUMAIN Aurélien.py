from graphics_nsi import* # Importation du module graphique graphics_nsi
from random import*

                  # Titre
pygame.mixer.music.load("Game_music_LibreDeDroit.mp3")     # Chargement de la musique
pygame.mixer.music.play()                                  # La musique est jouée



def cubeGame():
    Title = "Projet 'Clavier et déplacement' "
    pygame.display.set_caption(Title)                       # Définit le titre de la page
    coteCarre=150                                           # Définition du coté du carré
    boucle="encore"
    while boucle=="encore":
        longueurFenetre,hauteurFenetre=1000,600
        init_graphic(longueurFenetre,hauteurFenetre,Title)  # Initialisation de la fenêtre graphique
        P1=Point(coteCarre/2,300)                           # Définition de l'emplacement de la barre verte
        draw_fill_rectangle(P1,coteCarre,600,green)         # Dessine la barre verte

        x_vide,y_vide=coteCarre/2,randint(100,500)          # Définit la hauteur aléatoirement du carre Noir puis lance la fonction
        P2=Point(x_vide,y_vide)
        draw_fill_rectangle(P2,coteCarre,coteCarre,black)   # Déssine le carré noir


    #   Dessin du carré rouge ci-dessous:
        x,y=randint(450,925),randint(coteCarre/2,525)
        PRed=Point(x,y)
        draw_fill_rectangle(PRed,coteCarre,coteCarre,red)
        tours=0


    #   Mouvement du carré rouge ci-dessous:
        while x!=x_vide or y!=y_vide:
            tours+=1
            saisie=wait_arrow()
            draw_fill_rectangle(PRed,coteCarre,coteCarre,black)
            P1=Point(coteCarre/2,300)
            draw_fill_rectangle(P1,coteCarre,600,green)
            P2=Point(x_vide,y_vide)
            draw_fill_rectangle(P2,coteCarre,coteCarre,black)


        #   Le carre avance toujours à 9px sauf quand il est proche des axes x et y.
            if saisie=="up" and y>y_vide-5 and y<y_vide+5 and y>=coteCarre/2:
                if x>=coteCarre+coteCarre/2:
                    y-=1
            elif saisie=="up" and y>=coteCarre/2:    # UP
                if x>=coteCarre+coteCarre/2:
                    y-=9




            elif saisie=="down"and y>y_vide-5 and y<y_vide+5 and y<=hauteurFenetre-coteCarre/2 and x>=coteCarre+coteCarre/2:
                y+=1
            elif saisie=="down" and y<=hauteurFenetre-coteCarre/2 and x>=coteCarre+coteCarre/2:  #DOWN
                y+=9



            elif saisie=="left"and ((x-9>=coteCarre+coteCarre/2) or (x-9>=coteCarre/2 and y==y_vide)):
                x-=9
            elif saisie=="left"and ((x-1>=coteCarre+coteCarre/2) or (x-1>=coteCarre/2 and y==y_vide)): #LEFT
                x-=1


            elif saisie=="right" and x<coteCarre+coteCarre/2+5 and x<=longueurFenetre-coteCarre/2:
                x+=1
            elif saisie=="right" and x<=longueurFenetre-coteCarre/2: #RIGHT
                x+=9

            PRed=Point(x,y)
            draw_fill_rectangle(PRed,coteCarre,coteCarre,red)


    #   Nous redessinons à chaque tour la barre verte, le carré noir ainsi que le carré rouge.
        Pfond=Point(longueurFenetre/2,hauteurFenetre/2)
        draw_fill_rectangle(Pfond,longueurFenetre,hauteurFenetre,green)
        P1=Point(coteCarre/2,300)
        draw_fill_rectangle(P1,coteCarre,600,purple)
        P2=Point(x_vide,randint(coteCarre/2,525))
        draw_fill_rectangle(P2,coteCarre,coteCarre,blue)
        TxtFin=" Voulez-vous rejouer? "                     # Défini le texte de fin
        TailleTxt=50                                        # Défini la taille du texte
        Pmilieu=Point(coteCarre*2,coteCarre/5)
        xOUI,yOUI=longueurFenetre/2+coteCarre*0.5,hauteurFenetre/2-TailleTxt
        xNON,yNON=longueurFenetre/2-coteCarre*0.5,hauteurFenetre/2-TailleTxt
        PmilieuOui=Point(xOUI,yOUI)
        PmilieuNon=Point(xNON,yNON)
        aff_pol(TxtFin,TailleTxt,Pmilieu, (255, 255, 255) ) # Affiche le texte de fin
        PMO=Point(xOUI+48,yOUI+40)                          # Défini l'emplacement de de "Oui"
        aff_pol("Oui",TailleTxt,PmilieuOui, (0, 100, 00) )  # Affiche "Oui"
        PMN=Point(xNON+48,yNON+40)                          #Défini l'emplacement de "Non"
        aff_pol("Non",TailleTxt,PmilieuNon, (255, 50, 0) )  # Affiche "Non"
        P=wait_clic()                                       # Attente de coordonnée d'un clic


    #   Tourne tant qu'il n'y a pas eu de clic dans la zone souhaité
        while  P.x<429 and P.y<262  or P.x>522 and P.y>304 or P.x<576 and P.y<262 or P.x>658 and P.y>302:

        #   Nous redessinons à chaque tour la barre verte, le carré violet ainsi que le carré rouge.
            Pfond=Point(longueurFenetre/2,hauteurFenetre/2)
            draw_fill_rectangle(Pfond,longueurFenetre,hauteurFenetre,green)
            P1=Point(coteCarre/2,300)
            draw_fill_rectangle(P1,coteCarre,600,purple)    # Dessine le carré violet
            P2=Point(x_vide,randint(coteCarre/2,525))
            draw_fill_rectangle(P2,coteCarre,coteCarre,blue)
            TxtFin=" Voulez-vous rejouer? "                 # Défini le texte de fin
            TailleTxt=50
            Pmilieu=Point(coteCarre*2,coteCarre/5)
            xOUI,yOUI=longueurFenetre/2+coteCarre*0.5,hauteurFenetre/2-TailleTxt
            xNON,yNON=longueurFenetre/2-coteCarre*0.5,hauteurFenetre/2-TailleTxt
            PmilieuOui=Point(xOUI,yOUI)
            PmilieuNon=Point(xNON,yNON)
            aff_pol(TxtFin,TailleTxt,Pmilieu, (255, 255, 255) ) # Affiche le texte de fin


            PMO=Point(xOUI+48,yOUI+40)
            aff_pol("Oui",TailleTxt,PmilieuOui, (0, 100, 00) )  # Affiche "Oui"

            PMN=Point(xNON+48,yNON+40)
            aff_pol("Non",TailleTxt,PmilieuNon, (255, 50, 0) )  # Affiche "Non"

            P=wait_clic()                                   # Attend les coordonnées d'un clic




        if P.y<302 and P.y>429 or P.x>262 and P.x<522:      # Si l'utilisateur clic sur "Non", le jeu s'arrete
            boucle="exit"
        elif P.y<304 and P.x>576 or P.y>262 and P.x<658:    # Si l'utilisateur clic sur "Oui", le jeu continu
            coteCarre=coteCarre*0.8                         # Le carré rouge devien 20% plus petit





cubeGame()                                     # Exécute la fonction





wait_escape()# Permet d’attendre un clic sur Echap avant de fermer la fenêtre graphique