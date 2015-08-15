import sys, re, json

try:
	deck_file = open(sys.argv[1], 'r')
except IndexError:
	print "No file passed"
	sys.exit(0)

jsonData = open("./res/AllCards.json")
cardData = json.load(jsonData)

costArray = [0 for i in range(8)]

lines = deck_file.readlines()
for cards in lines:
	info = re.split('(\d+)', cards.strip())
	num = int(info[1])
	name = info[2]
	if name[0] == ' ':
		name = name[1:]
	try:
		card_cost = int(cardData[name]["cmc"])
		if card_cost > 7:
			card_cost = 7
		costArray[card_cost] += num
	except KeyError:
		#contnues if the card has no cost
		costArray[0] += num
		continue 
print costArray
