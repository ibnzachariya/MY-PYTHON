print(r'''                       _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# choice1 = input('You\'re at a crossroad, do you want to go "left" or "right".\n').lower()
# # \ used as an escape. .lower() used to ignore casing for inputs
# if choice1 == "left":
#     choice2 = input('You\'ve come to a lake. There\'s an Island in the middle of the lake. Type "wait" to wait for a boat or type "swim" to swim.\n').lower()
#     if choice2 == "wait":
#         choice3 = input("You arrived at the Island unharmed. There is a house with 3 doors. One red, one yellow, one blue. which do you choose?\n").lower()
#         if choice3 == "red":
#             print("You enter a room of fire, Game Over")
#         elif choice3 == "yellow":
#             print("You found the treasure, You Win")
#         elif choice3 == "blue":
#             print("You enter a room of beasts, Game Over")
#         else:
#             print("Room doesn't exist, Game Over")
#     else:
#         print("You fucked up, Game Over")
#
# else:
#     print("oops, you fell into a hole, Game Over")
print("Welcome to Life Path.\nYour mission is to make heaven")
choice1 = input('Are you "Human" or "Not Human"\n').lower()

if choice1 == 'human':
    choice2 = input('Are you a "believer" or a "disbeliver"\n').lower()
    if choice2 == 'believer':
        choice3 = input("Believe in all branches, Y/N?\n").lower()
        if choice3 == 'y':
            pick1 = input("Belief in all branches, Y/N?\n").lower()
            if pick1 == 'y':
                pick2 = input("Do you put into implementation? Y/N?\n").lower()
                if pick2 == 'y':
                    print("Ma sha Allah, You win")
                else:
                    print("What a pity, Game Over")
            else:
                print("Oops, Game Over")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Not for You, Game Over")