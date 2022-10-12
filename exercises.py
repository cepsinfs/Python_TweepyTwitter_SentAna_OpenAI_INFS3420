from xmlrpc.client import FastMarshaller
import streamlit as st

st.set_page_config(
    "Main Application", 
    ":joy:", 
    )



st.title("Welcome to the Streamlit World!!")

numbers = []
en = []


num = st.number_input("Choose a number", min_value=1)

even =  st.checkbox("Generate Even Numbers")

if even:
    for item in range(2, num+1, 2):
        numbers.append(item)

    st.success(numbers)


odd = st.checkbox("Generate Odd Numbers")

if odd:
    for item in range(1, num+1, 2):
        en.append(item)

    st.success(en)






cohort = st.radio(
    "Choose your Cohort", 
    [2020, 2021, 2022], 
    horizontal=True)

if cohort:
    st.write("You have selected", cohort)
    
user = st.text_input("Username")
if user:
    st.info("Your username is: "+ user)


st.text_input("Password", type="password")















st.header("Web Development")

st.write("Some Text goes here about Web Development")

st.subheader("Graphical User Interface")

st.write("Some Text goes here about GUI")

a = 10
b = 20 
sum = a+b

st.write("The sum of a and b is: ", sum, (a*b))

sum

st.caption("Figure 1.1 - Emojis Explained")

st.text("print('This is an argument')")

st.code("tuple_object.count('item')")






