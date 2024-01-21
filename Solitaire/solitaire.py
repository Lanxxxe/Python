import random


class Card:
    def __init__(self, shape, rank, open=False):
        self.shape = shape
        self.rank = rank
        self.open = open

    def color(self):
        return 'Red' if self.shape in ['H', 'D'] else 'Black'

    def __str__(self):
        return "{}{}".format(self.shape, self.rank) if self.open else "[]"


class Solitaire:
    def __init__(self):
        self.piles = [[] for _ in range(7)]
        self.stock = []
        self.foundations = [[] for _ in range(4)]
        self.initialize_game()

    def initialize_game(self):
        shapes = ['H', 'D', 'c', 's']
        ranks = ['A', '2', '3', '4', '5', '6',
                 '7', '8', '9', 'T', 'J', 'Q', 'K']
        deck = [Card(shape, rank, open=False)
                for shape in shapes for rank in ranks]
        random.shuffle(deck)

        for x in range(7):
            self.piles[x] = deck[x * (x + 1) // 2:][:x + 1]

        for pile in self.piles:
            if pile:
                pile[-1].open = True

        # self.bottom_card = Card("XX", " ", open = False) # XX if empty

    def print_game_screen_layout(self):
        print("S O L I T A I R E")
        if self.stock:
            print("S: ", str(self.stock[0]))
        else:
            print("S: []   A: {}   B: {}   C: {}   D: {}".format(*('XX' if not card else str(card) for card in self.foundations)))  # print the foundation and stock

        print(":    ".join(str(i)for i in range(1, 8)))  # number on top of cards
        # max num of cards in each pile
        max_pile_height = max(len(pile) for pile in self.piles)
        # every row in the range starts from 1, then will add 1 to the height
        for row in range(1, max_pile_height + 1):
            row_str = ""
            for pile in self.piles:
                if row <= len(pile):
                    # adds the string of the card at position row-1 in the current pile
                    row_str += f"{pile[row-1]}    "
                else:
                    row_str += "      "  # maintain allignment
            print(row_str.rstrip())

    # Ito ung part na inayos ko, inayos ko ung conditions.

    def move_card(self, from_pile_index, target_pile_index):
        if target_pile_index.upper() == 'A' or target_pile_index.upper() == 'B' or target_pile_index.upper() == 'C' or target_pile_index.upper() == 'D':
            from_pile_index = int(from_pile_index) - 1
            # target_pile_index = int(target_pile_index) - 1

            # Get the source pile and target pile based on the provided indices
            from_pile = self.piles[from_pile_index]
            # target_pile = self.piles[target_pile_index]

            if target_pile_index.upper() == 'A':#Checks if the list in null
                    if len(self.foundations[0]) != 0:
                        if ord(self.foundations[0][-1][1]) > ord(from_pile[-1].rank): #Checks if the source card is lower then the card in the foundation
                            if (self.foundations[0][-1][1].islower() != from_pile[-1].shape.islower() or self.foundations[0][-1][1].isupper() != from_pile[-1].shape.isupper()): #checks the type of the card
                                self.foundations[0].append(str(from_pile[-1]))
                                self.piles[int(from_pile_index)].pop()
                                if from_pile:
                                    from_pile[-1].open = True
                        else:
                            print("Invalid. Cannot be put in the foundation")
                            self.print_game_screen_layout()
                    else:      
                        self.foundations[0].append(str(from_pile[-1]))
                        self.piles[int(from_pile_index)].pop()
                        if from_pile:
                            from_pile[-1].open = True
            elif target_pile_index.upper() == 'B':
                    if len(self.foundations[1]) != 0:#Checks if the list in null
                        if ord(self.foundations[1][-1][1]) > ord(from_pile[-1].rank): #Checks if the source card is lower then the card in the foundation
                            if (self.foundations[1][-1][1].islower() != from_pile[-1].shape.islower() or self.foundations[1][-1][1].isupper() != from_pile[-1].shape.isupper()): #checks the type of the card
                                self.foundations[1].append(str(from_pile[-1]))
                                self.piles[int(from_pile_index)].pop()
                                if from_pile:
                                    from_pile[-1].open = True
                        else:
                            print("Invalid. Cannot be put in the foundation")
                            self.print_game_screen_layout()
                    else:      
                        self.foundations[1].append(str(from_pile[-1]))
                        self.piles[int(from_pile_index)].pop()
                        if from_pile:
                            from_pile[-1].open = True
            elif target_pile_index.upper() == 'C':
                    if len(self.foundations[2]) != 0: #Checks if the list in null
                        if ord(self.foundations[2][-1][1]) > ord(from_pile[-1].rank): #Checks if the source card is lower then the card in the foundation
                            if (self.foundations[2][-1][1].islower() != from_pile[-1].shape.islower() or self.foundations[2][-1][1].isupper() != from_pile[-1].shape.isupper()): #checks the type of the card
                                self.foundations[2].append(str(from_pile[-1]))
                                self.piles[int(from_pile_index)].pop()
                                if from_pile:
                                    from_pile[-1].open = True
                        else:
                            print("Invalid. Cannot be put in the foundation")
                            self.print_game_screen_layout()
                    else:      
                        self.foundations[2].append(str(from_pile[-1]))
                        self.piles[int(from_pile_index)].pop()
                        if from_pile:
                            from_pile[-1].open = True
            elif target_pile_index.upper() == 'D':
                    if len(self.foundations[3]) != 0: #Checks if the list in null
                        if ord(self.foundations[3][-1][1]) > ord(from_pile[-1].rank): #Checks if the source card is lower then the card in the foundation
                            if (self.foundations[3][-1][1].islower() != from_pile[-1].shape.islower() or self.foundations[3][-1][1].isupper() != from_pile[-1].shape.isupper()):
                                self.foundations[3].append(str(from_pile[-1]))
                                self.piles[int(from_pile_index)].pop()
                                if from_pile:
                                    from_pile[-1].open = True
                        else:
                            print("Invalid. Cannot be put in the foundation")
                            self.print_game_screen_layout()
                    else:      
                        self.foundations[3].append(str(from_pile[-1]))
                        self.piles[int(from_pile_index)].pop()
                        if from_pile:
                            from_pile[-1].open = True

        else:
            from_pile_index = int(from_pile_index) - 1
            target_pile_index = int(target_pile_index) - 1

            # Get the source pile and target pile based on the provided indices
            from_pile = self.piles[from_pile_index]
            target_pile = self.piles[target_pile_index]

            # Check if the provided pile indices are valid
            if not self.valid_pile(from_pile_index) or not self.valid_pile(target_pile_index):
                print("Invalid pile index.")
                return self.print_game_screen_layout()
            # Check if the source pile is empty or the top card is not open
            # elif not from_pile or not from_pile[-1].open:
            #     print("Invalid move. No open card in the source pile.")
            #     return self.print_game_screen_layout()

            # Check if the move is valid according to the game rules
            elif self.valid_move(from_pile, target_pile):
                # Move the last card from the source pile to the target pile
                target_pile.append(from_pile[-1])

                print(f"Moved {from_pile[-1]} from pile {from_pile_index + 1} to pile {target_pile_index + 1}.")
                # Remove the top card from the source pile
                from_pile.pop()
                # If the source pile is not empty, open the top card
                if from_pile:
                    from_pile[-1].open = True
                self.print_game_screen_layout()  # Print updated game screen layout
            
            else:
                print("Invalid move. Card cannot be moved to the target pile.")


    # Nag set ako ng conditions dito,
    def valid_pile(self, pile_index):
        # convert pile_index into integer
        # return True if both conditions meet, return False naman kung isa lang or walang na meet na condition
        return 0 <= int(pile_index) and int(pile_index) < int(len(self.piles))

    def deal_stock(self):
        if not self.stock:
            print("Stock is empty.")
            return

        held_card = self.stock.pop(0)  # get top card
        foundation_index = int(input("Choose foundation (A-D) to move the card: ")) - 1

        # if valid, move
        if self.valid_move(held_card, self.foundations[foundation_index]):
            self.foundations[foundation_index].append(held_card)
        else:
            print("Invalid move. Card cannot be moved to the foundation.")

        row_index = int(input("Choose row (1-7) to move the card: ")) - 1
        if self.valid_move(held_card, self.piles[row_index]):
            self.piles[row_index].append(held_card)
        else:
            print("Invalid move. Card cannot be moved to the row.")

    def valid_move(self, source_pile, target_pile):
        if not target_pile:  # If the target pile is empty, any card can be placed
            return True
        elif source_pile[-1].rank == 'K':
            return False  # Cannot move a King (K) to another pile
        elif target_pile[-1].shape.isupper() == source_pile[-1].shape.isupper() or target_pile[-1].shape.islower() == source_pile[-1].shape.islower():
            return False
        elif target_pile[-1].open and source_pile[-1].rank == 'A':
            return True  # Can move an Ace (A) to an open pile
        elif source_pile[-1].rank == 'J' and target_pile[-1].rank == 'Q' or source_pile[-1].rank == 'Q' and target_pile[-1].rank == 'K':
            return True  # Can move a Jack (J) to a Queen (Q) or Can move a Queen (Q) to a King (K)
        elif source_pile[-1].rank == 'T' and target_pile[-1].rank == 'J':
            return True  # Can move a 10 to a Jack (J)
        elif ord(source_pile[-1].rank) == ord(target_pile[-1].rank) - 1:
            return True  # Can move a card one rank lower to an open pile
        elif ord(source_pile[-1].rank) < ord(target_pile[-1].rank):
            return True
        else:
            return False  # Invalid move

    def load_game(self, file_name):
        with open(file_name, 'r') as file:  # 'r' = read
            lines = file.readlines()  # read all lines of file into lines

        self.stock = [Card(card[0], card[1:]) for card in lines[0].split()[
            1:]]  # get stock from first line

        for i in range(1, 7):
            pile_cards = [Card(card[0], card[1:])
                          for card in lines[i].split()[2:]]  # card info per pile
            self.piles[i - 1] = pile_cards  # assign to i-1 (excluded)
            if pile_cards:
                pile_cards[-1].open = True  # if pile has cards, open the last

        for i in range(8, 11):  # foundation
            foundation_cards = [Card(card[0], card[1:])
                                for card in lines[i].split()[1:]]
            self.foundations[i - 8] = foundation_cards


def play():
    game = Solitaire()

    while True:
        game.print_game_screen_layout()

        # Displays the menu of the game.
        print("Menu:")
        print("[1] Move")
        print("[2] Deal")
        print("[3] Save")
        print("[4] Load")
        print("[CTRL-C] Exit")

        user = input("Enter choice: ").upper()  # Gets user's input.

        if user == '1':
            # Gets user's input.
            hold_pile_index = input("Source pile index: ")
            # Gets user's input.
            target_pile_index = input("Target pile index: ")
            game.move_card(hold_pile_index, target_pile_index)
        elif user == '2':
            game.deal_stock()
        elif user == '3':
            file_name = input("Enter filename to save: ").upper()
            print("Saved!")
        elif user == '4':
            print("Load")
        elif user == 'E':
            break
        else:
            # If the user inputs other character/s.
            print("Invalid choice. Please try again.")


play()
