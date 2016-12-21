import random

def main():
	Game = BlackjackGame()
	while(boolResponse('Start new game? (y/n)')):
		Game.startNewGame()
	
class BlackjackGame():
	def __init__(self):
		self.deck = []
		self.Dealer = Player()
		self.Player = Player()
		
	def startNewGame(self):
		self.refreshAndShuffleDeck()
		self.resetPlayer(self.Player)
		self.resetPlayer(self.Dealer)
		self.dealCard(self.Player)
		self.dealCard(self.Player)
		self.dealCard(self.Dealer)
		self.dealCard(self.Dealer)
		playerHitting = True
		while(playerHitting):
			print("Dealers hand: ?, ", self.Dealer.hand[1:])
			print("Your hand: ", self.Player.hand)
			print("Your hand value: ", self.Player.handValue)
			
			if(boolResponse('Hit?: ')):
				self.dealCard(self.Player)
			else:
				playerHitting = False
				
			print(self.Player.hand)
			print(self.Player.handValue)
			
			if(self.Player.handValue > 21):
				print('Bust!')
				playerHitting = False
				self.Player.handValue = 0
			elif(self.Player.handValue == 21):
				playerHitting = False
				
		if(self.Player.handValue <= 21):		
			while(self.Dealer.handValue < self.Player.handValue):
				self.dealCard(self.Dealer)
				
			print("Dealers hand: ", self.Dealer.hand)
			print("Dealers hand value: ", self.Dealer.handValue)
				
			if(self.Dealer.handValue > 21):
				print('Dealer busts! You win!')
			elif(self.Dealer.handValue > self.Player.handValue):
				print('Dealer wins')
			elif(self.Dealer.handValue == self.Player.handValue):
				print('Tie')
			else:
				print('You win!')
				
		else:
			print('Dealer wins')
				
	def refreshAndShuffleDeck(self):
		suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
		cards = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']
		for suit in suits:
			for card in cards:
				self.deck.append(card + ' of ' + suit)
		random.shuffle(self.deck)
		
	def resetPlayer(self, player):
		player.hand = []
		player.handValue = 0
		player.numHighAces = 0
		
	def dealCard(self, player):
		card = self.deck.pop()
		player.hand.append(card)
		cardValue = self.analyzeCard(card)
		if(cardValue == 11):
			player.numHighAces += 1
		player.handValue += cardValue
		self.evalAces(player)
		
	def evalAces(self, player):
		if(player.handValue > 21):
			if(player.numHighAces != 0):
				player.handValue -= 10
				player.numHighAces -= 1
			
	def analyzeCard(self, card):
		cardValues = {
				'Jack': 10,
				'Queen': 10,
				'King': 10,
					}
		card = card.split(' ')
		if card[0] in cardValues:
			cardValue = cardValues[card[0]]
		elif card[0] == 'Ace':
			cardValue = 11
		else:
			cardValue = int(card[0])
		return cardValue
		
	
class Player():
	def __init__(self):
		self.money = 5000
		self.hand = []
		self.handValue = 0
		self.numHighAces = 0
		
class Dealer():
	def __init__(self):
		self.hand = []
		self.handValue = 0
		self.numHighAces = 0

			
def boolResponse(string):
	while(1==1):
		response = input(string)
		if(response == 'y' or response == 'Y'):
			return True
		elif(response == 'n' or respone == 'N'):
			return False


if __name__ == '__main__':
	main()