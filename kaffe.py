pris = 0        #Her definerer jeg Pris og Mengde Kaffekopper som en int sånn at jeg kan bruke disse senere.
mengde_kaffekopper = 0

kaffetyper = {         #Her lagde jeg en ordliste med alle kaffetypene og hvor mye de er verdt så jeg kan bruke de etterpå
   "Espresso" : 2.50,
   "Americano" : 3.00,
   "Latte" : 2.50,
   "Cappuccino" : 3.00,
   "Macciato" : 2.50,
   "Mocha" : 3.50,
   "Flat White" : 2.50,
}

størrelse = {    #Her lagde jeg også en ordbok med størrelsene på koppene som jeg kan ta å bruke etterpå.
   "Medium" : 0.0,
   "Stor" : 1.0,
   "Ekstra Stor" : 1.50,
}

takeaway = {    #Her lagde jeg enda en ordbok med Ja og Nei som skal brukes til å spørre om du vil ha take away.
   "Ja" : 0.0,
   "Nei" : 1.0,
}

spørsmål = [      #Imotsettning til de andre ordbøkene så har jeg valgt å lagre spørsmålene i en liste. Dette er fordi det er bedre å bruke en liste om du skal hente ut inholdet etter hverandre. 
   "Hvor mange kopper skal du ha? ", "Hvilke kaffetype skal du ha? ", "Hvilke størreslse hvil du ha på koppen? ", "Take Away? " 
]




def program(liste1, liste2, liste3, liste4):    #Dette er selve programmet. Her definerer eg program med antall lister eg har som ligger øverst i koden.
   global mengde_kaffekopper, pris        #Her setter jeg de variablene helt øverst som en global for at de skal kunne brukes inne i en def.
   
   mengde_kaffekopper = int(input(spørsmål[0]))    #Det denne gjør er å spørre deg spørsmål med indexen 0, og venter på ditt input. Etter det lagrer den verdien i variablen mengde_kaffekopper som en int siden det skal være et helt tall. 
   
   
   print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
   print("+                               +")
   print("+         The Coffee Shop       +")
   print("+              Welcome          +")      #Dette er menyen til kaffen.
   print("+                               +")
   print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
   print("")
   print("We serve the following coffees:")
   print(" > Espresso")
   print(" > Americano")
   print(" > Latte")
   print(" > Cappuccino")
   print(" > Macchiato")
   print(" > Mocha")
   print(" > Flat White")
   print("----------------------------")
   
   
   for i in range(mengde_kaffekopper):    #Denne tar verdien som ble lagret i det første spørsmålet og kjører alt inni denne løkken flere ganger basert på hva du skrev inn i mengde_kaffekopper.
   
      type_kaffe = input(spørsmål[1]).title()      #Nå spør den deg om spørsmålet i listen som har en index på 1. og setter svaret til å ha stor forbokstav. dette skjer fordi det .title() funksjonen er på slutten av inputen.
      while type_kaffe not in kaffetyper:    #Så lenge det du skrev inn i spørsmålet over ikke ligger i ordboken kaffetyper, så sier den at de ikkje har den kaffetypen og spør deg samme spørsmål omigjen.
         print("Desverre så har vi ikkje denne kaffetypen i butikken.")
         type_kaffe = input(spørsmål[1]).title()
   
      kopp_størrelse = input(spørsmål[2]).title()     #Dette er litt det samme som kaffetype spørsmålet, men litt anderledes. Det du skriver blir lagret i kopp_størrelse
      if kopp_størrelse == "":      #Men denne har en "Om du ikkje skriver noe inn i spørsmålet om koppstørelse, så setter den koppstørelsen automatisk til medium."
         kopp_størrelse = "Medium"
      while kopp_størrelse not in størrelse:    #Denne er samme som while løkken over. 
         print("Denne størrelsen har vi ikkje. Velg mellom Medium(standard), Stor eller Ekstra Stor")
         kopp_størrelse = input(spørsmål[2]).title()
   
      spisested = input(spørsmål[3]).title()    #Det siste spørsmålet er akkuratt som det første. Den spør spørsmålet med indexen 3 i spørsmål listen og gjør at svaret har stor bokstav.
      while spisested not in takeaway:    #Sålenge svaret ikkje er ja eller nei så stiller han deg spørsmålet igjen.
         print("Svar med Ja eller Nei")
         spisested = input(spørsmål[3]).title()
   
      pris += kaffetyper[type_kaffe] + størrelse[kopp_størrelse] + takeaway[spisested]    #Her regner han ut prisen i til alle spørsmålene. den sier at pris plus type_kaffe som ligger inni kaffetyper og kopp_størrelse som er inni 
                                                                                          #størrelse og spisested som er inni takeaway er det samme som pris. Den gjør det på denne måten sånn at selv om den går gjennom koden
   print(f"dette kommer til å koste deg {pris}$")                                                                            #Flere ganger pågrunn av for løkken, så vill ikkje prisen fra den første gjennomgangen forsvinne mens den redefinerer segselv. 
              
      
program(kaffetyper, størrelse, takeaway, spørsmål)       #Denne er viktig fordi den kaller på funksjonen. Det er her du legger inn hvilke lister du bruker sånn at koden hvet hva (spørsmål[2]) er osv.




   
