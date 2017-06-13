# Count It!
import operator
import sys
# Read in the File


file = open(sys.argv[1], "r")
txt = file.read()
file.close()

# Count the words

words = {}

for word in txt.split():
	if word.lower() in words:
		words[word.lower()] += 1
	else:
		words[word.lower()] = 1

sorted_words = sorted(words.items(), key=operator.itemgetter(1), reverse=True)



# Write the counted words into a file

file = open(sys.argv[1] [:-4] + "-count" + sys.argv[1] [-4:], "w")
file.write("Total Words - {} \n Unique Words - {} \n\n".format(len(txt.split()), len(sorted_words)))
for wordinfo in sorted_words:
	file.write("{} - {}\n".format(wordinfo[0],wordinfo[1]))
file.close()


print("All Done!")