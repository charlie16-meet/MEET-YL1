class Animal:
	def __init__(self,name,color,age,size):
		self.name=name 
		self.color=color
		self.age=age
		self.size=size
	def print_all(self):
		print(self.name)
		print(self.color)
		print(self.age)
		print(self.size)


dog = Animal(name="max",color="black",age=4,size="huge")
cat = Animal(name="min",color="white",age=2,size="tiny")

dog.print_all()
print("##################")

cat.print_all()
