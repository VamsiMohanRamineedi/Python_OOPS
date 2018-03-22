class Mother:
	eye_color = 'brown'
	hair_color = 'dark brown'
	hair_type = 'curly'

class Father:
	eye_color = 'blue'
	hair_color = 'blond'
	hair_type = 'straight'

class Child(Mother, Father):
	pass

# c = Child()
# print(c.eye_color)

help(Child)
