#ZADANIE 2. Podana jest lista zawierająca elementy o wartościach 1-n.
#Napisz funkcję, która sprawdzi, jakich elementów brakuje:
#1-n = [1,2,3,4,5,...,10]
#np. n=10
#wejście: [2,3,7,4,9], 10
#wyjście: [1,5,6,8,10]

def zadanie2(l=[2,3,7,4,9], n=10):

    full_list = list(range(1, n+1))
    new_l = []

    for number in full_list:
        if number not in l:
            new_l.append(number)
    
    return new_l;
