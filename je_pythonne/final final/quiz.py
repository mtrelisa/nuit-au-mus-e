from tkinter import Tk, Frame, Label, Button


class Question:
    def __init__(self, question, reponses, bonnereponse):
        self.question = question
        self.reponses = reponses
        self.bonnereponse = bonnereponse

    def verification(self, lettre, fenetre):
        global nb_bonnes_rep
        if(lettre == self.bonnereponse):
            label = Label(fenetre, text="Bravo !")
            nb_bonnes_rep += 1
        else:
            label = Label(fenetre, text="Tu es nul. Mais continues à visiter c'est bon pour ta culture G !")
        label.pack()
        fenetre.after(1000, lambda *args: self.question_suivante(fenetre))

    def afficher_fenetre(self, fenetre_principale):
        fenetre = Frame(fenetre_principale)
        Label(fenetre, text=self.question).pack()
        Button(fenetre, text=self.reponses[0], command=lambda *args: self.verification("A", fenetre)).pack()
        Button(fenetre, text=self.reponses[1], command=lambda *args: self.verification("B", fenetre)).pack()
        return fenetre

    def question_suivante(self,question,fenetre):
        fenetre.pack_forget()
        demande_question(question)


def demande_question(questions):
    global  fenetre_principale, index, button, nb_bonnes_rep, nombre_de_questions
    if(len(questions) == index + 1):
        Label(fenetre_principale, text="Vous avez eu " + str(nb_bonnes_rep) + " sur " + str(nombre_de_questions) + "\n bonne reponse").pack()
        return
    button.pack_forget()
    index += 1
    questions[index].afficher_fenetre(fenetre_principale).pack()
    
    
class Musee:
    def __init__(self, question, reponses):
        self.question = question
        self.reponses = reponses

    def association(self, lettre, fenetre):
        global parcours
        if(lettre == 'A'):
            parcours+='0'

        else:
            parcours+='1'

        fenetre.after(1000, lambda *args: self.question_suivante(fenetre))

    def afficher_choix(self, fenetre_principale):
        fenetre = Frame(fenetre_principale)
        Label(fenetre, text=self.question).pack()
        Button(fenetre, text=self.reponses[0], command=lambda *args: self.association("A", fenetre)).pack()
        Button(fenetre, text=self.reponses[1], command=lambda *args: self.association("B", fenetre)).pack()
        return fenetre

    def question_suivante(self, fenetre):
        fenetre.pack_forget()
        parcours_musee()

def parcours_musee():
    global questions1,questions2,questions3,questions4, fenetre_principale, parcours, button
    if(len(parcours) == 2 ):
        Label(fenetre_principale, text="Vous serez redirige vers le quizz de l'oeuvre choisie").pack()
        if parcours=='00': 
            Label(fenetre_principale, text="La grotte d'El Castillo comprend un gisement archéologique et une grotte ornée situés sur le monte Castillo à Puente Viesgo (Cantabrie, Espagne).On recense plus de 80 empreintes de mains et des figures circulaires réalisés avec des pigments rouges. Un de ces disques vient d’être daté d’au moins 40 800 ans et devient le plus ancien art pariétal au monde").pack()
            Button(fenetre_principale, text='aller au quizz' , command=lambda *args:demande_question(questions1)).pack()
        elif parcours =='01':
            Label(fenetre_principale, text="La grotte de Lascaux, située sur la commune de Montignac-Lascaux, dans le département français de la Dordogne en région Nouvelle-Aquitaine. Leur âge est estimé entre environ 19 000 et 17 000 ans.  Elle est parfois surnommée « la chapelle Sixtine de l'art pariétal » du à la qualité esthétique de ses œuvres. ").pack()
            Button(fenetre_principale, text='aller au quizz' , command=lambda *args:demande_question(questions2)).pack()
        elif parcours =='10':
            Label(fenetre_principale, text="La civilisation minoenne a révélé de nombreuses fresques, réalisées par des peintres expérimentés, qui se trouvaient dans les pièces d'apparat et aux entrées du palais. L’une des plus célèbres se trouvait au palais de Cnossos en Crète. Elle représente, sur un fond bleu, un taureau qui est en train de charger vers la gauche. Trois “acrobates” l’entourent, qui exécutent toutes les phases d’un saut périlleux").pack()
            Button(fenetre_principale, text='aller au quizz' , command=lambda *args:demande_question(questions3)).pack()
        elif parcours =='11':
            Label(fenetre_principale, text="La scène peinte sur cette amphore grecque d'Athènes, datant des années 540-520 avant notre ère, présente le moment du combat entre le lion et Héraklès.").pack()
            Button(fenetre_principale, text='aller au quizz' , command=lambda *args:demande_question(questions4)).pack()
        else:
            return
    
    elif(len(parcours) == 0 ):
        questions_choix[0].afficher_choix(fenetre_principale).pack()
        
    elif(len(parcours) == 1 ):
        if parcours=='0': 
            button.pack_forget()
            questions_choix[1].afficher_choix(fenetre_principale).pack()
        elif parcours=='1': 
            button.pack_forget()
            questions_choix[2].afficher_choix(fenetre_principale).pack()




questions1= []      
fichier = open("question.txt", "r")
ligne = fichier.readline()
while(ligne != ""):
    ques = ligne
    reponses = []
    for i in range(2):
        reponses.append(fichier.readline())
    bonnereponse = fichier.readline()
    bonnereponse = bonnereponse[:-1]
    questions1.append(Question(ques, reponses, bonnereponse))
    ligne = fichier.readline()
fichier.close()

questions2 =  []
fichier = open("question2.txt", "r")
ligne = fichier.readline()
while(ligne != ""):
    ques = ligne
    reponses = []
    for i in range(2):
        reponses.append(fichier.readline())
    bonnereponse = fichier.readline()
    bonnereponse = bonnereponse[:-1]
    questions2.append(Question(ques, reponses, bonnereponse))
    ligne = fichier.readline()
fichier.close()

questions3= []
fichier = open("question3.txt" , "r")
ligne = fichier.readline()
while(ligne != ""):
    ques = ligne
    reponses = []
    for i in range(2):
        reponses.append(fichier.readline())
    bonnereponse = fichier.readline()
    bonnereponse = bonnereponse[:-1]
    questions3.append(Question(ques, reponses, bonnereponse))
    ligne = fichier.readline()
fichier.close()

questions4= []
fichier = open("question4.txt", "r")
ligne = fichier.readline()
while(ligne != ""):
    ques = ligne
    reponses = []
    for i in range(2):
        reponses.append(fichier.readline())
    bonnereponse = fichier.readline()
    bonnereponse = bonnereponse[:-1]
    questions4.append(Question(ques, reponses, bonnereponse))
    ligne = fichier.readline()
fichier.close() 





index = -1
nb_bonnes_rep = 0
nombre_de_questions = 2
index2= -1


questions_choix = []
fichier = open("choixepoque.txt", "r")
ligne = fichier.readline()
while(ligne != ""):
    ques = ligne
    reponses = []
    for i in range(2):
        reponses.append(fichier.readline())
    questions_choix.append(Musee(ques, reponses))
    ligne = fichier.readline()
fichier.close()
parcours=""
 




fenetre_principale = Tk()
Label(fenetre_principale, text="Bienvenue au musée !").pack()
button = Button(fenetre_principale, text="J'espère que ce quizz te plaira !", command=parcours_musee())
button.pack()
fenetre_principale.mainloop()