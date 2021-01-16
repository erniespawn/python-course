import random

print "Nice card game to learn Class"




class Card(object):

	def __init__(self, suit, val):
		self.suit = suit
		self. value = val

	def show(self):
		print "{} of {}".format(self.value, self.suit)




class Deck(object):
	def __init__(self):
		self.cards = []
		self.build()

	def build(self):
		for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
				for v in range(1, 14):
					self.cards.append(Card(s, v))

	def show(self):
		for c in self.cards:
			c.show()

	def shuffle(self):
			for i in range(len(self.cards)-1, 0, -1):
				r = random.randint(0,i)
				self.cards[i], self.cards[r] = self.cards[r], self.cards[i]


class Player(object):
	pass
 



card = Card("Clubs", 6)
card.show()

deck = Deck()
deck.show()
deck.shuffle()
deck.show()