import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import GetOldTweets3 as got


############### Твиттерден кілттіr сөздерге байланысты керек твиттерді жинап алатын функция ####################

def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('crime') \
        .setSince("2020-01-01") \
        .setUntil("2020-04-15") \
        .setMaxTweets(300)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    text_tweets = [[tweet.text] for tweet in tweets]
    return text_tweets

    # for tweet in text_tweets:
    #     print(tweet)

############### Твиттерден алынған барлық твиттерді бір үлкен текстке айналдыру ################################

text = ""
text_tweets_list = get_tweets()
text_tweets_lenght = len(text_tweets_list)
# print(text_tweets_lenght)

for i in range(0, text_tweets_lenght):
    text = text_tweets_list[i][0] + " " + text

print(text)

############### Берілген мәтінді пунктуация белгілерінен тазартамын, ###########################################
############### және барлық әріпті төменгі регистірге ауыстырамын, және stop сөздерден тазартамын ##############

# text = open('Files/read', encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
tokenized_words = word_tokenize(cleaned_text, "english")

# print(tokenized_words)

final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)


############### Толық тазартылған текстті алып, әрбір сөзді қандай да бір ######################################
############### эмоцияға жатама жоқ па соны тексеремін #########################################################

emotion_list = []
with open('files/emotions', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        # print("Word: "+word+", Emotion: "+ emotion)
        if word in final_words:
            emotion_list.append(emotion)

# print(emotion_list)
emotions_count = Counter(emotion_list)
# print(emotions_count)

############### NLTK пайдаланып сентимент анализ жасаймын, нәтижесінде жиналған ################################
############### барлық твиттердің не жағымды не жағымсыз екенін анықтаймын #####################################

def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    pos = score['pos']
    neg = score['neg']

    if pos > neg:
        print('positive value')
    elif neg > pos:
        print('negative value')
    else:
        print('neutral')


sentiment_analyse(cleaned_text)

fig, ax1 = plt.subplots()
ax1.bar(emotions_count.keys(), emotions_count.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
