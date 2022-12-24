import os
import time
from csv import writer
import csv
import pandas as pd
import shutil
import json

pon = os.listdir("./defolt/files")
ok = len(os.listdir("./defolt/files"))

def clear():
    os.system('clear||cls')

def checkrus():
    if os.path.isfile("rus.json"):
        if ok == 0:
            print("Нужны файлы tutorial.csv и characters.csv")
        else:
            if ok == 1:
                print("Чего то не хватает")
            if os.path.isfile("./defolt/files/characters.csv") and os.path.isfile("./defolt/files/tutorial.csv"):
                print("Все найдено!\nПриступаю к работе!")
                time.sleep(3)
                clear()

def check():
    if os.path.isfile("eng.json"):
        if ok == 0:
            print("Need files tutorial.csv и characters.csv")
        else:
            if ok == 1:
                print("Something missing")
            if os.path.isfile("./defolt/files/characters.csv") and os.path.isfile("./defolt/files/tutorial.csv"):
                print("All founded!")
                time.sleep(3)
                clear()

if os.path.isfile("eng.json") or os.path.isfile("rus.json"):
    check() or checkrus()
else:
    try:
        russian = int(input("1.English\n2.Russian\n"))
    except ValueError:
        print(f"{style.RED}You wrote the word...{style.WHITE}")
        quit()
    if russian == 1:
        x = {
                "lang": "eng",
            }
        with open('eng.json', 'w') as json_file:
            json.dump(x, json_file)
        time.sleep(3)
        clear()
        check()
    elif russian == 2:
        
        x2 = {
                "lang": "rus",
            }
        with open('rus.json', 'w') as json_file:
            json.dump(x2, json_file)
        time.sleep(3)
        clear()
        checkrus()

    
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def menu():
    print (f"{style.GREEN}-------------SpaceCat1748 edition--------------")
    print (f"{style.CYAN}1. Edit Robots in tutorial")
    print (f"{style.CYAN}2. Add Character")
    print (f"{style.CYAN}3. Exit")

def menuRussian():
    print (f"{style.GREEN}-------------SpaceCat1748 версия--------------")
    print (f"{style.CYAN}1. Изменить ботов в tutorial.csv")
    print (f"{style.CYAN}2. Скопировать перса в characters.csv")
    print (f"{style.CYAN}3. Выход")

        
def copy():
    shutil.copy("./defolt/files/characters.csv", "./output/characters.csv")
    selectedcharacters = input("shelly\ncolt\nbull\nbrock\nricochet\nspike\nbarley\njessie\nnita\ndynamike\nelprimo\nmortis\ncrow\npoco\nbo\npiper\npam\ntara\ndarryl\npenny\nfrank\ngene\ntick\nleon\nrosa\ncarl\nbibi\n8bit\nsandy\nbea\nemz\nmr.p\nmax\njacky\ngale\nnani\nsprout\nsurge\ncolette\namber\nlou\nbyron\nedgar\nruffs\nstu\nbelle\nsqueak\ngrom\nbuzz\ngriff\nash\nmeg\nlolla\nfang\neve\njanet\nbonnie\notis\nsam\ngus\nbuster\nchester\ngray\nmandy\n Select: ")
    with open('./output/characters.csv', 'r') as ef, open('./output/characters.csv', 'a') as of:
        for line in ef:
            if selectedcharacters in line:
                if "human" in line:
                    of.write(line)
    print("added")
    time.sleep(3)
    clear()

    shutil.copy("./output/characters.csv", "./defolt/backuped/characters.csv")

def copyrus():
    shutil.copy("./defolt/files/characters.csv", "./output/characters.csv")
    selectedcharacters = input("shelly\ncolt\nbull\nbrock\nricochet\nspike\nbarley\njessie\nnita\ndynamike\nelprimo\nmortis\ncrow\npoco\nbo\npiper\npam\ntara\ndarryl\npenny\nfrank\ngene\ntick\nleon\nrosa\ncarl\nbibi\n8bit\nsandy\nbea\nemz\nmr.p\nmax\njacky\ngale\nnani\nsprout\nsurge\ncolette\namber\nlou\nbyron\nedgar\nruffs\nstu\nbelle\nsqueak\ngrom\nbuzz\ngriff\nash\nmeg\nlolla\nfang\neve\njanet\nbonnie\notis\nsam\ngus\nbuster\nchester\ngray\nmandy\n Выберете: ")
    with open('./output/characters.csv', 'r') as ef, open('./output/characters.csv', 'a') as of:
        for line in ef:
            if selectedcharacters in line:
                if "human" in line:
                    of.write(line)

    print("Скопирован")
    time.sleep(3)
    clear()
    shutil.copy("./output/characters.csv", "./defolt/backuped/characters.csv")

if os.path.isfile("./eng.json"):
    while True:
        menu()
        try:
            pon = int(input(f"{style.CYAN}Select: {style.WHITE}"))
        except ValueError:
            print(f"{style.RED}You wrote the word...{style.WHITE}")
            quit()

        if pon == 1:
            franxx = input("Write Custom Brawler name:\n")
            df = pd.read_csv("./defolt/files/tutorial.csv")
            for index, row in df.iterrows():
                if df.loc[index,'SpawnCharacter'] == "TutorialDummy":
                    df.loc[index,'SpawnCharacter'] = franxx
                    df.to_csv('tutorial.csv', index=False)
                    shutil.copy("./tutorial.csv", "./output/tutorial.csv")
                    shutil.copy("./output/tutorial.csv", "./defolt/backuped/tutorial.csv")
            for index, row in df.iterrows():
               if df.loc[index,'SpawnCharacter'] == "TutorialDummy2":
                    df.loc[index,'SpawnCharacter'] = franxx
                    df.to_csv('tutorial.csv', index=False)
                    shutil.copy("./tutorial.csv", "./output/tutorial.csv")
                    shutil.copy("./output/tutorial.csv", "./defolt/backuped/tutorial.csv")
            for index, row in df.iterrows():
                if df.loc[index,'SpawnCharacter'] == "TutorialDummy3":
                    df.loc[index,'SpawnCharacter'] = franxx
                    df.to_csv('tutorial.csv', index=False)
                    shutil.copy("./tutorial.csv", "./output/tutorial.csv")
                    shutil.copy("./output/tutorial.csv", "./defolt/backuped/tutorial.csv")
            clear()
        elif pon == 2:
            copy()
            time.sleep(3)
            clear()
        elif pon == 3:
            quit()
elif os.path.isfile("./rus.json"):
    while True:
        menuRussian()
        try:
            pon = int(input(f"{style.CYAN}Select: {style.WHITE}"))
        except ValueError:
            print(f"{style.RED}Ты слово написал...{style.WHITE}")
            quit()
    
        if pon == 1:
            franxx = input("Имя кастомного бравлера:\n")
            df = pd.read_csv("./defolt/files/tutorial.csv")
            for index, row in df.iterrows():
                if df.loc[index,'SpawnCharacter'] == "TutorialDummy":
                    df.loc[index,'SpawnCharacter'] = franxx
                    df.to_csv('tutorial.csv', index=False)
                    shutil.copy("./tutorial.csv", "./output/tutorial.csv")
                    shutil.copy("./output/tutorial.csv", "./defolt/backuped/tutorial.csv")
            for index, row in df.iterrows():
               if df.loc[index,'SpawnCharacter'] == "TutorialDummy2":
                    df.loc[index,'SpawnCharacter'] = franxx
                    df.to_csv('tutorial.csv', index=False)
                    shutil.copy("./tutorial.csv", "./output/tutorial.csv")
                    shutil.copy("./output/tutorial.csv", "./defolt/backuped/tutorial.csv")
            for index, row in df.iterrows():
                if df.loc[index,'SpawnCharacter'] == "TutorialDummy3":
                    df.loc[index,'SpawnCharacter'] = franxx
                    df.to_csv('tutorial.csv', index=False)
                    shutil.copy("./tutorial.csv", "./output/tutorial.csv")
                    shutil.copy("./output/tutorial.csv", "./defolt/backuped/tutorial.csv")
            clear()
        elif pon == 2:
            if os.path.isfile("./defolt/backuped/characters.csv"):
                franxx2 = int(input("Хотите использовать бэкап?\n1. Да\n2. Нет\n"))
                if franxx2 == 1:
                    print("ok")
                    selectedcharacters = input("shelly\ncolt\nbull\nbrock\nricochet\nspike\nbarley\njessie\nnita\ndynamike\nelprimo\nmortis\ncrow\npoco\nbo\npiper\npam\ntara\ndarryl\npenny\nfrank\ngene\ntick\nleon\nrosa\ncarl\nbibi\n8bit\nsandy\nbea\nemz\nmr.p\nmax\njacky\ngale\nnani\nsprout\nsurge\ncolette\namber\nlou\nbyron\nedgar\nruffs\nstu\nbelle\nsqueak\ngrom\nbuzz\ngriff\nash\nmeg\nlolla\nfang\neve\njanet\nbonnie\notis\nsam\ngus\nbuster\nchester\ngray\nmandy\n Выберете: ")
                    with open('./output/characters.csv', 'r') as ef, open('./output/characters.csv', 'a') as of:
                        for line in ef:
                            if selectedcharacters in line:
                                if "human" in line:
                                    of.write(line)
                    print("Скопирован")
                    time.sleep(3)
                    clear()
                    shutil.copy("./output/characters.csv", "./defolt/backuped/characters.csv")             
                elif franxx2 == 2:
                    copyrus()
                    time.sleep(3)
                    clear()
            else:
                copyrus()
                time.sleep(3)
                clear()
        elif pon == 3:
            quit()
        elif pon > 3:
            print(f"{style.CYAN}Такого пункта пока нету {style.WHITE}")
            quit()
    
