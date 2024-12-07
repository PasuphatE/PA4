import openai
import streamlit as st
import pandas as pd
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt

openai.api_key = "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"

#st.title("🎈 My new app")
#st.write(
#    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
#)
#a=2+8
#st.write(
#    a
#)
#
#tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
#
#with tab1:
#    st.header("A cat")
#    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
#with tab2:
#    st.header("A dog")
#    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
#with tab3:
#    st.header("An owl")
#    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


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

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    return wordcloud
    
def main():
    st.title("🎈 Welcome to WordCloud generator ☁️")
    st.write("We can generate any WordCloud from your conditions using AI! Try Now!")

    user_prompt = st.text_area("Input your text here.", "Streamlit is awesome! Word Cloud is fun!")


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
