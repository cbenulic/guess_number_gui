from tkinter import *
import random

class Gissanumret(Frame):
    def __init__(self, master):
        super(Gissanumret, self).__init__(master)
        self.grid()
        self.starta_spel()
    
    #Skapar relevanta variabler och bygger GUI    
    def starta_spel(self):
        self.numret = random.randint(1,100)
        self.gissningar = 0
        
        #Skapar textruta för instruerande texter och placerar den i GUI
        self.text = Text(self, height = 3, width = 71, wrap = WORD, bg = "yellow")
        self.text.insert(0.0, "Välkommen till spelet \"Gissa mitt tal\"!\nDu ska gissa vilket tal jag tänker på")
        self.text.configure(state = DISABLED)
        self.text.grid(row = 0, columnspan = 4, sticky = W)
        
        #Skapar etikett och placerar den i GUI
        self.etikett_gissning = Label(self, text = "Jag gissar på: ")
        self.etikett_gissning.grid(row = 1, column = 0, sticky = W)
        
        #Skapar ruta för inskrivning av gissning och placerar den i GUI
        self.skriv = Entry(self, width = 4)
        self.skriv.grid(row = 1, column = 0, sticky = E)
        
        #Skapar etikett och placerar den i GUI
        self.etikett_antal = Label(self, text = "Antal gissningar: ")
        self.etikett_antal.grid(row = 1, column = 1, sticky = W)
        
        #Skapar ruta för visning av antal gissningar och placerar den i GUI
        self.antal = Entry(self, width = 2)
        self.antal.insert(0, self.gissningar)
        self.antal.grid(row = 1, column = 1, sticky = E)
        
        #Skapar knapp för att gissa och placerar den i GUI
        self.gissa = Button(self, text = "Gissa", padx = 1, command = self.gissa_nummer)
        self.gissa.grid(row = 1, column = 2, sticky = W)
        
        #Skapar knapp för att starta om spelet och placerar deni GUI
        self.ny_omgang = Button(self, text = "Ny omgång", padx = 1, command = self.starta_om)
        self.ny_omgang.grid(row = 1, column = 2, sticky = E)
        
        #Skapar knapp för att avsluta spelet och placerar den i GUI
        self.avsluta = Button(self, text = "Avsluta", command = self.avsluta_spel)
        self.avsluta.grid(row = 1, column = 3, sticky = W+E)
        
    #Avslutar spelet    
    def avsluta_spel(self):
        self.quit()
    
    #Startar om spelet. Ändrar info som visas, återställer räknare för gissningar och genererar nytt tal som ska gissas    
    def starta_om(self):
        self.gissningar = 0
        self.numret = random.randint(1,100)
        self.text.configure(bg = "yellow", state = NORMAL)
        self.text.delete(0.0, END)
        self.text.insert(0.0, "Välkommen till spelet \"Gissa mitt tal\"!\nDu ska gissa vilket tal jag tänker på")
        self.text.configure(state = DISABLED)
        self.antal.delete(0, END)
        self.antal.insert(0, self.gissningar)
        self.skriv.delete(0, END)
    
    #Kontrollerar gissning    
    def gissa_nummer(self):
        try: 
            gissning = int(self.skriv.get())
        except ValueError:
            self.text.configure(bg = "pink", state = NORMAL)
            self.text.delete(0.0, END)
            self.text.insert(0.0, "Du måste gissa på ett heltal")
            self.text.configure(state = DISABLED)
        else:
            #Ökar räknaren för antal gissningar och visar användaren att gissningen var för hög
            if gissning > self.numret:
                self.gissningar += 1
                self.text.configure(bg = "blue", state = NORMAL)
                self.text.delete(0.0, END)
                self.text.insert(0.0, "Du gissade för högt")
                self.text.configure(state = DISABLED)
                self.antal.delete(0, END)
                self.antal.insert(0, self.gissningar)
                #Ökar räknaren för antal gissningar och visar användaren att gissningen var för låg
            elif gissning < self.numret:
                self.gissningar += 1
                self.text.configure(bg = "red", state = NORMAL)
                self.text.delete(0.0, END)
                self.text.insert(0.0, "Du gissade för lågt")
                self.text.configure(state = DISABLED)
                self.antal.delete(0, END)
                self.antal.insert(0, self.gissningar)
            #Ökar räknaren för antal gissningar och visar användaren att gissningen var rätt
            elif gissning == self.numret:
                self.gissningar +=1
                self.text.configure(bg = "green", state = NORMAL)
                self.text.delete(0.0, END)
                self.text.insert(0.0, "Du gissade RÄTT!")
                self.text.configure(state = DISABLED)
                self.antal.delete(0, END)
                self.antal.insert(0, self.gissningar)
        
        
root = Tk()
root.title("Gissa mitt nummer")
root.geometry("503x100")

app = Gissanumret(root)

root.mainloop()
