#!ANSHUMALI_KARNA_PYTHON
# coding: utf-8

# # CORONAVIRUS DATA 

# In[2]:


from matplotlib import pyplot as plt
import OpenBlender
import pandas as pd
import json
get_ipython().run_line_magic('matplotlib', 'inline')
action = 'API_getObservationsFromDataset'
parameters = { 
 'token':'5e7334b3951629333c047563Seb8MBWZ8nvNWo9ca5zVOEE6Nq0K2W',
 'id_dataset':'5e6ac97595162921fda18076',
 'date_filter':{
               "start_date":"2020-01-01T06:00:00.000Z",
               "end_date":"2020-03-11T06:00:00.000Z"},
 'consumption_confirmation':'on' 
}

df_confirmed = pd.read_json(json.dumps(OpenBlender.call(action, parameters)['sample']), convert_dates=False, convert_axes=False).sort_values('timestamp', ascending=False)
df_confirmed.reset_index(drop=True, inplace=True)
df_confirmed.head(10)


# # CORONAVIRUS PLOT

# In[9]:


interest_countries = ['China', 'Iran', 'Korea', 'Italy', 'France', 'Germany', 'Spain']
for country in interest_countries:
    df_news['count_news_' + country] = [len([text for text in daily_lst if country.lower() in text]) for daily_lst in df_news['source_lst']]
df_news.reindex(index=df_news.index[::-1]).plot(x = 'timestamp', y = [col for col in df_news.columns if 'count' in col], figsize=(17,7), kind='area')


# In[11]:


#from os import path
#from PIL import Image
#from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#plt.figure()
#plt.imshow(WordCloud(max_font_size=50, max_words=80, background_color="white").generate(' '.join([val for val in df['source'][0: 20]])), interpolation="bilinear")
#plt.axis("off")
#plt.show()
#plt.figure()
#plt.imshow(WordCloud(max_font_size=50, max_words=80, background_color="white").generate(' '.join([val for val in df['source'][0: 20]])), interpolation="bilinear")
#plt.axis("off")
#plt.show()


# In[ ]:




