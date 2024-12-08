import openai
import streamlit as st
import pandas as pd
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt

key=""
with st.sidebar:
    st.title("🎈 Input Your OpenAI API Key 🎈")
    title = st.text_input("Type your key here", key,type="password")
    key=title
    if key=="":
        Currkey="None"
    else:
        Currkey=key
    if len(Currkey)>10:
        showKey=Currkey[0:4]+"..."+Currkey[-4:]
    else:
        showKey=Currkey
    st.write("Your current key:<br> ", showKey)

def get_chatgpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=500
)

        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

#def generate_wordcloud(text):
#    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
#    return wordcloud
    
def main():
    st.title("🎈 Welcome to WordCloud generator ☁️")
    st.write("We can generate any WordCloud from your conditions using AI! Try Now!")

    user_prompt = st.text_area("Input your text here.", "Streamlit is awesome! Word Cloud is fun!")

    st.write("Power by Pasuphat Earakskul, Surasak Kao-iean")


    if st.button("Create Word Cloud"):
        if user_prompt:
            with st.spinner("ChatGPT is calculating..."):
                response_text = get_chatgpt_response(user_prompt)
         
                st.subheader("ChatGPT's response:")
                st.write(response_text)

                wordcloud = generate_wordcloud(response_text)
                
                st.subheader("Word Cloud from your text:")
                fig, ax = plt.subplots()
                ax.imshow(wordcloud, interpolation="bilinear")
                ax.axis("off")
                st.pyplot(fig)  
        else:
            st.warning("please input text!")

if __name__ == "__main__":
    main()

