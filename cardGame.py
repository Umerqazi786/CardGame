from random import choice as select_card
import random


class CardGame:
    ''' Card game class which implements the card game with following rules:
        1. Number of players are from 2 to 4
        2. Deck consist of 56 cards. 52 ordinary cards and 4 penalty cards
        3. Game will grow on number of rounds until the top score reaches 21 and difference in score between top scorer and rest of the players is greater than 1
        4. Winner of the round will get two points and if any player draw penalty card, their score will decrease by 1, given player score is not zero'''
    def __init__(self, number_of_players):
        '''Initialize total number of players'''
        self.players = number_of_players

    def create_deck(self):
        '''Method to create deck of cards including four penalty cards. Returns list containing tuple for each card in format (value, suit) '''
        suit = ['Spade', 'Heart', 'Diamond', 'Club']
        deck = []                   # Initiating list to build deck. Each card is inserted in form of tuple with 0 index of tuple to be value and 1 index to be suit
        for i in range(1, 14):      # For loop for 13 different value cards
            for j in suit:          # For loop for 4 different suit for each value
                if i == 1:
                    deck.append(('Ace', j))
                elif i == 11:
                    deck.append(('Jack', j))
                elif i == 12:
                    deck.append(('Queen', j))
                elif i == 13:
                    deck.append(('King', j))
                else:
                    deck.append((i, j))
        for i in range(1, 5):       # For loop for 4 penalty-cards
            deck.append((0, 'Penalty-card'))

        return deck

    def random_card(self, deck):
        '''Method to  randomly select card out of the list of deck. '''
        return select_card(deck)

    def remove_deck_card(self, deck, card):
        '''Method to remove card from deck list after player has selected the card in each round so other players dont get the same card.'''
        deck.remove(card)

    def shuffle_deck(self, deck):
        '''Method to shuffle the deck after each round'''
        return random.shuffle(deck)

    def compare_cards(self, a, b):
        '''Compare the two cards according to value and suit and return true if 'a' is bigger than 'b' otherwise return false.
         If both players have penalty-card, method returns false. If both player has same card value than method checks for
         card with bigger suit and return boolean result accordingly. '''
        player_1_value, player_1_suit = a # Extracting value and suit from card 'a'.
        player_2_value, player_2_suit = b # Extracting value and suit from card 'b'.
        if player_2_suit == 'Penalty-card' and player_1_suit != 'Penalty-card': # If 'a' is not penalty card and 'b' is penalty-card.
            return True
        elif player_1_suit == 'Penalty-card' and player_2_suit != 'Penalty-card': # If 'b' is not penalty-card and 'a' is penalty-card.
            return False
        elif player_2_suit == 'Penalty-card' and player_1_suit == 'Penalty-card': # If both cards are penalty-card.
            return False
        # Below is the assignment according to value of card.
        if player_1_value == 'Ace':
            player_1_value = 14
        elif player_1_value == 'Jack':
            player_1_value = 11
        elif player_1_value == 'Queen':
            player_1_value = 12
        elif player_1_value == 'King':
            player_1_value = 13
        if player_2_value == 'Ace':
            player_2_value = 14
        elif player_2_value == 'Jack':
            player_2_value = 11
        elif player_2_value == 'Queen':
            player_2_value = 12
        elif player_2_value == 'King':
            player_2_value = 13
        if player_1_value > player_2_value: # If a value is
            return True
        elif player_2_value > player_1_value:
            return False
        elif player_1_value == player_2_value and (player_1_value != 0 and player_2_value != 0):
            if player_1_suit == 'Spade':
                return True
            elif player_2_suit == 'Spade':
                return False
            elif player_1_suit == 'Heart' and (player_2_suit == 'Diamond' or player_2_suit == 'Club'):
                return True
            elif player_2_suit == 'Heart' and (player_1_suit == 'Diamond' or player_1_suit == 'Club'):
                return False
            elif player_1_suit == 'Diamond' and player_2_suit == 'Club':
                return True
            elif player_2_suit == 'Diamond' and player_1_suit == 'Club':
                return False

    def two_players(self):
        '''Method to run two players game mode. Rules are same as described in class docstring.'''
        # Initiating score variable for each player.
        score_player_1 = 0
        score_player_2 = 0
        done = True
        i = 1
        while done: # While loop to keep game running until winner is called or user wants to quit.
            if score_player_1 <= 21 or score_player_2 <= 21 or abs(score_player_1 - score_player_2) == 1: # Logic statement according to game rules provided.
                x = CardGame.create_deck(self)
                CardGame.shuffle_deck(self, x)
                while True: # While loop to ask user to enter correct input to draw card.
                    player_1_input = input('Player-1 please press "n" to draw a card or press "q" to quit the game: ')
                    print()
                    if player_1_input == 'n' or player_1_input == 'N':
                        break
                    elif player_1_input == 'q' or player_1_input == 'Q':
                        done = False
                        break
                    else:
                        print('You did not press the right key. Try Again!')
                        print()
                if not done:
                    break
                player_1_card = CardGame.random_card(self, x) # Using random method to draw card from deck.
                player_1_value, player_1_suit = player_1_card # Extracting card value and suit from the drawn card.
                if player_1_suit != 'Penalty-card': # Printing the card on screen for other players to see.
                    print("Player-1 card is", player_1_value, 'of', player_1_suit)
                    print()
                else: # Printing penalty-card if drawn
                    print("Player-1 card is", player_1_suit)
                    print()

                CardGame.remove_deck_card(self, x, player_1_card) # Removing card from deck so same card is not available for same round
                player_2_card = CardGame.random_card(self, x)
                while True:
                    player_2_input = input('Player-2 please press "n" to draw a card or press "q" to quit game: ')
                    print()
                    if player_2_input == 'n' or player_2_input == 'N':
                        break
                    elif player_2_input == 'q' or player_2_input == 'Q':
                        done = False
                        break
                    else:
                        print('You did not press the right key. Try Again!')
                        print()
                if not done:
                    break
                player_2_value, player_2_suit = player_2_card
                if player_2_suit != 'Penalty-card':
                    print("Player-2 card is", player_2_value, 'of', player_2_suit)
                    print()
                else:
                    print("Player-2 card is", player_2_suit)
                    print()
                CardGame.remove_deck_card(self, x, player_2_card)
                if player_2_suit == 'Penalty-card': # Decreasing score by 1 if player draw a penalty-card given score is not zero already.
                    if score_player_2 == 0:
                        pass
                    else:
                        score_player_2 -= 1
                if player_1_suit == 'Penalty-card':
                    if score_player_1 == 0:
                        pass
                    else:
                        score_player_1 -= 1
                player_1 = CardGame.compare_cards(self, player_1_card, player_2_card) # Comparing cards to see which card is bigger.
                player_2 = CardGame.compare_cards(self, player_2_card, player_1_card)
                # Printing round winner after checking condition.
                if player_1:
                    score_player_1 += 2
                    print('Round-' + str(i), 'winner is Player-1')
                    print()
                elif player_2:
                    score_player_2 += 2
                    print('Round-' + str(i), 'winner is Player-2')
                    print()
                elif not player_1 and not player_2:
                    print('Round-' + str(i), 'is a tie. Both player picked Plenty-card')
                    print()
            print('         Total-Score      ')
            print('Player-1 |', score_player_1, '  ', 'Player-2 |', score_player_2)
            print()
            # Checking if all the conditions to win the game are met. If so, then announce the winner and print it out.
            if (score_player_1 >= 21 and abs(score_player_1 - score_player_2) > 1) or (
                    score_player_2 >= 21 and abs(score_player_1 - score_player_2) > 1):
                if score_player_1 > score_player_2:
                    print('Game winner is Player-1')
                    print()
                else:
                    print('Game winner is Player-2')
                    print()
                done = False
            i += 1
        while True: # While loop to ask user if they want to play another game
            input1 = input('Do you want to play another game. press "y" or "n": ')
            if input1 == 'y' or input1 == 'Y':
                print()
                main()
                break
            elif input1 == 'n' or input1 == 'N':
                print()
                print('Thank you for playing card game!')
                break
            else:
                print('You pressed wrong key. Try again!')

    def three_players(self):
        ''' Method to run three players game mode'''
        score_player_1 = 0
        score_player_2 = 0
        score_player_3 = 0
        done = True
        i = 1
        while done: # While loop to keep game running until conditions to win are met or player wants to quit.
            if score_player_1 <= 21 or score_player_2 <= 21 or score_player_3 <= 21 or abs(score_player_1 - score_player_2) <= 1 \
                    or abs(score_player_1 - score_player_3) <= 1 or abs(score_player_2 - score_player_3) <= 1: # Logic expression to keep running the game in
                x = CardGame.create_deck(self)                                                                 # three players mode until winner is declared
                CardGame.shuffle_deck(self, x)
                while True: # Asking player for input.
                    player_1_input = input('Player-1 please press "n" to draw a card or press "q" to quit the game: ')
                    print()
                    if player_1_input == 'n' or player_1_input == 'N':
                        break
                    elif player_1_input == 'q' or player_1_input == 'Q':
                        done = False
                        break
                    else:
                        print('You did not press the right key. Try Again!')
                        print()
                if not done:
                    break
                player_1_card = CardGame.random_card(self, x)
                player_1_value, player_1_suit = player_1_card
                if player_1_suit != 'Penalty-card':
                    print("Player-1 card is", player_1_value, 'of', player_1_suit)
                    print()
                else:
                    print("Player-1 card is", player_1_suit)
                    print()

                CardGame.remove_deck_card(self, x, player_1_card)
                while True:
                    player_2_input = input('Player-2 please press "n" to draw a card or press "q" to quit game: ')
                    print()
                    if player_2_input == 'n' or player_2_input == 'N':
                        break
                    elif player_2_input == 'q' or player_2_input == 'Q':
                        done = False
                        break
                    else:
                        print('You did not press the right key. Try Again!')
                        print()
                if not done:
                    break
                player_2_card = CardGame.random_card(self, x)
                player_2_value, player_2_suit = player_2_card
                if player_2_suit != 'Penalty-card':
                    print("Player-2 card is", player_2_value, 'of', player_2_suit)
                    print()
                else:
                    print("Player-2 card is", player_2_suit)
                    print()
                CardGame.remove_deck_card(self, x, player_2_card)
                while True:
                    player_3_input = input('Player-3 please press "n" to draw a card or press "q" to quit game: ')
                    print()
                    if player_3_input == 'n' or player_3_input == 'N':
                        break
                    elif player_3_input == 'q' or player_3_input == 'Q':
                        done = False
                        break
                    else:
                        print('You did not press the right key. Try Again!')
                        print()
                if not done:
                    break
                player_3_card = CardGame.random_card(self, x)
                player_3_value, player_3_suit = player_3_card
                if player_3_suit != 'Penalty-card':
                    print("Player-3 card is", player_3_value, 'of', player_3_suit)
                    print()
                else:
                    print("Player-3 card is", player_3_suit)
                    print()
                CardGame.remove_deck_card(self, x, player_3_card)
                if player_3_suit == 'Penalty-card': # Decreasing score by 1 if penalty card is drawn by the player.
                    if score_player_3 == 0:
                        pass
                    else:
                        score_player_3 -= 1
                if player_2_suit == 'Penalty-card':
                    if score_player_2 == 0:
                        pass
                    else:
                        score_player_2 -= 1
                if player_1_suit == 'Penalty-card':
                    if score_player_1 == 0:
                        pass
                    else:
                        score_player_1 -= 1
                player_1_2 = CardGame.compare_cards(self, player_1_card, player_2_card) # Compairing cards of each player to get the largest card
                player_2_1 = CardGame.compare_cards(self, player_2_card, player_1_card)
                player_1_3 = CardGame.compare_cards(self, player_1_card, player_3_card)
                player_3_1 = CardGame.compare_cards(self, player_3_card, player_1_card)
                player_2_3 = CardGame.compare_cards(self, player_2_card, player_3_card)
                player_3_2 = CardGame.compare_cards(self, player_3_card, player_2_card)
                if player_1_2 and player_1_3: # Checking conditions for round winner.
                    print('Round-' + str(i), 'winner is Player-1')
                    print()
                    score_player_1 += 2
                elif player_2_1 and player_2_3:
                    print('Round-' + str(i), 'winner is Player-2')
                    print()
                    score_player_2 += 2
                elif player_3_1 and player_3_2:
                    print('Round-' + str(i), 'winner is Player-3')
                    print()
                    score_player_3 += 2
                elif not player_1_2 and not player_2_1 and not player_1_3 and not player_3_1 and not player_2_3 and not player_3_2:
                    print('Round' + str(i), 'is a tie. All three players picked Plenty-card')
                    print()

            print('                Total-Score                         ')
            print('Player-1 |', score_player_1, '  ', 'Player-2 |', score_player_2, ' ', 'Player-3 |', score_player_3)
            print()
            high_score = 0
            # Conditions for game winner
            if score_player_1 >= score_player_2 and score_player_1 >= score_player_3:
                high_score = score_player_1
            elif score_player_2 >= score_player_1 and score_player_2 >= score_player_3:
                high_score = score_player_2
            elif score_player_3 >= score_player_1 and score_player_3 >= score_player_2:
                high_score = score_player_3
            if high_score == score_player_1 and high_score >= 21:
                if abs(high_score - score_player_2) > 1 and abs(high_score - score_player_3) > 1:
                    print('Game winner is Player-1')
                    print()
                    done = False
            elif high_score == score_player_2 and high_score >= 21:
                if abs(high_score - score_player_1) > 1 and abs(high_score - score_player_3) > 1:
                    print('Game winner is Player-2')
                    print()
                    done = False
            elif high_score == score_player_3 and high_score >= 21:
                if abs(high_score - score_player_1) > 1 and abs(high_score - score_player_2) > 1:
                    print('Game winner is Player-3')
                    print()
                    done = False
            i += 1
        while True: # While loop to ask users if they want to play another game
            input1 = input('Do you want to play another game. press "y" or "n": ')
            if input1 == 'y' or input1 == 'Y':
                print()
                main()
                break
            elif input1 == 'n' or input1 == 'N':
                print()
                print('Thank you for playing card game!')
                break
            else:
                print('You pressed wrong key. Try again!')

    def four_players(self):
        '''Method to run game mode with four players'''
        score_player_1 = 0
        score_player_2 = 0
        score_player_3 = 0
        score_player_4 = 0
        done = True
        i = 1
        while done: # While loop and logical condition for the game to run in four players mode.
            if score_player_1 <= 21 or score_player_2 <= 21 or score_player_3 <= 21 or score_player_4 <= 21 or abs(
                    score_player_1 - score_player_2) \
                    <= 1 or abs(score_player_1 - score_player_3) <= 1 or abs(
                score_player_1 - score_player_4) <= 1 or abs(
                score_player_2 - score_player_3) <= 1 \
                    or abs(score_player_2 - score_player_4) <= 1 or abs(score_player_3 - score_player_4) <= 1:
                x = CardGame.create_deck(self)
                CardGame.shuffle_deck(self, x)
                while True: # Asking player for keyboard input to draw card.
                    player_1_input = input('Player-1 please press "n" to draw a card or press "q" to quit the game: ')
                    print()
                    if player_1_input == 'n' or player_1_input == 'N':
                        break
                    elif player_1_input == 'q' or player_1_input == 'Q':
                        done = False
                        break
                    else:
                        print('You did not press the right key. Try Again!')
                        print()
                if not done:
                    break
                player_1_card = CardGame.random_card(self, x)
                player_1_value, player_1_suit = player_1_card
                if player_1_suit != 'Penalty-card':
                    print("Player-1 card is", player_1_value, 'of', player_1_suit)
                    print()
                else:
                    print("Player-1 card is", player_1_suit)
                    print()

                CardGame.remove_deck_card(self, x, player_1_card)
                while True:
                    player_2_input = input('Player-2 please press "n" to draw a card or press "q" to quit game: ')
                    print()
                    if player_2_input == 'n' or player_2_input == 'N':
                        break
                    elif player_2_input == 'q' or player_2_input == 'Q':
                        done = False
                        break
                    else:
                        print('You did not press the right key. Try Again!')
                        print()
                if not done:
                    break
                player_2_card = CardGame.random_card(self, x)
                player_2_value, player_2_suit = player_2_card
                if player_2_suit != 'Penalty-card':
                    print("Player-2 card is", player_2_value, 'of', player_2_suit)
                    print()
                else:
                    print("Player-2 card is", player_2_suit)
                    print()
                CardGame.remove_deck_card(self, x, player_2_card)
                while True:
                    player_3_input = input('Player-3 please press "n" to draw a card or press "q" to quit game: ')
                    print()
                    if player_3_input == 'n' or player_3_input == 'N':
                        break
                    elif player_3_input == 'q' or player_3_input == 'Q':
                        done = False
                        break
                    else:
                        print('You did not press the right key. Try Again!')
                        print()
                if not done:
                    break
                player_3_card = CardGame.random_card(self, x)
                player_3_value, player_3_suit = player_3_card
                if player_3_suit != 'Penalty-card':
                    print("Player-3 card is", player_3_value, 'of', player_3_suit)
                    print()
                else:
                    print("Player-3 card is", player_3_suit)
                    print()
                CardGame.remove_deck_card(self, x, player_3_card)
                while True:
                    player_4_input = input('Player-4 please press "n" to draw a card or press "q" to quit game: ')
                    print()
                    if player_4_input == 'n' or player_4_input == 'N':
                        break
                    elif player_4_input == 'q' or player_4_input == 'Q':
                        done = False
                        break
                    else:
                        print('You did not press the right key. Try Again!')
                        print()
                if not done: # If player wants to quit, break the while loop.
                    break
                player_4_card = CardGame.random_card(self, x)
                player_4_value, player_4_suit = player_4_card
                if player_4_suit != 'Penalty-card':
                    print("Player-4 card is", player_4_value, 'of', player_4_suit)
                    print()
                else:
                    print("Player-4 card is", player_4_suit)
                    print()
                CardGame.remove_deck_card(self, x, player_4_card)
                if player_4_suit == 'Penalty-card': # Checking for penalty-cards and decreasing score by 1.
                    if score_player_4 == 0:
                        pass
                    else:
                        score_player_4 -= 1
                if player_3_suit == 'Penalty-card':
                    if score_player_3 == 0:
                        pass
                    else:
                        score_player_3 -= 1
                if player_2_suit == 'Penalty-card':
                    if score_player_2 == 0:
                        pass
                    else:
                        score_player_2 -= 1
                if player_1_suit == 'Penalty-card':
                    if score_player_1 == 0:
                        pass
                    else:
                        score_player_1 -= 1
                player_1_2 = CardGame.compare_cards(self, player_1_card, player_2_card) # Comparing cards to check for largest card.
                player_1_3 = CardGame.compare_cards(self, player_1_card, player_3_card)
                player_1_4 = CardGame.compare_cards(self, player_1_card, player_4_card)
                player_2_1 = CardGame.compare_cards(self, player_2_card, player_1_card)
                player_2_3 = CardGame.compare_cards(self, player_2_card, player_3_card)
                player_2_4 = CardGame.compare_cards(self, player_2_card, player_4_card)
                player_3_1 = CardGame.compare_cards(self, player_3_card, player_1_card)
                player_3_2 = CardGame.compare_cards(self, player_3_card, player_2_card)
                player_3_4 = CardGame.compare_cards(self, player_3_card, player_4_card)
                player_4_1 = CardGame.compare_cards(self, player_4_card, player_1_card)
                player_4_2 = CardGame.compare_cards(self, player_4_card, player_2_card)
                player_4_3 = CardGame.compare_cards(self, player_4_card, player_3_card)
                if player_1_2 and player_1_3 and player_1_4: # Printing round winner
                    print('Round-' + str(i), 'winner is Player-1')
                    print()
                    score_player_1 += 2
                elif player_2_1 and player_2_3 and player_2_4:
                    print('Round-' + str(i), 'winner is Player-2')
                    print()
                    score_player_2 += 2
                elif player_3_1 and player_3_2 and player_3_4:
                    print('Round-' + str(i), 'winner is Player-3')
                    print()
                    score_player_3 += 2
                elif player_4_1 and player_4_2 and player_4_3:
                    print('Round-' + str(i), 'winner is Player-4')
                    print()
                    score_player_4 += 2
                elif not player_1_2 and not player_1_3 and not player_1_4 and not player_2_1 and not player_2_3 \
                        and not player_2_4 and not player_3_1 and not player_3_2 and not player_3_4 and not player_4_1 \
                        and not player_4_2 and not player_4_3: # If all 4 players draw penalty-card.
                    print('Round' + str(i), 'is a tie. All four players picked Plenty-card')
                    print()

            print('                       Total-Score                                   ') #Printing out total score after each round
            print('Player-1 |', score_player_1, '  ', 'Player-2 |', score_player_2, ' ', 'Player-3 |', score_player_3,
                  ' ',
                  'Player-4 |', score_player_4)
            print()
            high_score = 0 # Conditions to check game winner.
            if score_player_1 >= score_player_2 and score_player_1 >= score_player_3 and score_player_1 >= score_player_4:
                high_score = score_player_1
            elif score_player_2 >= score_player_1 and score_player_2 >= score_player_3 and score_player_2 >= score_player_4:
                high_score = score_player_2
            elif score_player_3 >= score_player_1 and score_player_3 >= score_player_2 and score_player_3 >= score_player_4:
                high_score = score_player_3
            elif score_player_4 >= score_player_1 and score_player_4 >= score_player_2 and score_player_4 >= score_player_3:
                high_score = score_player_4
            if high_score == score_player_1 and high_score >= 21:
                if abs(high_score - score_player_2) > 1 and abs(high_score - score_player_3) > 1 and abs(
                        high_score - score_player_4) > 1:
                    print('Game winner is Player-1')
                    print()
                    done = False
            elif high_score == score_player_2 and high_score >= 21:
                if abs(high_score - score_player_1) > 1 and abs(high_score - score_player_3) > 1 and abs(
                        high_score - score_player_4) > 1:
                    print('Game winner is Player-2')
                    print()
                    done = False
            elif high_score == score_player_3 and high_score >= 21:
                if abs(high_score - score_player_1) > 1 and abs(high_score - score_player_2) > 1 and abs(
                        high_score - score_player_4) > 1:
                    print('Game winner is Player-3')
                    print()
                    done = False
            elif high_score == score_player_4 and high_score >= 21:
                if abs(high_score - score_player_1) > 1 and abs(high_score - score_player_2) > 1 and abs(
                        high_score - score_player_3) > 1:
                    print('Game winner is Player-4')
                    print()
                    done = False
            i += 1
        while True:
            input1 = input('Do you want to play another game. press "y" or "n": ')
            if input1 == 'y' or input1 == 'Y':
                print()
                main()
                break
            elif input1 == 'n' or input1 == 'N':
                print()
                print('Thank you for playing card game!')
                break
            else:
                print('You pressed wrong key. Try again!')


def main():
    '''Function to control the game modes according to player input'''
    while True: # While loop to ask user to enter digit from 2 to 4 to play different game modes. Loops until user enters the valid input
        try:
            print()
            number_of_players = int(input("Please enter number of players participating (minimum 2 and maximum 4): "))
            print()
            if 2 <= number_of_players <= 4:
                break
            else:
                print()
                print('You entered wrong number of players. Please try again!')
        except ValueError:
            print()
            print('You did not enter digit. Please try again!')
    if number_of_players == 2: # Two players mode.
        game = CardGame(number_of_players)
        game.two_players()
    elif number_of_players == 3:  # Three players mode
        game = CardGame(number_of_players)
        game.three_players()
    elif number_of_players == 4: # Four players mode
        game = CardGame(number_of_players)
        game.four_players()

if __name__ == '__main__':
    print("         Welcome to the card game         ")
    main()
