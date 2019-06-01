import pandas as pd
from langdetect import detect
from tqdm import tqdm_notebook
import nltk


def modelSession():
        # creates 

        # reading
        data = pd.read_csv('articles_bbc_2018_01_30.csv')
        print(data.shape)
        data = data.dropna().reset_index(drop=True)
        print(data.shape)
        print(data.head())

        # cleaning
        tqdm_notebook().pandas()
        data['lang'] = data.articles.progress_map(detect)
        data.lang.value_counts()
        data = data.loc[data.lang=='en']

        #tokenization
        data['sentences'] = data.articles.progress_map(sent_tokenize)
        data['sentences'].head(1).tolist()[0][:3] # Print the first 3 sentences of the 1st article



modelSession()