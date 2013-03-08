#!/usr/bin/python

def pinmask(Pin):
	if Pin == 0:
		return 75
	elif Pin == 1:
		return 91
	elif Pin == 2:
		return 191
	elif Pin == 3:
		return 24
	elif Pin == 4:
		return 200
	elif Pin == 5:
		return 90
	elif Pin == 6:
		return 72
	elif Pin == 7:
		return 101 

def export(Pin_no):
	Pin = pinmask(Pin_no)
	print "Pin_Name %d" % Pin
	try:
		pinexport = open("/sys/class/gpio/export","w")
		pinexport.write(str(Pin))
		pinexport.close()
	except IOError:
		print "GPIO %d already Exists, skipping export gpio" % Pin

def setup(Pin_no, direction):
	Pin = pinmask(Pin_no)
	gpio_name = "gpio%s" % (str(Pin))
	pindir = open("/sys/class/gpio/"+gpio_name+"/direction", "w")
	if direction == 1:
		pindir.write("high")
	else:
		pindir.write("in")
	pindir.close()
	
def read(Pin_no):
	Pin = pinmask(Pin_no)
	gpio_name = "gpio%s" % (str(Pin))
	pinread = open("/sys/class/gpio/"+gpio_name+"/value", "r")
	output = pinread.read()
	pinread.close()
	return output

def write(Pin_no, value):
	Pin = pinmask(Pin_no)
	gpio_name = "gpio%s" % (str(Pin))
	pinwrite = open("/sys/class/gpio/"+gpio_name+"/value", "w")
	pinwrite.write(str(value))
	pinwrite.close()









