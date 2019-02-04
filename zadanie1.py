#ZADANIE 1. Napisz generator kodów pocztowych, który przyjmuje 2 stringi:
#"79-900" i "80-155" i zwraca listę kodów pomiędzy nimi.

def zadanie1(kod_start="79-900", kod_stop="80-155"):

    kody_pocztowe = []
    kod1 = kod_start.replace("-","")
    kod2 = kod_stop.replace("-","")
    kod1 = int(kod1)
    kod2 = int(kod2)

    kod1_temp = kod1
    for i in range(kod1_temp, kod2-1):
        kod1 = kod1+1
        kod1_str = str(kod1)
        kod1_str = kod1_str[:2] + "-" + kod1_str[2:]
        kody_pocztowe.append(kod1_str)    
    
    return kody_pocztowe;
