import os
import time
from csv import writer
import csv
import shutil
import json
from assets import down
from colorama import Fore, Back, Style
try:
                import pandas as pd
except ModuleNotFoundError:
                os.system("pip install pandas")

if not os.path.isdir("./defolt/backuped") and not os.path.isdir("./output"):
                os.mkdir("./output")
                os.mkdir("./defolt/backuped")
else:
                pass

verse = "1.67 Beta"

pon = os.listdir("./defolt/files")
ok = len(os.listdir("./defolt/files"))

def clear():
    os.system('clear||cls')

def checkrus():
    if os.path.isfile("rus.json"):
        if ok == 1:
            print("Скачиваю файлы")
            down("bs", 4, "./defolt/files")
        else:
            if os.path.isfile("./defolt/files/characters.csv") and os.path.isfile("./defolt/files/tutorial.csv"):
                print("Все найдено!\nПриступаю к работе!")
                time.sleep(3)
                clear()

def check():
    if os.path.isfile("eng.json"):
        if ok == 1:
            print("Need files tutorial.csv и characters.csv")
            down("bs", 4, "./defolt/files")
        else:
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
    print (Fore.GREEN + f"                        TutorialBS | Version: {verse} | Author: SpaceCat")
    print (Fore.CYAN + "1. Edit Robots in tutorial")
    print (Fore.CYAN + "2. Copy Character")
    print (Fore.CYAN + "3. Exit")

def menuRussian():
    print (Fore.GREEN + f"                   TutorialBS | Версия: {verse} | Автор: SpaceCat")
    print (Fore.CYAN + "1. Изменить ботов в tutorial.csv")
    print (Fore.CYAN + "2. Скопировать перса в characters.csv")
    print (Fore.CYAN + "3. Выход")

        
def copyeng():
     shutil.copy("./defolt/files/characters.csv", "./output/characters.csv")
     shutil.copy("./defolt/files/characters_1.csv", "./output/characters_1.csv")
     selectedcharacters = input("shelly\ncolt\nbull\nbrock\nricochet\nspike\nbarley\njessie\nnita\ndynamike\nelprimo\nmortis\ncrow\npoco\nbo\npiper\npam\ntara\ndarryl\npenny\nfrank\ngene\ntick\nleon\nrosa\ncarl\nbibi\n8bit\nsandy\nbea\nemz\nmr.p\nmax\njacky\ngale\nnani\nsprout\nsurge\ncolette\namber\nlou\nbyron\nedgar\nruffs\nstu\nbelle\nsqueak\ngrom\nbuzz\ngriff\nash\nmeg\nlolla\nfang\nFlea\njanet\nbonnie\notis\nsam\ngus\nbuster\nchester\ngray\nmandy\n Select: ")
     with open('./output/characters.csv', 'r') as ef, open('./output/characters_1.csv', 'a') as of:
                for line in ef:
                    if selectedcharacters in line:
                        if "human" in line:
                           of.write(line)
     df = pd.read_csv("./output/characters_1.csv")
     for index, row in df.iterrows():
         if df.loc[index,'Type'] == "Hero":
                                                df.loc[index,'Type'] = "Minion_Building"
                                                hue = input(f"{style.YELLOW}Custom Brawler Name:\n{style.WHITE}")
                                                df.loc[index,'Name'] = hue
                                                df.to_csv('./output/characters_1.csv', index=False)
                                                ho = int(input("Want to change speed, damage, hitpoints?\n1. Yeah\n2. No\n"))
                                                if ho == 1:
                                                        ho2 = input("Speed:")
                                                        ho3 = input("AutoAttack Damage:")
                                                        ho4 = input("Hitpoints:")
                                                        for index, row in df.iterrows():
                                                                if df.loc[index,'Homeworld'] == "human":
                                                                        df.loc[index,'Speed'] = ho2
                                                                        df.loc[index,'AutoAttackDamage'] = ho3
                                                                        df.loc[index,'Hitpoints'] = ho4
                                                                        df.to_csv('./defolt/backuped/characters_1.csv', index=False)
                                                                        with open('./defolt/backuped/characters_1.csv', 'r') as cum, open('./defolt/backuped/characters.csv', 'a') as es:
                                                                            for line in cum:
                                                                                if selectedcharacters in line:
                                                                                    if "human" in line:
                                                                                        es.write(line)
                                                                                        shutil.copy("./defolt/backuped/characters.csv", "./output/characters.csv")
                                                                                        shutil.copy("./defolt/backuped/characters_1.csv", "./output/characters_1.csv")
                                                                                        print("Copied")
                                                                                        time.sleep(3)
                                                                                        clear()
                                        
                                                    
                                                elif ho == 2:
                                                        df.to_csv('./defolt/backuped/characters_1.csv', index=False)
                                                        with open('./defolt/backuped/characters_1.csv', 'r') as cum, open('./defolt/backuped/characters.csv', 'a') as es:
                                                                for line in cum:
                                                                        if selectedcharacters in line:
                                                                                if "human" in line:
                                                                                        es.write(line)
                                                                                        shutil.copy("./defolt/backuped/characters.csv", "./output/characters.csv")
                                                                                        shutil.copy("./defolt/backuped/characters_1.csv", "./output/characters_1.csv")
                                                                                        print("Copied")
                                                                                        time.sleep(3)
                                                                                        clear()

def copyrus():
     shutil.copy("./defolt/files/characters.csv", "./output/characters.csv")
     shutil.copy("./defolt/files/characters_1.csv", "./output/characters_1.csv")
     selectedcharacters = input("shelly\ncolt\nbull\nbrock\nricochet\nspike\nbarley\njessie\nnita\ndynamike\nelprimo\nmortis\ncrow\npoco\nbo\npiper\npam\ntara\ndarryl\npenny\nfrank\ngene\ntick\nleon\nrosa\ncarl\nbibi\n8bit\nsandy\nbea\nemz\nmr.p\nmax\njacky\ngale\nnani\nsprout\nsurge\ncolette\namber\nlou\nbyron\nedgar\nruffs\nstu\nbelle\nsqueak\ngrom\nbuzz\ngriff\nash\nmeg\nlolla\nfang\nFlea\njanet\nbonnie\notis\nsam\ngus\nbuster\nchester\ngray\nmandy\n Выберете:")
     with open('./output/characters.csv', 'r') as ef, open('./output/characters_1.csv', 'a') as of:
                for line in ef:
                    if selectedcharacters in line:
                        if "human" in line:
                           of.write(line)
     df = pd.read_csv("./output/characters_1.csv")
     for index, row in df.iterrows():
                                if df.loc[index,'Type'] == "Hero":
                                                df.loc[index,'Type'] = "Minion_Building"
                                                hue = input(f"{style.YELLOW}Имя Кастом Бойца:\n{style.WHITE}")
                                                df.loc[index,'Name'] =hue
                                                df.to_csv('./output/characters_1.csv', index=False)
                                
     with open('./output/characters_1.csv', 'r') as ef, open('./output/characters.csv', 'a') as of:
            for line in ef:
                if selectedcharacters in line:
                    if "human" in line:
                                of.write(line)
            print("Скопирован")
            time.sleep(3)
            clear()
            shutil.copy("./output/characters.csv", "./defolt/backuped/characters.csv")
            shutil.copy("./output/characters_1.csv", "./defolt/backuped/characters_1.csv")
    
if os.path.isfile("./eng.json"):
    while True:
        menu()
        try:
            pon = int(input(f"{style.CYAN}Select: {style.WHITE}"))
        except ValueError:
            print(f"{style.RED}You wrote the word...{style.WHITE}")
            time.sleep(3)
            clear()

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
            if os.path.isfile("./defolt/backuped/characters.csv") and os.path.isfile("./defolt/backuped/characters_1.csv"):
                shutil.copy("./defolt/files/characters_1.csv", "./defolt/backuped/characters_1.csv")
                franxx2 = int(input("Use backup?\n1. Yeah\n2. No\n"))
                if franxx2 == 1:
                        
                     selectedcharacters = input("shelly\ncolt\nbull\nbrock\nricochet\nspike\nbarley\njessie\nnita\ndynamike\nelprimo\nmortis\ncrow\npoco\nbo\npiper\npam\ntara\ndarryl\npenny\nfrank\ngene\ntick\nleon\nrosa\ncarl\nbibi\n8bit\nsandy\nbea\nemz\nmr.p\nmax\njacky\ngale\nnani\nsprout\nsurge\ncolette\namber\nlou\nbyron\nedgar\nruffs\nstu\nbelle\nsqueak\ngrom\nbuzz\ngriff\nash\nmeg\nlolla\nfang\nFlea\njanet\nbonnie\notis\nsam\ngus\nbuster\nchester\ngray\nmandy\n Select: ")
                     with open('./defolt/backuped/characters.csv', 'r') as ef, open('./defolt/backuped/characters_1.csv', 'a') as of:
                                                for line in ef:
                                                                if selectedcharacters in line:
                                                                                if "human" in line:
                                                                                                of.write(line)
                     df = pd.read_csv("./defolt/backuped/characters_1.csv")
                     for index, row in df.iterrows():
                                if df.loc[index,'Type'] == "Hero":
                                                df.loc[index,'Type'] = "Minion_Building"
                                                hue = input(f"{style.YELLOW}Custom Brawler Name:\n{style.WHITE}")
                                                df.loc[index,'Name'] = hue
                                                ho = int(input("Want to change speed, damage, hitpoints?\n1. Yeah\n2. No\n"))
                                                if ho == 1:
                                                        ho2 = input("Speed:")
                                                        ho3 = input("AutoAttack Damage:")
                                                        ho4 = input("Hitpoints:")
                                                        for index, row in df.iterrows():
                                                                if df.loc[index,'Homeworld'] == "human":
                                                                        df.loc[index,'Speed'] = ho2
                                                                        df.loc[index,'AutoAttackDamage'] = ho3
                                                                        df.loc[index,'Hitpoints'] = ho4
                                                                        df.to_csv('./defolt/backuped/characters_1.csv', index=False)
                                                                        with open('./defolt/backuped/characters_1.csv', 'r') as cum, open('./defolt/backuped/characters.csv', 'a') as es:
                                                                            for line in cum:
                                                                                if selectedcharacters in line:
                                                                                    if "human" in line:
                                                                                        es.write(line)
                                                                                        shutil.copy("./defolt/backuped/characters.csv", "./output/characters.csv")
                                                                                        shutil.copy("./defolt/backuped/characters_1.csv", "./output/characters_1.csv")
                                                                                        print("Copied")
                                                                                        time.sleep(3)
                                                                                        clear()
                                        
                                                    
                                                elif ho == 2:
                                                        df.to_csv('./defolt/backuped/characters_1.csv', index=False)
                                                        with open('./defolt/backuped/characters_1.csv', 'r') as cum, open('./defolt/backuped/characters.csv', 'a') as es:
                                                                for line in cum:
                                                                        if selectedcharacters in line:
                                                                                if "human" in line:
                                                                                        es.write(line)
                                                                                        shutil.copy("./defolt/backuped/characters.csv", "./output/characters.csv")
                                                                                        shutil.copy("./defolt/backuped/characters_1.csv", "./output/characters_1.csv")
                                                                                        print("Copied")
                                                                                        time.sleep(3)
                                                                                        clear()                                                                                      
                elif franxx2 == 2:
                     copyeng()
                     time.sleep(3)
                     clear()
            else:
                copyeng()
                time.sleep(3)
                clear()
                
        elif pon == 3:
            quit()
elif os.path.isfile("./rus.json"):
    while True:
        menuRussian()
        try:
            pon = int(input(f"{style.CYAN}Выберите: {style.WHITE}"))
        except ValueError:
            print(f"{style.RED}Ты слово написал...{style.WHITE}")
            time.sleep(3)
            clear()
    
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
            if os.path.isfile("./defolt/backuped/characters.csv") and os.path.isfile("./defolt/backuped/characters_1.csv"):
                franxx2 = int(input("Хотите использовать бэкап?\n1. Да\n2. Нет\n"))
                if franxx2 == 1:
                     selectedcharacters = input("shelly\ncolt\nbull\nbrock\nricochet\nspike\nbarley\njessie\nnita\ndynamike\nelprimo\nmortis\ncrow\npoco\nbo\npiper\npam\ntara\ndarryl\npenny\nfrank\ngene\ntick\nleon\nrosa\ncarl\nbibi\n8bit\nsandy\nbea\nemz\nmr.p\nmax\njacky\ngale\nnani\nsprout\nsurge\ncolette\namber\nlou\nbyron\nedgar\nruffs\nstu\nbelle\nsqueak\ngrom\nbuzz\ngriff\nash\nmeg\nlolla\nfang\nFlea\njanet\nbonnie\notis\nsam\ngus\nbuster\nchester\ngray\nmandy\n Выберете: ")
                     with open('./defolt/backuped/characters.csv', 'r') as ef, open('./defolt/backuped/characters_1.csv', 'a') as of:
                                                for line in ef:
                                                                if selectedcharacters in line:
                                                                                if "human" in line:
                                                                                                of.write(line)
                     df = pd.read_csv("./defolt/backuped/characters_1.csv")
                     for index, row in df.iterrows():
                                if df.loc[index,'Type'] == "Hero":
                                                df.loc[index,'Type'] = "Minion_Building"
                                                hue = input(f"{style.YELLOW}Имя Кастом Бойца:\n{style.WHITE}")
                                                df.loc[index,'Name'] = hue
                                                df.to_csv('./defolt/backuped/characters_1.csv', index=False)
                                
                     with open('./defolt/backuped/characters_1.csv', 'r') as cum, open('./defolt/backuped/characters.csv', 'a') as es:
                                                for line in cum:
                                                                if selectedcharacters in line:
                                                                            if "human" in line:
                                                                                        es.write(line)
                     print("Скопирован")
                     time.sleep(3)
                     clear()
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
    
