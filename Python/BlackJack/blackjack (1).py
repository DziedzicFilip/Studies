import random
talia = [10,10,10,10,9,9,9,9,8,8,8,8,7,7,7,7,6,6,6,6,5,5,5,5,4,4,4,4,3,3,3,3,2,2,2,2,'q','q','q','q','k','k','k','k','j','j','j','j','a','a','a','a']

def hit(reka_gracza, talia_gry):
        los = talia[random.randrange(0,len(talia))]
        reka_gracza.append(los)
        talia_gry.remove(los)
def double_down(reka_gracza, talia_gry):
    hit(reka_gracza, talia_gry)



def start():
    talia_gry = talia
    reka_gracza = []
    reka_gracza2 = []
    reka_krupiera = []
    split = 0
    start = True
    for i in range(2):
        los = talia[random.randrange(0,len(talia))]
        reka_gracza.append(los)
        talia_gry.remove(los)
    for i in range(2):
        los = talia[random.randrange(0,len(talia))]
        reka_krupiera.append(los)
        talia_gry.remove(los)
    print(reka_gracza)
    print(reka_krupiera[random.randrange(0,1)])
    while start:
        action = input("podaj co chcesz zrobic")
        match action:
            case 1:
                hit(reka_gracza, talia_gry)
            case 2:
                double_down(reka_gracza, talia_gry)
            case 3:
                split_t=True
                while split_t:
                    x = input("podaj split")
                    for i in reka_gracza:
                        if reka_gracza[i] == x:
                            reka_gracza.remove(x)
                            reka_gracza2.append(x)
                            hit(reka_gracza2, talia_gry)
                            hit(reka_gracza, talia_gry)
                            split_t=False
                        else:
                            print("nie ma takiej karty- ")
                            warunek = input("Czy chcesz podaj inna? 1 - tak 0 nie ")
                            if warunek==0:
                                split_t=False
            case 4:
                start=False






start()