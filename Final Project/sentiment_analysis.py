import csv

with open('sentiment_desc.csv', mode= 'r') as file:
    csv_reader = csv.reader(file)
    descriptions = list(csv_reader)

sent_file = open('AFINN-111.txt')

scores = {}  # initialize an empty dictionary
for line in sent_file:
    term, score = line.split("\t")
    scores[term] = int(score)  # Convert the score to an integer

score = 0
for photo in descriptions:
    for word in photo:
        if word in scores.keys():
            score = score + scores[word]
            # score = scores[word]
            # print(score)
print(score)
