def main():
	# define the function encode()
	def encode(text):
		if not text:
			return "\n"
		else:
			i = 1
			while i < len(text) and text[0] == text[i]:
				i += 1
			return text[0] + str(i) + encode(text[i:])

	# get user input and print the result
	print("Text to encode: ")
	userInput = input()
	print("The result is: \n" + encode(userInput))


main()