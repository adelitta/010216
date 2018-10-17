sentence = input('Please enter message: ') 
words = sentence.split(" ")
pig = ""
vowels = "aeiouy"

for word in words:
	if word[0] in vowels:
			word = word + 'yay'
	else:
		i = 0

		for letter in word:
			if letter not in vowels:
				word = word + letter
				i += 1 
			else:
				break
		word = word[i:] + "ay "

	pig += word + " "
		
print(pig)
