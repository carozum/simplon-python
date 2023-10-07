"""
Exercice 2 : le jeu du plus ou moins
"""

from random import randint

# ****** Function that check if a number input by user meets the requirements


def check_input(num, tries, sup):
    while True:
        try:
            num = int(num)
            if num > sup or num < 0:
                raise ValueError(
                    f"\nThe number must be between 0 and {sup}. \nTry again. ")
        except ValueError as err:
            if 'base 10' in str(err):
                num = input(
                    "\nPlease be sure to enter a number. \nTry again:  ")
            else:
                num = input(err)
        else:
            tries += 1
            return num, tries


# ****************** function that displays the stats for all the games


def display_stats(games):
    average = sum(games) / len(games)
    games.sort()
    min = games[0]
    max = games[len(games)-1]
    return (f"""
        \nAverage tries: {average}
        \rMin number of tries: {min}
        \rMax number of tries {max}""")


# ********* function that asks for the level of game chosen


def ask_level():
    print(
        f"""There are different levels of your difficulty: 
    \r - A to guess a number between 0 and 10
    \r - B to guess a number between 0 and 50
    \r - C to guess a number between 0 an 100
    """)
    level = input('Select your level: ')
    if level.upper() == "A":
        sup = 10
    elif level.upper() == 'B':
        sup = 50
    else:
        sup = 100
    return sup


# ************** function that plays a game
def guess_num(games, sup):

    guess = randint(1, sup)
    print(guess)

    num = input(f"\nEnter a number between 0 and {sup}: ")
    num, tries = check_input(num, 0, sup)

    still_playing = True

    while still_playing:
        if num > guess:
            num = input("\nToo high.\nTry again: ")
            num, tries = check_input(num, tries, sup)

        elif num < guess:
            num = input("\nToo low. \nTry again: ")
            num, tries = check_input(num, tries, sup)
        else:
            games.append(tries)
            print(f"""
        \nGREAT!!! You have guess the number {guess} after {tries} tries
        \r {display_stats(games)}
        \n*****************************""")
            want_to_play = input("\nDo you want to play again ? Y/N ")
            if want_to_play.upper() != "Y":
                return "See you next time"
            else:
                sup = ask_level()
                guess_num(games, sup)


def main():
    print(
        f"""*****************************
    \n
    \rEXERCICE 2 - Guessing game
    """)
    sup = ask_level()
    games = []
    print(guess_num(games, sup))


if __name__ == "__main__":
    main()
