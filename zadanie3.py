#ZADANIE 3. Należy wygenerować listę liczb od 2 do 5.5 ze skokiem co 0.5.
#Dane wynikowe muszą być typu decimal.

from decimal import *

def zadanie3(start=2, stop=5.5, step=0.5):

    number = Decimal(start)
    list = [number]
    
    while number != Decimal(stop):
        number = number+Decimal(step)
        list.append(number)
    
    return list;
