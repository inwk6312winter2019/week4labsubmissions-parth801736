from Lab5task1 import point
import copy

class rectangle:
	def __init__(self):
		self.width = 0
		self.height = 0
		self.corner = 0


def find_center(r):
	c = point()
	c.x = r.corner.x + r.width/2.0
	c.y = r.corner.y + r.height/2.0
	return c

def move_rectangle(r, dx, dy):
	r.corner.x += dx
	r.corner.y += dy

def new_move(r, dx, dy):
	res = copy.deepcopy(r)
	move_rectangle(res, dx, dy)
	return res


rect = rectangle()
rect.width = 40.0
rect.height = 80.0

rect.corner = point()
rect.corner.x = 0.0
rect.corner.y = 0.0

print('Center')
c = find_center(rect)

print('(%g, %g)' % (c.x,c.y))
print('')

print('(%g, %g)' % (rect.corner.x, rect.corner.y))
print('move')

move_rectangle(rect, 200, 100)
print('(%g, %g)' % (rect.corner.x, rect.corner.y))
print('')
print('New move')

n_rect = new_move(rect, 80, 160)
print('(%g, %g)' % (n_rect.corner.x, n_rect.corner.y))






	

