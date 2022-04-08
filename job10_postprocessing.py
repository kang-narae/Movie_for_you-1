import pandas as pd

df = pd.read_csv('./crawling_data/datasets/movie_review_2018_2022.csv')
print(df.head())
df.info()

stopwords = pd.read_csv('./crawling_data/stopwords.csv')
stopwords_list = list(stopwords['stopword'])
cleaned_sentences = []
stopwords_movie = ['영화', '보다', '출연', '감독', '연출', '보다', '좋다', '리뷰',
                   '작품', '있다', '하다', '보기', '개봉', '되어다', '평점',
                   '나오다', '제작', '없다', '이다']
stopwords_list = stopwords_list + stopwords_movie
for review in df.cleaned_sentences:
    review_word = review.split(' ')

    words = []
    for word in review_word:
        if len(word) > 1:
            if word not in stopwords_list:
                words.append(word)
    cleaned_sentence = ' '.join(words)
    cleaned_sentences.append(cleaned_sentence)
df['cleaned_sentences'] = cleaned_sentences
df.to_csv('./crawling_data/datasets/movie_review_2018_2022.csv',
          index=False)
df.info()

















