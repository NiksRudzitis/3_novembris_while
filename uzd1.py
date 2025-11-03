# Summe ievaditos skaitlus 0 norada, ka darbs jabeidz
summa = 0
x = int(input("Ievadi skaitli (0 lai beigtu): "))
while x != 0:
    summa += x
    x = int(input("Ievadi skaitli (0 lai beigtu): "))
print("Summa:", summa)
