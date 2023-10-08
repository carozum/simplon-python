def rps(p1, p2):
    r = "rock"
    p = 'paper'
    s = "scissors"

    if p1 == p2:
        return "Draw!"
    elif (p1 == s and p2 == p) or (p1 == r and p2 == s) or (p1 == p and p2 == r):
        return "Player 1 won!"
    else:
        return "Player 2 won!"
