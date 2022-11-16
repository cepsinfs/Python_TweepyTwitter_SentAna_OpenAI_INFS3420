
import streamlit as st
import pandas as pd
from genFunctions import *
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

st.set_option('deprecation.showPyplotGlobalUse', False)


def fileAnalysis():
    
    # df = pd.DataFrame({"A" : [1, 2, 3, 4], "B" : [2, 4, 6, 8]})

    # st.write(df)

    # df1 = df.apply(square)

    # st.write(df1)


    list1 = ["hi how are you", "Not bad", "I am going to commit suicide", "after the class", "may be!!"]

    list2 = ' '.join([item for item in list1])
    st.success(list2)


   

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
            content['Subjectivity'] = content['text'].apply(getSubjectivity)
            content['Polarity'] = content['text'].apply(getPolarity)
            content['Analysis'] = content['Polarity'].apply(getAnalysis)

            ## For Word Cloud Generation

            all_words = ' '.join([tw for tw in content['text']])
            
            wc = WordCloud(background_color='white').generate(all_words)
            plt.imshow(wc)
            plt.axis('off')
            st.pyplot()

            ## Streamlit Bar Chart

            lab_count = content.Analysis.value_counts()
            st.write(lab_count)
            st.bar_chart(lab_count)


            ## Matplotlib.pyplot Bar Chart
            labels = lab_count.index.values
            #st.write(labels)

            _count = lab_count.to_numpy()
            #st.write(_count)

            fig, ax = plt.subplots()

            ax.bar(labels, _count)
            ax.set_xlabel('Sentiments')
            ax.set_ylabel('Count')
            st.pyplot(fig)

            ## Matplotlib PIE chart

            pie_fig, ax = plt.subplots()
            ax.pie(_count, labels=labels, explode=(0, 0, 0.2), shadow=True, autopct="%1.1f%%" )
            st.pyplot(pie_fig)

            











            st.write(content)
        
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


        # info = content.loc[content.likes == content.likes.max(), ['tweet_id', 'author_id']].values
        # st.write(info[0][0])