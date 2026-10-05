import random
# 1. Choisir un nombre au hazard
number_to_guess = random.randint(1, 1000)
guess = -1
abandon=False

while guess != number_to_guess:
    #2.1 demander un nombre
    instruction= input("Entrez un nombre entre 1 et 1000 [q: quitter]: ")
    if not instruction.isnumeric():
      if instruction == "q":
          abandon=True
          break
    guess= int(instruction)
    if guess < number_to_guess:
        print("C'est plus")
    elif guess > number_to_guess:
        print("C'est moins")


if abandon:
    print(f"Dommage, porchaine fois utilise ton cerveau, le nombre était {number_to_guess}")
else:
    print(f"Bravo, vous avez trouvé le nombre {number_to_guess}")
    
