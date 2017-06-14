#Converts text provided by user into Brainfuck
#Input can be anything in ASCII range
intext=raw_input("Enter your text:")
limiter='+'*10
print limiter
print '[',
for i in intext:
	loop=ord(i)/10
	print '>',
	for j in range(0,loop):
		print '+',
#Iterate to first cell
for i in range(0,len(intext)):
	print '<',
print '-]'

#Adding remaining value to existing cells
for i in intext:
	remain=ord(i)%10
	print '>',
	for j in range(0,remain):
		print '+',
for i in range(0,len(intext)):
	print '<',

#Print value to output
for i in range(0,len(intext)):
	print '>.'