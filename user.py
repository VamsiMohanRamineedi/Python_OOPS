#simple class definition
class User:
	
	def __init__(self):
		self.name = 'Vamsi'
		self._age = 25
		self.__city = 'Hyderabad'

user1 = User()
print(f'Name: {user1.name}')
print(f'Age: {user1._age}')
print(f'City: {user1._User__city}')
#print(dir(user1))