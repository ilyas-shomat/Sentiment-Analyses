
import string
from collections import Counter
import  matplotlib.pyplot as plt
import GetOldTweets3 as got

def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('corona virus') \
        .setSince("2020-01-01") \
        .setUntil("2020-04-15") \
        .setMaxTweets(100)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    text_tweets = [[tweet.text] for tweet in tweets]
    return text_tweets

    # for tweet in text_tweets:
    #     print(tweet)

text = ""
text_tweets_list = get_tweets()
text_tweets_lenght = len(text_tweets_list)
print(text_tweets_lenght)

for i in range(0, text_tweets_lenght):
    text = text_tweets_list[i][0] + " " + text

print(text)

# Берілген мәтінді пунктуация белгілерінен тазартамын, және барлық әріпті төменгі регистірге ауыстырамын
# text = open('Files/read', encoding='utf-8').read()

lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))

splited_text = cleaned_text.split()

# print(tokenized_words)

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []

for word in splited_text:
    if word not in stop_words:
        final_words.append(word)


# print(final_words)

emotion_list = []
with open('Files/emotions', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",",'').replace("'",'').strip()
        word, emotion = clear_line.split(':')
        # print("Word: "+word+", Emotion: "+ emotion)

        if word in final_words:
            emotion_list.append(emotion)

# print(emotion_list)
w = Counter(emotion_list)
print(w)

plt.bar(w.keys(), w.values())
plt.savefig('graph.png')
plt.show()