import sys

dumb = False
try:
    from rich.console import Console
    from rich.table import Table
    from rich import box
except ImportError:
    dumb = True

if not dumb:
    def print_card(card):
        def render(x):
            return '[bold red]X[/bold red]' if x == -1 else str(x)
        console = Console()
        table = Table(show_header=False, box=box.DOUBLE_EDGE, show_lines=True)
        for i in range(5):
            table.add_row(*[render(x) for x in card[i]])
        console.print(table)
else:
    def print_card(card):
        print("-" * 15)
        for i in range(5):
            print(*card[i])
        print("-" * 15)

def check_card(card_id) -> bool:
    f = flags[card_id]
    # check rows
    for i in range(5):
        if all(f[i]):
            return True

    # check columns
    ft = list(zip(*f))
    for i in range(5):
        if all(ft[i]):
            return True

    return False

def solve():
    # which cards have won?
    has_won = [False for _ in range(len(deck))]

    for num in numbers:
        for i, card in enumerate(deck):
            for row in range(5):
                for col in range(5):
                    if card[row][col] == num:
                        flags[i][row][col] = True

            won = check_card(i)
            if won and not has_won[i]:
                has_won[i] = True
                # len([ j for j in range(len(deck)) if has_won[j] ])
                num_wins = len(list(filter(None, has_won)))
                if num_wins == 1 or num_wins == len(deck):
                    score = 0
                    for row in range(5):
                        for col in range(5):
                            if not flags[i][row][col]:
                                score += card[row][col]
                    print(f"Card #{i+1} wins:")
                    print_card(card)
                    print(f"Score = {score * num}\n")

if __name__ == "__main__":
    fp = sys.stdin

    line = fp.readline()
    numbers = [int(num) for num in line.strip().split(',')] # numbers to draw

    card = [] # a single card
    deck = [] # the deck of cards
    flags = [] # drawn/not-drawn flags for each card

    # read the input
    while True:
        line = fp.readline()
        if line and line != '\n':
            card.append([int(x) for x in line.strip().split()])
        else:
            if card:
                deck.append(card)
            card = []
            if line == '':
                break

    # initially, the flags of each number in each card is False
    for card in deck:
        flags.append([[False for _ in range(5)] for _ in range(5)])
    
    # solve part 1 & part 2
    solve()
