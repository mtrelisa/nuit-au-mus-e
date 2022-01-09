# visite-au-mus-e
Un jeu où l'on visite un musée, allant d'endroit en endroit, selon nos choix.Il y a des changements "d'espaces". (Jeu sur pygame):

On choisit entre deux réponses à chaque fois. (clic droit):
 - Le premier choix "systématique"("a") serait de choisir entre une époque (reliée à l'art) et un autre histoire de nous orienter dans la partie.
 - Les choix qui vont s'ensuivre seront des minis préférences entre les tableaux d'un style choisi (en dessous des tableaux seront insérés des mini-textes pour apprendre)
 - A la fin on répondra à un mini qcm avec "oui" et "non" pour vérifier si on a bien suivi l'histoire (du moins un minimum). Si l'on réponds mal on est banni du musée. Si on
   réponds bien... bah on reste dans le musée (ok c'est nul mais les vigiles sont trop sympas). On aura accès à un autre niveau avec d'autres styles de peinture (peut-être).(ps: en fait non, un niveau ça suffit). 
   
 Interphace graphique avec tkinter
 
 CLASSES ET LES FONCTIONS QU'ELLES POSSEDENT :
 class Question: 
 - def verification(self, lettre, fenetre)
 - def afficher_fenetre(self, fenetre_principale)
 - def question_suivante(self,fenetre)
 - def demande_question(questions)
 
 class Musee:
 - def association(self, lettre, fenetre)
 - def afficher_choix(self, fenetre_principale)
 - def question_suivante(self, fenetre)
 - def parcours_musee()
 
 
 

 
