auswahl = input("Rezept auswählen (1, 2, 3):")
portion = input("Wähle die Anzahl der Portionen aus")
portions = int(portion)
print("(1) Pfannkuchen",
      "(2) Waffeln",
      "(3) Käsekuchen")
print("")
print("")

for Pfannkuchen in [str("Pfannkuchen"),
                    str(""),
                    str(portions * 2) + " Eier",
                    str(portions * 200) + "ml Milch",
                    str(portions * 100) + "g Milch",
                    str(portions * 0.5) + " Prise(n) Salz",
                    str(portions * 0.5) + " Msp. Backpulver",
                    str("Öl zum Backen")]:
    if auswahl == "1":
        print(Pfannkuchen)

for Waffeln in   [  str("Waffeln"),
                    str(""),
                    str(portions * 500) + "g Zucker",
                    str(portions * 500) + "g Margarine, zimmerwarm",
                    str(portions * 10) + " Eier",
                    str(portions * 2) + "Pck. Vanillinzucker",
                    str(portions * 1) + " Schuss Rum",
                    str(portions * 1000) + "g Mehl",
                    str(portions * 1) + "l Milch",
                    str(portions * 1) + "Pck. Backpulver"]:
       
    if auswahl == "2":
        print(Waffeln)

for Käsekuchen in [ str("Käsekuchen"),
                    str(""),
                    str("Für den Knetteig:"),
                    str(""),
                        str(portions * 200) + "g Mehl",
                        str(portions * 75) + "g Zucker",
                        str(portions * 75) + "g Margarine",
                        str(portions * 1) + " Ei(er)",
                        str(portions * 0.5) + "Pck. Backpulver",
                        str("Fett für die Form"),
                        str(""),
                    str("Für die Füllung:"),
                    str(""),
                        str(portions * 125) + "g Margarine",
                        str(portions * 225) + "g Zucker",
                        str(portions * 1) + "Pck Vanillezucker",
                        str(portions * 1) + "Pck Vanillepudding",
                        str(portions * 3) + " Eier",
                        str(portions * 500) + "g Quark (1 Becher)",
                        str(portions * 200 ) + "g saure Sahne (1 Becher)",
                        str(portions * 200) + "g süße Sahne (1 Becher)"]:
    
    if auswahl == "3":
        print(Käsekuchen)

print("")
input("Zum beenden beliebige Taste drücken...!")

