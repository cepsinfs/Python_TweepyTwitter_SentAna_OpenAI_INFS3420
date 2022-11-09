
import streamlit as st
import pandas as pd
from genFunctions import *


def fileAnalysis():
    
    # df = pd.DataFrame({"A" : [1, 2, 3, 4], "B" : [2, 4, 6, 8]})

    # st.write(df)

    # df1 = df.apply(square)

    # st.write(df1)

    st.title("File Analysis Task")


    up_file = st.file_uploader("Upload your File for analysis", type=['csv', 'xlsx'])

    if up_file:
        details = {

            "File name": up_file.name,
            "File type": up_file.type,
            "File Size": up_file.size
        }

        st.write(details)

        if up_file.type == "text/csv":
            content = pd.read_csv(up_file, index_col=0)
            
        else:
            content = pd.read_excel(up_file)
            content['author_id'] = content['author_id'].astype('int64')
            content['tweet_id'] = content['tweet_id'].astype('int64')
            

        feature = st.multiselect("Choose your Feature", options=content.columns, default=list(content.columns))
        
        with st.expander("Expand to see the data"):
            st.write(content[feature])

        clean = st.button("Clean Tweets")
        
        if clean:
            content['text'] = content['text'].apply(cleanText)
            st.write(content[feature])
        
        else:
            st.write(content[feature])

        
        


        max_likes = content.likes.max()

        tw_text = content.loc[content.likes == content.likes.max(), 'text'].values
        name = content.loc[content.likes == content.likes.max(), 'name'].values
        handler = content.loc[content.likes == content.likes.max(), 'handler'].values
        posted_on = content.loc[content.likes == content.likes.max(), 'date'].values

        st.markdown("## :thumbsup:" + str(max_likes) )
        st.write(f"{name[0]} ({handler[0]}) on {posted_on[0]}:" )
        st.info(tw_text[0])