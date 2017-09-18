def main():
	# define the function decode()
	def decode(text):
		if not text:
			return "\n"
		else:
			return text[0] * int(text[1]) + decode(text[2:])

	# get user input and print the result
	print("Text to decode: ")
	userInput = input()
	print("The result is: \n" + decode(userInput))


main()