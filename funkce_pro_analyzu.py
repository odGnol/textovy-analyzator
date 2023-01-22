from data import registrovani_uzivatele
from data import oddelujici_cara
from funkce_pro_sklonovani import sklonovat_slovo, sklonovat_cislo

def kontrola_registrace(login, heslo):
  return True if login in registrovani_uzivatele and heslo == registrovani_uzivatele[login] else False

def analyza_textu(seznam_slov):
  pocet_slov_s_velkym_pismenem = 0
  pocet_slov_psany_velkymi_pismeny = 0
  pocet_slov_psany_malymi__pismeny = 0
  pocet_cisel = 0
  soucet_cisel = 0
  
  for slovo in seznam_slov:
    if slovo.isupper():
      pocet_slov_psany_velkymi_pismeny += 1
    elif slovo.islower():
      pocet_slov_psany_malymi__pismeny += 1
    elif slovo.isnumeric():
      pocet_cisel += 1
      soucet_cisel += int(slovo)
    elif slovo.istitle():
      pocet_slov_s_velkym_pismenem += 1
  
  celkovy_pocet_slov = len(seznam_slov)
  print(f"{oddelujici_cara}\nText obsahuje {celkovy_pocet_slov} {sklonovat_slovo(celkovy_pocet_slov)}.",
      f"Text obsahuje {pocet_slov_s_velkym_pismenem} {sklonovat_slovo(pocet_slov_s_velkym_pismenem)} začínající velkým písmenem.",
      f"Text obsahuje {pocet_slov_psany_velkymi_pismeny} {sklonovat_slovo(pocet_slov_psany_velkymi_pismeny)} skládající se z velkých písmen.",
      f"Text obsahuje {pocet_slov_psany_malymi__pismeny} {sklonovat_slovo(pocet_slov_psany_malymi__pismeny)} skládající se z malých písmen.",
      sklonovat_cislo(pocet_cisel),
      f"Součet všech čísel je {soucet_cisel}.",
      oddelujici_cara,
      sep="\n")
          
def zobrazit_analyzu_textu_s_grafem(seznam_slov):
  analyza_textu(seznam_slov)
  
  pocet_delek_slov = dict()
  
  for slovo in seznam_slov:
    delka_slova_bez_spec_znaku = len(slovo.strip(".?!:,;"))
    if delka_slova_bez_spec_znaku in pocet_delek_slov.keys():
      pocet_delek_slov[delka_slova_bez_spec_znaku] += 1
    else:
      pocet_delek_slov[delka_slova_bez_spec_znaku] = 1
  
  print(f"DÉLKA| {'VÝSKYT':<20} |POČET", oddelujici_cara, sep="\n")
  for k, v in sorted(pocet_delek_slov.items()):
    hvezdny_graf = "*" * v
    print(f"{k:>5}| {hvezdny_graf:<20} |{v}")