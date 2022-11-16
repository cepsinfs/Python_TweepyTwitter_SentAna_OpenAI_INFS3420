import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from fileTask import *
from mulAnalysis import *


st.image('logo-no-background.png')

with st.sidebar:


    option = option_menu(
        "Analysis Method", 
        options=['File Analysis', 'Multiple Tweets Analysis', 'Explore Profile', 'Single Tweet Analysis'], 
        menu_icon="house-door", 
        icons=["upload", "list-check","person-bounding-box", "chat-dots"], 
        
        
        )

if option =="File Analysis":
    fileAnalysis()


if option =="Multiple Tweets Analysis":
    mul_tweets_analysis()

    
        










