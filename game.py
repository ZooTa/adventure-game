import time
import random


def print_pause(text):
    print(text)
    time.sleep(2)


def print_pause_random(text):
    print(random.choice(text))
    time.sleep(2)


def game():
    print_pause("you are in your apartment alone.")
    print_pause("you are sleeping.")
    print_pause("it is so dark.")
    print_pause("you hear some sound.")
    choice_1()
    play_again()


def choice_1():
    choice1 = input("what will you do\n"
                    "1.agnoring it and complete your sleep\n"
                    "2.go to see what is happening\n")

    if "1" in choice1:
        zz = ["the next day, when you wake up you find your apartment ropped",
              "it turned out that they are thieves and they killed you"]
        print_pause_random(zz)

    elif "2" in choice1:
        print_pause("you find three thieves ropping you")
        choice_2()

    else:
        print_pause("i do not understand you")
        choice_1()


def choice_2():
    choice2 = input("what will you do\n"
                    "1.call the police\n"
                    "2.go to hide\n")
    if "1" in choice2:
        xx = ["the police come and cought them",
              "the heard you and get in your room and killed you"]
        print_pause_random(xx)

    elif "2" in choice2:
        print_pause("you find a knife")
        choice_3()

    else:
        print_pause("i do not understand you")
        choice_2()


def choice_3():
    choice3 = input("what will you do\n"
                    "1.trying to kill them\n"
                    "2.Continue hiding\n")

    if "1"in choice3:
        cc = ["great, you killed them",
              "you killed one\nand then the other two killed you",
              "while you thinking\nthey cought you and killed you"]
        print_pause_random(cc)

    elif "2" in choice3:
        print_pause("one of themgo to rop your room\n"
                    "after he finished he forgot his gun")
        choice_4()

    else:
        print_pause("i do not understand you")
        choice_3()


def choice_4():
    choice4 = input("what will you do\n"
                    "1.get the gun and try to kill them\n"
                    "2.Continue hiding\n")
    if "2" in choice4:
        aa = ["they ropped your apartment and you did not do any thing",
              "the police find you the next day killed becouse the"
              "thieves found you"]
        print_pause_random(aa)

    elif "1" in choice4:
        qq = ["great, you killed them",
              "you killed one\nand then the other killed you"]
        print_pause_random(qq)

    else:
        print_pause("i do not understand you")
        choice_4()


def play_again():
    choice = input("would you like to play again\n"
                   "yes\n"
                   "no\n")
    if "yes" in choice:
        print_pause("ok, here we go again")
        start_game()

    elif "no" in choice:
        print_pause("ok, goodbye")

    else:
        print_pause("i do not understand you")
        play_again()


def start_game():
    print_pause("you are playing a simulator game")
    game()


start_game()
