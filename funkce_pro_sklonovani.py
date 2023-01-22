def sklonovat_slovo(pocet_slov):
  if pocet_slov == 1:
    return "slovo"
  elif pocet_slov > 1 and pocet_slov < 5:
    return "slova"
  else:
    return "slov"
  
def sklonovat_cislo(pocet):
  if pocet == 0:
    return "Text neobsahuje žádné číslo."
  else:
    if pocet == 1:
      sklonovane_cislo = "číslo"
    elif pocet > 1 and pocet < 5:
      sklonovane_cislo = "čísla"
    else:
      sklonovane_cislo = "čísel"
  return f"Text obsahuje {pocet} {sklonovane_cislo}."

def vokativ(jmeno_uzivatele):
  if jmeno_uzivatele.endswith("b"):
    jmeno_uzivatele += "e"
  elif jmeno_uzivatele.endswith("n") or jmeno_uzivatele.endswith("z"):
    jmeno_uzivatele += "o"
  elif jmeno_uzivatele.endswith("e"):
    jmeno_uzivatele += "u"
  
  return jmeno_uzivatele