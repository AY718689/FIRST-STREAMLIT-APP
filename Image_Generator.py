import streamlit as st
import pandas as pd
import numpy as np

st.title('BASIC IMAGE GENERATOR')

imgs = pd.read_csv("imgs_1.csv")[['img_link','keywords']]
key = imgs.groupby('keywords')['img_link'].count().sort_values(ascending=False).head(50).reset_index()

select = st.selectbox('Choose an option: ',options=tuple(key['keywords']))
n = st.number_input('How many images you want ?',1,10,help='Choose any number between 1 to 10')
cols = st.columns(n)
for col in cols :
    condition = imgs['keywords']==select
    idx_val = imgs[condition].index.to_list()
    col = st.image(imgs.iloc[np.random.choice(idx_val),0],width=500,use_column_width='always')