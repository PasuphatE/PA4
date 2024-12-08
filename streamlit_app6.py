import streamlit as st
import pandas as pd
import openai
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from io import BytesIO

# ฟังก์ชั่นในการสร้าง word cloud
def generate_wordcloud(text, language):
    wordcloud = WordCloud(font_path=None if language == 'en' else 'ChulaCharasNewReg.ttf', width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig("wordcloud.png", format="png")
    return wordcloud

# ฟังก์ชั่นในการนับคำ
def count_words(df):
    text_data = ' '.join(df.astype(str).values.flatten())
    words = text_data.split()
    word_counts = pd.Series(words).value_counts()
    return word_counts

# Sidebar สำหรับการเติม API key
st.sidebar.title("OpenAI API Key")
api_key = st.sidebar.text_input("กรุณากรอก API Key", type="password")

# ตั้งค่า API key
if api_key:
    openai.api_key = api_key

    # รับ input จากผู้ใช้
    st.title("NLP Application with OpenAI")
    uploaded_file = st.file_uploader("อัปโหลดไฟล์ CSV หรือ XLSX - ใช้ข้อมูลภาษาอังกฤษเท่านั้น ", type=["csv", "xlsx", "txt"])

    if uploaded_file:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file, encoding='utf-8-sig')  # ใช้ encoding แบบ 'utf-8-sig'
        elif uploaded_file.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith(".txt"):
            df = pd.read_csv(uploaded_file, delimiter='\t', encoding='utf-8-sig')  # ใช้ encoding แบบ 'utf-8-sig'

        st.write("แสดงข้อมูลจากไฟล์ที่อัปโหลด:")
        st.dataframe(df)

        # นับคำ
        word_counts = count_words(df)

        # สร้างและแสดง word cloud
        text_data = ' '.join(df.astype(str).values.flatten())
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=f"สร้างภาพ word cloud จากข้อมูลนี้:\n{text_data}",
            max_tokens=1000
        )

        language = 'th' if any("\u0E00" <= ch <= "\u0E7F" for ch in text_data) else 'en'
        wordcloud = generate_wordcloud(response.choices[0].text, language)
        st.image(wordcloud.to_array())

        # แสดงภาพ word cloud และดาวน์โหลดผลงาน
        st.download_button(label="ดาวน์โหลดภาพ Word Cloud", data=open("wordcloud.png", "rb"), file_name="wordcloud.png")

