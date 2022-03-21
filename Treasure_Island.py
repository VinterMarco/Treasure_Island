import time

logo = '''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
 '''
welcome = "Welcome to the Treasure Island\nYou're mission is to find the treasure!"
shark_logo = '''



                                |.
                               ::.
                               :::
              ___              |::
             `-._''--.._       |::
                 `-._   `-._  .|::
                    `-._    `-::::
                       `.     |:::.
                         )    |::`:"-._ 
                       <'   _.7  ::::::`-,.._
                        `-.:        `` '::::::".
                        .:'       .    .   `::::)
                      .:'        .           .:::}
                   _.:'    __          .     :::/
     ,-.___,,..--'' --.""``  ``"".-- --,.._____.-.
    ((   ___ """   -- ...     ....   __  ______  (D
     "-'`   ```''-.  __,,.......,,__      ::.  `-"
                   `<-....,,,,....-<   .:::'
                     "._       ___,,._:::(
                        ::--=''       `\:::.
                       / :::'           `\::.
                      / ::'               `\::
                     / :'                   `\:
                    ( /                       `"
                     "

'''
death = '''

               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO)
       ::::::;       ;          OOOOO)
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#


'''

treasure = '''
__________________
    .-'  \ _.-''-._ /  '-.
  .-/\   .'.      .'.   /\-.
 _'/  \.'   '.  .'   './  \='_
:======:======::======:======:  
 '. '.  \     ''     /  .' .'
   '. .  \   :  :   /  . .'
     '.'  \  '  '  /  '.'
       ':  \:    :/  :'
         '. \    / .'
           '.\  /.'    
             '\/'

'''

monsters = '''



       -"")
    .-"  .`)     (
   j   .'_+     :[                )      .^--..
  i    -"       |l                ].    /      i
 ," .:j         `8o  _,,+.,.--,   d|   `:::;    b
 i  :'|          "88p;.  (-."_"-.oP        \.   :
 ; .  (            >,%%%   f),):8"          \:'  i
i  :: j          ,;%%%:; ; ; i:%%%.,        i.   `.
i  `: ( ____  ,-::::::' ::j  [:```          [8:   )
<  ..``'::::8888oooooo.  :(jj(,;,,,         [8::  <
`. ``:.      oo.8888888888:;%%%8o.::.+888+o.:`:'  |
 `.   `        `o`88888888b`%%%%%88< Y888P""'-    ;
   "`---`.       Y`888888888;;.,"888b."""..::::'-'
          "-....  b`8888888:::::.`8888._::-"
             `:::. `:::::O:::::::.`%%'|
              `.      "``::::::''    .'
                `.                   <
                  +:         `:   -';
                   `:         : .::/
                    ;+_  :::. :..;;;       
                    ;;;;,;;;;;;;;,;;


'''
print(logo)
time.sleep(2)
print(welcome)
time.sleep(2)
players_name = str(input("What is your name?: "))
print(f"OK {players_name}, let's begin! ")
time.sleep(2)

while True:
    choice_1 = str(input("You start at a crossroad, where do you want to go? [ Type: 'left' or 'right' ] ").lower())
    if choice_1 == 'left':
        choice_2 = str(input("You've come to a lake. There is an island in the middle of the lake.[Type 'wait' - to wait for a boat or 'swim' - to swim across the lake]")).lower()
        if choice_2 == 'wait':
            choice_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue.\nWhich colour do you chose").lower()
            if choice_3 == "red":
                print(death)
                time.sleep(2)
                print("It's a room full of fire.You died!")
                time.sleep(2)
                print("GAME OVER")
            elif choice_3 == "yellow":
                print(treasure)
                time.sleep(3)
                print("You found the treasure.You are rich for life.")
                time.sleep(1)
                print(f'Congratulations, {players_name}!!!!!!!')

            elif choice_3 == "blue":
                print("It's a room full of mosters.You fought them for hours, but in the end...")
                time.sleep(1)
                print(monsters)
                time.sleep(2)
                print('You died!')
                time.sleep(2)
                print('GAME OVER')
            else:
                print("You died because you did not respect the rules!")
                time.sleep(2)
                print("GAME OVER!")
        else:
            print(shark_logo)
            time.sleep(2)
            print("You got eaten by sharks")
            time.sleep(1)
            print("GAME OVER")

    else:
        print("You fell into a hole.Game over!")

    play_again = input("Play again ? [y/n]: ")
    if play_again.lower() != "y":
        break
