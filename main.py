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
                    str("Öl zum Backen"),
                    str(""),
                    str("Zubereitung:"),
                    str(""),
                    str("Gesamtzeit ca. 45 Minuten"),           
                    str(""),
                    str("Die Eier mit dem Zucker cremig aufschlagen, dann mit der Milch verrühren. Nun Salz, Mehl und Backpulver dazugeben und alles zu einem glatten Teig rühren."),
                    str(""),
                    str("Danach den Teig für ca. 15 Minuten ruhen lassen, da das Mehl noch ausquillt. Dann 1 - 2 große Schöpfkellen Teig in eine auf mittlere Hitze erhitzte, beschichtete Pfanne geben."),
                    str(""),
                    str("Nach ca. 2 Minuten bilden sich kleine Bläschen, dann den Pfannkuchen einmal wenden und von der anderen Seite schön goldbraun ausbacken."),
                    str(""),
                    ]:
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
                    str(portions * 1) + "Pck. Backpulver",
                    str(""),
                    str("Zubereitung:"),
                    str(""),
                    str("Gesamtzeit ca. 55 Minuten (Für ca. 30 Waffeln)."),
                    str(""),
                    str("Die verquirlten Eier mit dem Zucker und der Margarine glatt verrühren, bis ein schaumiger Teig entsteht. Vanillezucker und einen guten Schuss echten Rum hinzufügen."),
                    str(""),
                    str("1000 g Mehl und das Backpulver dazugeben und verrühren, dadurch wird der Teig etwas klebrig."),
                    str(""),
                    str("Zuletzt nach und nach die Milch unterrühren und so lange rühren, bis der Teig eine glatte und weiche Konsistenz hat."),
                    str(""),
                    str("In einem heißen Waffeleisen die Waffeln portionsweise backen und heiß servieren."),
                    str(""),
                    ]:
       
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
                        str(portions * 200) + "g süße Sahne (1 Becher)",
                    str(""),
                    str("Zubereitung:"),
                    str(""),
                    str("Gesamtzeit ca. 1 Stunde 30 Minuten"),
                    str(""),
                    str("Die Zutaten für den Knetteig in eine Schüssel geben, rasch zusammenkneten und zur Seite stellen."),
                    str(""),
                    str("Für die Füllung Margarine, Zucker, Vanillezucker, Puddingpulver und Eier in einer Schüssel verrühren. Dann den Quark und die saure Sahne untermischen. Die süße Sahne steif schlagen und unterheben."),
                    str(""),
                    str("Den Backofen auf 180 °C Ober-/Unterhitze vorheizen."),
                    str(""),
                    str("Den Knetteig in einer gefetteten 26er Springform auslegen, etwa 2 - 3 cm am Rand hochziehen. Nun die Füllung in die Form geben, glatt streichen und im heißen Backofen 1 Stunde backen."),
                    str(""),
                    str("Achtung: Den Kuchen erst nach dem völligen Erkalten aus der Form nehmen, da unmittelbar nach dem Herausnehmen aus dem Backofen die Konsistenz der Quarkmasse noch zu weich ist."),
                    str(""),
                        ]:
    
    if auswahl == "3":
        print(Käsekuchen)

print("")
input("Zum beenden beliebige Taste drücken...!")

