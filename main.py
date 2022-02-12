x = int(input('Enter first variable:'))
fdsj = int(input('Enter second variable:'))
z = input("which to use (+-*/**):")

if z == "+":
	t = x + fdsj
elif z == "-":
	t = x - fdsj
elif z == "*":
	t = x * fdsj
elif z == "/":
	t = x / fdsj
elif z == "**":
  t = x ** fdsj
else:
	print("Error 404")
print("Your answer is {0}".format(t))
