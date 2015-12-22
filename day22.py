import inputs, random, math

class Spell:
	def __init__(self, name, cost, turns, effect):
		self.name = name
		self.cost = cost
		self.turns = turns
		self.effect = effect

class Player: 
	LEASTSPELLCOST = 53

	def __init__(self, hp, mana):
		self.hp = hp
		self.mana = mana
		self.defense = 0

	def hasenoughmana(self):
		return self.mana >= self.LEASTSPELLCOST

	def isdead(self): 
		return self.hp <= 0

class Boss: 
	def __init__(self, hp, dmg):
		self.hp = hp
		self.dmg = dmg

	def isdead(self):
		return self.hp <= 0

class Game: 
	boss = ''
	player = ''
	activespells = {}
	turnnumber = 0
	manaused = 0
	logs = ''
	tolog = False

	def __init__(self, boss, player, log):
		self.boss = boss
		self.player = player
		self.activespells = {}
		self.turnnumber = 1
		self.logs = ''
		self.tolog = log

	def bossattack(self):
		dmg = max(self.boss.dmg - self.player.defense, 0)
		self.player.hp -= dmg
		if self.player.hp <= 0: 
			return False
		self.log('Boss attacks! {0} damage taken'.format(dmg))
		self.turnnumber +=1
		return True


	def playercast(self, spell):
		if spell.name in self.activespells.keys(): 
			self.log('{0} is already casted'.format(spell.name))
			return False
		if self.player.mana < spell.cost:
			self.log('Player does not have enough mana to cast {0}!'.format(spell.name))
			return False

		self.log('Player casts {0}'.format(spell.name))
		if spell.turns > 0: 
			self.activespells[spell.name] = (spell.turns, spell.effect)
		else:
			self.castspell(spell.name, spell.effect)
		self.player.mana -= spell.cost
		self.manaused += spell.cost
		self.turnnumber += 1
		return True


	def applyEffects(self):
		for spell in self.activespells: 
			t, effects = self.activespells[spell]
			self.castspell(spell, effects)
			self.activespells[spell] = (t - 1, effects)
			self.log('{0} has {1} turns left'.format(spell, t-1))
		self.activespells = { k:v for k, v in self.activespells.items() if v[0] > 0 }
		
	def castspell(self, name, effect):
		for t, e in effect:
			if t == 'd':
				self.log(' {0} deals {1} damange'.format(name, e))
				self.boss.hp -= e
			elif t == 'h':
				self.log(' {0} heals {1} hp'.format(name, e))
				self.player.hp += e
			elif t == 'a':
				if self.activespells[name][0] == 1:
					self.log(' {0} effects ending, armor no longer valid'.format(name))
					self.player.defense	 = 0
				else:
					self.log(' {0} gives you {1} armor'.format(name, e))
					self.player.defense = e
			elif t == 'r':
				self.log(' {0} provides {1} mana'.format(name, e))
				self.player.mana += e

	def isplayerturn(self): 
		return self.turnnumber % 2

	def isgameover(self): 
		return self.boss.isdead() or self.player.isdead()

	def log(self, message):
		if self.tolog: 
			self.logs += message + '\n'
		else:
			print(message)

def day22(ishuman, log): 
	drain = Spell('Drain', 73, 0, [('d', 2), ('h', 2)])
	missle = Spell('Magic Missle', 53, 0, [('d', 4)])
	shield = Spell('Sheild', 113, 6, [('a', 7)])
	poison = Spell('Poison', 173, 6, [('d', 3)])
	recharge = Spell('Recharge', 229, 5, [('r', 101)])

	spells = {'d': drain, 'm':missle, 's':shield, 'p':poison, 'r':recharge}
	
	
	
	minmanause = math.inf
	while True:
		boss = Boss(58, 9)
		player = Player(50, 500)
		game = Game(boss, player, log)

		while not game.isgameover(): 
			if game.isplayerturn(): 
				game.log('---Players turn---')
				game.player.hp -= 1
				if game.player.isdead(): 
					break
				game.applyEffects()
				game.log('- Player has {0} hit points, {1} armor, {2} mana'.format(game.player.hp, game.player.defense, game.player.mana))
				game.log('- Boss has {0} hit points'.format(game.boss.hp))
				if game.boss.isdead():
					break
				if game.player.hasenoughmana():
					
					spellcasted = False
					while not spellcasted: 
						if ishuman:
							spell_ = input('Please choose spell to cast: [d]rain, [m]issle, [s]hield, [p]oison, [r]echarge: ')
							spell = spells[spell_]
						else:
							spell = random.choice([missle, drain, shield, poison, recharge])
						spellcasted = game.playercast(spell)
				else:
					game.log('Player has no more mana. GAME OVER')
					break
			else:
				game.log('---Bosss turn---')
				game.log('- Player has {0} hit points, {1} armor, {2} mana'.format(game.player.hp, game.player.defense, game.player.mana))
				game.log('- Boss has {0} hit points'.format(game.boss.hp))
				game.applyEffects()
				game.bossattack()

		print('total mana used is {0}'.format(game.manaused))
		game.log('total mana used is {0}'.format(game.manaused))
		if game.boss.isdead():
			game.log('boss dead')
			if game.manaused < minmanause: 
				showlog =input('log?')
				if showlog == 'y':
					print(game.logs)
				tocontinue = input('continue?')
				if tocontinue == 'x':
					break
				minmanause = game.manaused
		elif game.player.isdead():
			game.log('player dead')
	print('least mana used to win is', minmanause)
	return

day22(False, True)