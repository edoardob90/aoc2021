import sys

fp = sys.stdin

line = fp.readline()
numbers = [int(num) for num in line.strip().split(',')] # numbers to draw

card = [] # single card
deck = [] # deck of cards

while True:
    line = fp.readline()
    if line and line != '\n':
        # read line of card
        card.extend([int(x) for x in line.strip().split()])
    else:
        if card:
            deck.append(card)
        card = []
        if line == '':
            break

def print_card(card):
    print('-'*15)
    for i in range(1, 6):
        print(*card[5*(i-1):5*i])
    print('-'*15, end='\n\n')

def draw(card, number) -> None:
    """Mark a number on a card as drawn"""
    if number in card:
        card[card.index(number)] = 'X'

def check_deck() -> bool:
    """Check if an entire row or column has been drawn from a card of the deck"""
    X = ['X'] * 5
    if deck:
        for j, card in enumerate(deck):
            for i in range(5):
                row = card[5 * i:5 * (i+1)] # take the i-th row
                col = card[i::5] # take the i-th column
                if row == X or col == X:
                    return (True, j)
    return (False, None)

print(f"Num cards read: {len(deck)}\n")
# for i, c in enumerate(deck):
#     print(f"card #{i}:")
#     print_card(c)

def solve_p1():
    # print_card(deck[51])
    for i, num in enumerate(numbers, start=1):
        for card in deck:
            draw(card, num)
        if i >= 5:
            won, win_card = check_deck()
            if won:
                last_num = num
                print(f"At round #{(i // 5) + 1} card {win_card+1} has won!")
                break

    print_card(deck[win_card])

    print("\nScore = {}".format(last_num * sum(filter(lambda x: x != 'X', deck[win_card]))))

if __name__ == "__main__":
    solve_p1()

