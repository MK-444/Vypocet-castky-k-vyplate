hruba_mzda = int(input("Hrubá mzda: "))

zdravotni_pojisteni_podnik = hruba_mzda/100*9
print("Zdravotní pojištění podnik: " + str(int(zdravotni_pojisteni_podnik)))

socialni_pojisteni_podnik = hruba_mzda/100*24.8
print("Socialní pojištění podnik: " + str(int(socialni_pojisteni_podnik)))

zvyseni_zakladu_dane = 0
print("Zvýšení základu daně: " + str(int(zvyseni_zakladu_dane)))

dan_pred_slevami = hruba_mzda/100*15
print("Daň před slevami: " + str(int(dan_pred_slevami)))

sleva_na_poplatnika = 2320
print("Sleva na poplatnika: " + str(int(sleva_na_poplatnika)))

dan_po_sleve = dan_pred_slevami - sleva_na_poplatnika
print("Daň po slevě: " + str(int(dan_po_sleve)))


deti = int(input("Kolik děti?: "))
if deti == 0:
    sleva_na_deti = 0
elif deti == 1:
    sleva_na_deti = 1267
    print("Sleva na děti: " + str(int(sleva_na_deti)))
elif deti == 2:
    sleva_na_deti = 1267 + 1617
    print("Sleva na děti: " + str(int(sleva_na_deti)))
elif deti == 3:
    sleva_na_deti = 1267 + 1617 + 2017
    print("Sleva na děti: " + str(int(sleva_na_deti)))
elif deti == 4:
    sleva_na_deti = 1267 + 1617 + 2017 + 2017
    print("Sleva na děti: " + str(int(sleva_na_deti)))
elif deti == 5:
    sleva_na_deti = 1267 + 1617 + 2017 + 2017 + 2017
    print("Sleva na děti: " + str(int(sleva_na_deti)))


studenti = int(input("Kolik studentu?: "))
if studenti == 0:
    sleva_na_studenta = 0
    print("Sleva na studenta: " + str(int(sleva_na_studenta)))
elif studenti == 1:
    sleva_na_studenta = 335
    print("Sleva na studenta: " + str(int(sleva_na_studenta)))
elif studenti == 2:
    sleva_na_studenta = 335 + 335
    print("Sleva na studenta: " + str(int(sleva_na_studenta)))
elif studenti == 3:
    sleva_na_studenta = 335 + 335 + 335
    print("Sleva na studenta: " + str(int(sleva_na_studenta)))
elif studenti == 4:
    sleva_na_studenta = 335 + 335 + 335 + 335
    print("Sleva na studenta: " + str(int(sleva_na_studenta)))
elif studenti == 5:
    sleva_na_studenta = 335 + 335 + 335 + 335 + 335
    print("Sleva na studenta: " + str(int(sleva_na_studenta)))


dan_po_sleve_potom = dan_po_sleve - sleva_na_deti - sleva_na_studenta

if dan_po_sleve_potom > 0:
    dan_bonus = 0
    print("Daň po slevě: " + str(int(dan_po_sleve_potom)))
    print("Daň bonus: " + str(int(dan_bonus)))
    
elif dan_po_sleve_potom < 0:
    dan_bonus = abs(dan_po_sleve_potom)
    dan_po_sleve_potom = 0
    print("Daň po slevě: " + str(int(dan_po_sleve_potom)))
    print("Daň bonus: " + str(int(dan_bonus)))
    


zdravotni_pojisteni_zamestnanec = hruba_mzda/100*4.5
print("Zdravotní pojištění zaměstnanec: " + str(int(zdravotni_pojisteni_zamestnanec)))

socialni_pojisteni_zamestnanec = hruba_mzda/100*6.5
print("Socialní pojištění zaměstnanec: " + str(int(socialni_pojisteni_zamestnanec)))

ostatni_srazky  = int(input("Kolik srážek?: "))
print("Ostatní srážky: " + str(int(ostatni_srazky)))

cista_mzda = hruba_mzda - dan_po_sleve_potom - zdravotni_pojisteni_zamestnanec - socialni_pojisteni_zamestnanec + dan_bonus
print("Čistá mzda: " + str(int(cista_mzda)))

castka_k_vyplate = cista_mzda - ostatni_srazky
print("Častka k vyplatě: " + str(int(castka_k_vyplate)))
