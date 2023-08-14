import pandas as pd
import string
import Wordcloud

def preprocess_text(text):
    
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation)) 
    return text


df = pd.read_csv('customer_booking.csv', encoding='ISO-8859-1')


booking_origins = df['booking_origin']

preprocessed_origins = [preprocess_text(origin) for origin in booking_origins]


all_origins_text = ' '.join(preprocessed_origins)


word_list = all_origins_text.split()
word_frequency = pd.Series(word_list).value_counts()


print(word_frequency)

from wordcloud import WordCloud, STOPWORDS
stopwords = set(STOPWORDS)




def show_wordcloud(data):
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        max_words=100,
        max_font_size=30,
        scale=3,
        random_state=1)

    wordcloud=wordcloud.generate(str(booking_origins))

    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')

    plt.imshow(wordcloud)
    plt.show()

show_wordcloud(df.Lemma)

