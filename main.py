import sys, re, json, random

#comment
try:
	deck_file = open(sys.argv[1], 'r')
except IndexError:
	print "No file passed"
	sys.exit(0)

jsonData = open("./res/AllCards.json")
cardData = json.load(jsonData)

costArray = [0 for i in range(8)]
totalCards = 0
cardList = []

lines = deck_file.readlines()
for cards in lines:
	info = re.split('(\d+)', cards.strip())
	num = int(info[1])
	totalCards += num
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
		if not cardData[name]["type"].startswith("Basic Land"):
			costArray[0] += num
	for i in range(0, num):
		cardList.append(name)
for i in range(0, len(costArray)):
	if i == 7:
		print str(i) + "+: " + str(costArray[i])
	else:
		print str(i) + ": " + str(costArray[i])

print "Sample hand:"
for i in range(0, 7):
	print cardList[random.randint(0, totalCards-1)]
