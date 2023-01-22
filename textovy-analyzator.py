"""
textovy-analyzator.py: první projekt do Engeto Online Python Akademie
autor: Long Do
e-mail: long.do@email.cz
discord: Long Do#7160
"""

from data import TEXTY as vybrane_texty, oddelujici_cara
from funkce_pro_analyzu import kontrola_registrace, zobrazit_analyzu_textu_s_grafem
from funkce_pro_sklonovani import vokativ

je_registrovan = kontrola_registrace(login := input("Přihlašovací jméno: "), heslo := input("Heslo: "))

if je_registrovan:
  print(f"{oddelujici_cara} \nVítejte v aplikaci, {vokativ(login.title())}! \nNabízíme {len(vybrane_texty)} vybrané texty k analýze.", oddelujici_cara, sep="\n")
  
  try:
    vyber_textu = int(input("Zvolte číslo textu mezi 1 a 3: "))
  except ValueError:
    print("Zadali jste jiný vstup než číslo. Program se ukončuje...")
    quit()
  
  if vyber_textu > 0 and vyber_textu < 4:
    jednotliva_slova_textu = vybrane_texty[vyber_textu - 1].split()
    zobrazit_analyzu_textu_s_grafem(jednotliva_slova_textu)
  else:
    print("Tento zvolený text neexistuje. Program se ukončuje...")
    quit()
    
else:
  print("Zadali jste špatné přihlašovací údaje. Program se ukončuje...")
  quit()