import os
logo = """
  ######            ######                             ######                             
  #    #            #    #                             #    #                             
  #    #  #     #   #       #######  #######  #     #  #    #   #######  #######  #     # 
 #######  #     #  ##       #     #  #     #  #    #   #######  #     #  #     #  #    #  
 ##       #######  ##       #     #  #     #  #####    ##    #  #     #  #     #  #####   
 ##             #  ##    #  #     #  #     #  #    #   ##    #  #     #  #     #  #    #  
 ##       #######  #######  #######  #######  #     #  #######  #######  #######  #     # 

                                                                  
"""
# úvodní menu
print(logo)
print("Vítejte v PyCookBook! Co chcete dělat?")
print()
print()
print('1: Vytvořit recept')
print('2: Najít recept')
print()
print('Zadej číslo pro výběr možnosti: ')
volba = input()

# výběr možností
if volba == "1":
        os.system('cls')
        print(logo)
        print('Do jaké kategorie mám recept zařadit?')
        print()
        print()
        print('1: Bezmasá jídla')
        print('2: Maso')
        print('3: Ryby')
        print('4: Polévky')
        print('5: Saláty')
        print('6: Sladká jídla')
        print('7: Přílohy')
        print('8: Omáčky')
        print('9: Předkrmy')
        print('10: Moučníky')
        input()

elif volba == "2":
        os.system('cls')
        print(logo)
        print('najdi recept')
        input()

else:
    os.system('cls')
    print(logo)
    print('Tato možnost není na výběr. Stisknutím jakékoliv klávesy PyCookBook vypnete.')
    input()
