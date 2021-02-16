import matplotlib.pyplot as plt 
import csv

def percentage(part, whole):
    return 100 * float(part) / float(whole)

####    FOR 1ST NEWS CHANNEL    ####

positive = 0
negative = 0
wpositive = 0
wnegative = 0
spositive = 0
snegative = 0
neutral = 0 

with open('GEO_Sentiments.csv', 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if (i == "Neutral"):
                neutral += 1
            elif (i == "Weakly_Positive"):
                wpositive += 1
            elif (i == "Positive"):
                positive += 1
            elif (i == "Strongly_Positive"):
                spositive += 1
            elif (i == "Weakly_Negative"):
                wnegative += 1
            elif (i == "Negative"):
                negative += 1
            elif (i == "Strongly_Negative"):
                snegative += 1


wpositive = percentage(wpositive,50)
positive = percentage(positive,50)
spositive = percentage(spositive,50)
neutral = percentage(neutral,50)
snegative = percentage(snegative,50)
negative = percentage(negative,50)
wnegative = percentage(wnegative,50)


names = ["Weakly Positive", "Positive", " Strongly Positive", "Neutral", "Weakly Negative", "Negative", "Strongly Negative"] 
positions = [0,1,2,3,4,5,6]
scores = [wpositive,positive,spositive,neutral,wnegative,negative,snegative]

plt.figure(figsize=(9, 6), dpi=100)
plt.bar(positions, scores, width= 0.6)
plt.ylabel("Percentage\n")
plt.xlabel("\nOutcome of 1st News Channel")
plt.yticks([0,10,20,30,40,50,60,70,80,90,100], 
['0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'])
plt.xticks(positions, names)
plt.tight_layout()
plt.savefig('C:/WampServer/www/SentimentAnalysis/Images/1stNews.svg', dpi=500)
plt.clf() 


####    FOR 2ND NEWS CHANNEL    ####


positive = 0
negative = 0
wpositive = 0
wnegative = 0
spositive = 0
snegative = 0
neutral = 0 

with open('AAJ_Sentiments.csv', 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if (i == "Neutral"):
                neutral += 1
            elif (i == "Weakly_Positive"):
                wpositive += 1
            elif (i == "Positive"):
                positive += 1
            elif (i == "Strongly_Positive"):
                spositive += 1
            elif (i == "Weakly_Negative"):
                wnegative += 1
            elif (i == "Negative"):
                negative += 1
            elif (i == "Strongly_Negative"):
                snegative += 1

wpositive = percentage(wpositive,50)
positive = percentage(positive,50)
spositive = percentage(spositive,50)
neutral = percentage(neutral,50)
snegative = percentage(snegative,50)
negative = percentage(negative,50)
wnegative = percentage(wnegative,50)

positions2 = [0,1,2,3,4,5,6]
scores2 = [wpositive,positive,spositive,neutral,wnegative,negative,snegative]

plt.figure(figsize=(9, 6), dpi=100)
plt.bar(positions2, scores2, width= 0.6, color= 'g')
plt.ylabel("Percentage\n")
plt.xlabel("\nOutcome of 2nd News Channel")
plt.yticks([0,10,20,30,40,50,60,70,80,90,100], 
['0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'])
plt.xticks(positions2, names)
plt.tight_layout()
plt.savefig('C:/WampServer/www/SentimentAnalysis/Images/2ndNews.svg', dpi=500)
plt.clf()

####    FOR 3RD NEWS CHANNEL    ####


positive = 0
negative = 0
wpositive = 0
wnegative = 0
spositive = 0
snegative = 0
neutral = 0 

with open('ARY_Sentiments.csv', 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if (i == "Neutral"):
                neutral += 1
            elif (i == "Weakly_Positive"):
                wpositive += 1
            elif (i == "Positive"):
                positive += 1
            elif (i == "Strongly_Positive"):
                spositive += 1
            elif (i == "Weakly_Negative"):
                wnegative += 1
            elif (i == "Negative"):
                negative += 1
            elif (i == "Strongly_Negative"):
                snegative += 1

wpositive = percentage(wpositive,50)
positive = percentage(positive,50)
spositive = percentage(spositive,50)
neutral = percentage(neutral,50)
snegative = percentage(snegative,50)
negative = percentage(negative,50)
wnegative = percentage(wnegative,50)

positions3 = [0.4,1.4,2.4,3.4,4.4,5.4,6.4]
scores3 = [wpositive,positive,spositive,neutral,wnegative,negative,snegative]

plt.figure(figsize=(9, 6), dpi=100)
plt.bar(positions3, scores3, width= 0.6, color= 'y')
plt.ylabel("Percentage\n")
plt.xlabel("\nOutcome of 3rd News Channel")
plt.yticks([0,10,20,30,40,50,60,70,80,90,100], 
['0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'])
plt.xticks(positions3, names)
plt.tight_layout()
plt.savefig('C:/WampServer/www/SentimentAnalysis/Images/3rdNews.svg', dpi=500)
plt.clf