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

    def question_suivante(self,fenetre, question):
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
        Label(fenetre_principale, text="Vous avez Serez rediriger vers le quizz de votre section").pack()
        if parcours=='00': 
            Label(fenetre_principale, text="blablabla").pack()
            Button(fenetre_principale, text='aller au quizz' , command=lambda *args:demande_question(questions1)).pack()
        elif parcours =='01':
            Button(fenetre_principale, text='aller au quizz' , command=lambda *args:demande_question(questions2)).pack()
        elif parcours =='10':
            Button(fenetre_principale, text='aller au quizz' , command=lambda *args:demande_question(questions3)).pack()
        elif parcours =='11':
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
nombre_de_questions = 3
index2= -1


questions_choix = []
fichier = open("gh.txt", "r")
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
Label(fenetre_principale, text="Tu es nul. Mais continues à visiter c'est bon pour ta culture G !").pack()
button = Button(fenetre_principale, text="Bienvenue au musee ", command=parcours_musee())
button.pack()
fenetre_principale.mainloop()
