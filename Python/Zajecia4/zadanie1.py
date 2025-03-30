def zadanie1():
    text=input("Podaj tekst: ")
    with open("zadanie1.txt", "w") as file:
        file.write(text) 
    with open("zadanie1.bin", "wb") as file:
        file.write(text.encode("utf-8"))
if __name__ == "__main__":
    zadanie1()