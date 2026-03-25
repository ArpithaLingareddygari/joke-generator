import streamlit as st
import requests
st.title("random joke generator")
st.button("get joke")
url = "https://official-joke-api.appspot.com/random_joke"
with st.spinner("fetching a funny joke..."):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        st.write("### Here's your joke:")
        st.success(data["setup"])
        st.info(data["punchline"])
    else:
        st.error("failed to fetch joke. try again!")
