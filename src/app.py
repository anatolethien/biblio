import pandas as pd
import streamlit as st
import requests
from PIL import Image
from io import BytesIO

books = pd.read_csv(
    filepath_or_buffer='assets/books.csv',
    usecols=[
        'title',
        'description',
        'image-url',
        'dimension-x',
        'dimension-y',
        'dimension-z',
        'weight'
    ]
).sample(n=5)

def get_image(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

books['image'] = books['image-url'].apply(get_image)

st.markdown(
    '''
    # Biblio

    These books were written for you.

    ---
    '''
)

for index, row in books.iterrows():
    st.markdown(
        f'''
        ## {row['title']}
        
        {row['description']}

        - **Dimensions**: {row['dimension-x']}mm * {row['dimension-y']}mm * {row['dimension-z']}mm
        - **Weight**: {row['weight']}g
        '''
    )
    st.image(row['image'])
    st.markdown(
        '''
        ---
        '''
    )
