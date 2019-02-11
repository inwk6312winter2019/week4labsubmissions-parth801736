class Time:
	def __init__(self):
		self.hour = 0
		self.minute = 0
		self.second = 0
	
def print_time(time):
	#print("%.2d:%.2d:%.2d"(time.hour,time.minute,time.second))
    print('{}:{:02}:{:02}'.format(time.hour, time.minute, time.second))
time = Time()
time.hour = 5
time.minute = 25
time.second = 15
print_time(time)
