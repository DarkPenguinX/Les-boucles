print ('''Bienvenue dans le programme pour cacluler ta moyenne
tape q à tout moment pour quitter la boucle.''')
print("Insere une note sur 20: ")
number_notes=0
note=0
abandon=False
while note != "q":
    if not note.isnumeric():
        if note == "q":
            abandon=True
            break
        else:
            print("Invalid")
            continue
    elif note.isnumeric():
        if int(instruction) < 0 or int(instruction) > 20:
            print("Valeur trop basse ou trop haute")
            continue
        else:
             note = note + int(instruction)
            number_notes += 1
   
moyenne = note / number_notes
moyenne = round(moyenne, 1)
print(f"Ta moyenne est de {moyenne}/20")    

        
        