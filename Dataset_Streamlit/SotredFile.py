import streamlit as st
import pandas as pd


st.title("File Analysis Task")

st.markdown("---")

up_file = st.file_uploader("Upload your File for analysis", type=['csv', 'xlsx'])

details = {

    "File name": up_file.name,
    "File type": up_file.type,
    "File Size": up_file.size
}

#st.write(details)

if up_file.type == "text/csv":
    content = pd.read_csv(up_file, index_col=0)
    with st.expander("Expand Data"):
        content
else:
    content = pd.read_excel(up_file)
    content['author_id'] = content['author_id'].astype('int64')
    content['tweet_id'] = content['tweet_id'].astype('int64')
    with st.expander("Expand Data"):
        content

feature = st.multiselect("Choose your Feature", options=content.columns, default=list(content.columns))
content[feature]

max_likes = content.likes.max()

tw_text = content.loc[content.likes == content.likes.max(), 'text'].values
name = content.loc[content.likes == content.likes.max(), 'name'].values
handler = content.loc[content.likes == content.likes.max(), 'handler'].values
posted_on = content.loc[content.likes == content.likes.max(), 'date'].values

st.markdown("## :thumbsup:" + str(max_likes) )
st.write(f"{name[0]} ({handler[0]}) on {posted_on[0]}:" )
st.info(tw_text[0])






