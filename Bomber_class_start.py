from Bomber_own_class import Bomber

def super_bomb(a, b, c):
	print("Welcome to Bomber")
	count = a
	iteration = b
	Bomber.setnumber(c)
	for _ in range(count):
	    thread = Bomber(iteration)
	    thread.start()
	print("ALL PROCESSES WERE STARTED")

