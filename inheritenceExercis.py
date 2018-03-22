class Character:

	def __init__(self, name, hp, level):
		self.name = name
		if hp >= 1:
			self.hp = hp
		else:
			raise ValueError('hp cannot be less than 1.')
		if level >= 1 and level <= 15:
			self._level = level
		else:
			raise ValueError('select levels from 1 to 15.')

	def __repr__(self):
		return f"My name is {self.name}"

	@property
	def level(self):
		return self._level

	@level.setter
	def level(self, new_level):
		if new_level >= 1 and new_level <= 15:
			self._level = new_level
		else:
			raise ValueError('select levels from 1 to 15.')

class NPC(Character):

	def __init__(self, name, hp, level):
		super().__init__(name, hp, level)

	def speak(self):
		return "I heard there were monsters running around last night!"

villager = NPC('Bob', 10, 12)
print(villager.name)
print(villager.hp)
print(villager.level)
print(villager.speak())

# print('Level: ',villager.level)
# villager.level = 7
# print('New Level: ',villager.level)





