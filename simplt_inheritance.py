class Animal:
	cool = True

	def make_sound(self, sound):
		return f"I will {sound}"

class Cat(Animal):
	pass

blue = Cat()
# print(blue.cool)
# print(blue.make_sound('meow'))

print(isinstance(blue,Animal))