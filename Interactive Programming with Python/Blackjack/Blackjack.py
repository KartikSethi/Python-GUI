# open the following link to see the code in action: 
# http://www.codeskulptor.org/#save2_sD3fyx1DFm.py

# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
message = ""
score = 0
player_hand_value = 0
dealer_hand_value = 0
stand_clicked = False


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    global stand_clicked
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        if pos[1] == 200 and pos[0] == 50 and in_play:
            card_loc = (CARD_BACK_CENTER[0] , CARD_BACK_CENTER[1])
            canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        else:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        

# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cards = []

    def __str__(self):
        # return a string representation of a hand
        string = ""
        for i in range(len(self.cards)):
                       string += str(self.cards[i]) + " "
        return "Hand contains " + string
        
    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card) 

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0
        have_Ace = False
        for card in self.cards:
            hand_value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                have_Ace = True
        if not have_Ace:
            return hand_value
        else:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value   
              
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        i = 0
        for card in self.cards:
            card.draw(canvas, [pos[0] + 100 * i, pos[1]])
            i += 1

# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.deck.append(card)
            
    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return(self.deck.pop())
        
        
    def __str__(self):
        # return a string representing the deck
        string_deck = ""
        for i in range(len(self.deck)):
            string_deck += str(self.deck[i]) + " "
        return "Deck contains " + string_deck


#define event handlers for buttons
def deal():
    global outcome, in_play, my_deck, dealer_hand, player_hand, outcome, message, score, dealer_hand_value, player_hand_value
    

    # your code goes here
    if not in_play:
        print ""
        stand_clicked = False
        message = "Hit or Stand?"
        outcome = ""
        my_deck = Deck()
        dealer_hand = Hand()
        player_hand = Hand()
        in_play = True
        my_deck.shuffle()
        
        for i in range(2):
            dealer_hand.add_card(my_deck.deal_card())
        dealer_hand_value = dealer_hand.get_value()
    
        for i in range(2):
            player_hand.add_card(my_deck.deal_card())
        player_hand_value = player_hand.get_value()
        
    else:
        message = "New Deal?"
        outcome = "Player loses."
        score -= 1
        in_play = False


    

def hit():
    # replace with your code below
    global player_hand_value, in_play, dealer_hand_value, outcome, message, score
    # if the hand is in play, hit the player
    if in_play:
        message = "Hit or Stand?"
        player_hand.add_card(my_deck.deal_card())
        player_hand_value = player_hand.get_value()
        dealer_hand_value = dealer_hand.get_value()
        
        
    # if busted, assign a message to outcome, update in_play and score
        if player_hand_value > 21:
            outcome = "Player went bust and loses."
            message = "New Deal?"
            score -= 1
            in_play = False
def stand():
    # replace with your code below
    global player_hand_value, in_play, dealer_hand_value, outcome, message, score, stand_clicked
    is_busted = False
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        stand_clicked = True
        while dealer_hand_value < 17:
            dealer_hand.add_card(my_deck.deal_card())
            dealer_hand_value = dealer_hand.get_value()
            if dealer_hand_value > 21:
                message = "New Deal?"
                outcome = "Dealer went bust and Player wins."
                in_play = False
                is_busted = True
                score += 1
                return
        if not is_busted:
            if player_hand_value <= dealer_hand_value:
                outcome = "Player loses."
                score -= 1
                
            else:
                outcome = "Player wins."
                score += 1
                
                
        # assign a message to outcome, update in_play and score
        
        in_play = False
        message = "New Deal?"
        
        
        
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    #card = Card("S", "A")
    #card.draw(canvas, [50, 400])
    canvas.draw_text('Blackjack', [80, 100], 50, 'Aqua', 'serif')
    canvas.draw_text('Score : ' + str(score), [380, 100], 35, 'Black', 'sans-serif')
    canvas.draw_text('Player', [50, 380], 25, 'Black', 'sans-serif')    
    canvas.draw_text(message, [200, 380], 25, 'Black', 'sans-serif')
    player_hand.draw(canvas, [50, 400])
    canvas.draw_text('Dealer', [50, 180], 25, 'Black', 'sans-serif')
    canvas.draw_text(outcome, [200, 180], 25, 'Black', 'sans-serif')
    dealer_hand.draw(canvas, [50, 200])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# Please leave valuable comments.