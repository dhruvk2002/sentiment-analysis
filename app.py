import streamlit as st
import pickle
import time

# load the model
model = pickle.load(open('sentiment_analysis.pkl', 'rb'))

st.title('Sentiment Analysis')

input = st.text_input('Enter your text')

submit = st.button('Predict')

if submit:
    start = time.time()
    prediction = model.predict([input])
    end = time.time()
    st.write('Prediction time taken: ', round(end-start, 2), 'seconds')
    
    print(prediction[0])
    st.write(prediction[0])