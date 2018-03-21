import random
random.seed(0)
class Card:

	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __repr__(self):
		return f"{self.value} of {self.suit}"


class Deck:

	def __init__(self):

		self.cards = []

		suits = ['Hearts','Diamonds','Clubs','Spades']
		values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
		# for i in suits:
		# 	for j in values:
		# 		card = Card(i,j)
		# 		self.cards.append(card)
		self.cards = [Card(suit, value) for suit in suits for value in values]
		# print('Init method \n')
		# print('Type of self.cards is ', type(self.cards))
		# print('\n')
		# print('Length of self.cards is ', len(self.cards))

	def __repr__(self):
		return f"Deck of {len(self.cards)} cards"

	def count(self):
		return len(self.cards)

	def _deal(self, number):
		if len(self.cards) == 0:
			raise ValueError("All cards have been dealt")

		min_value = min(number,len(self.cards))
		sampled = random.sample(self.cards,k = number)
		self.cards = [x for x in self.cards if x not in sampled]
		return sampled

	def shuffle(self):

		if len(self.cards) == 52:
			self.cards = random.sample(self.cards, k = len(self.cards))
			# print('\n In shuffle method, cards = ', self.cards)
			return self

		else:
			raise ValueError("Only full decks can be shuffled")

	def deal_card(self):
		return self._deal(1)[0]

	def deal_hand(self, number):
		return self._deal(number)

if __name__ == '__main__':
	my_deck = Deck()
	# print(my_deck)
	# my_deck.shuffle()
	# card = my_deck.deal_card()
	# print(card)
	# hand = my_deck.deal_hand(5)
	# print(hand)
	# print(my_deck)
	print(my_deck._deal(52))
	print(my_deck.count())
	print(my_deck._deal(3))


