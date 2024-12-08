import streamlit as st
import pandas as pd
import openai
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from io import BytesIO

# ฟังก์ชั่นในการสร้าง word cloud
def generate_wordcloud(text, language):
    if language == 'th':
        font_path = 'path/to/ChulaCharasNewReg.ttf'  # เปลี่ยนเป็นเส้นทางที่ถูกต้องของไฟล์ฟอนต์
    else:
        font_path = None
    wordcloud = WordCloud(font_path=font_path, width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig("wordcloud.png", format="png")
    return wordcloud

# ฟังก์ชั่นในการนับคำ
def count_words(text):
    words = text.split()
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
    user_input = st.text_area("กรุณาป้อนข้อความ (รองรับทั้งภาษาไทยและภาษาอังกฤษ)")

    if user_input:
        st.write("ข้อความที่ป้อน:")
        st.write(user_input)

        # นับคำ
        word_counts = count_words(user_input)
        st.write("ตารางความถี่ของคำ:")
        st.dataframe(word_counts)

        # ดาวน์โหลดตารางความถี่ของคำ
        csv = word_counts.to_csv(index=False).encode('utf-8-sig')
        st.download_button(
            label="ดาวน์โหลดตารางความถี่เป็น CSV",
            data=csv,
            file_name='word_counts.csv',
            mime='text/csv',
        )

        # สร้างและแสดง word cloud
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=f"สร้างภาพ word cloud จากข้อมูลนี้:\n{user_input}",
            max_tokens=1000
        )

        language = 'th' if any("\u0E00" <= ch <= "\u0E7F" for ch in user_input) else 'en'
        wordcloud = generate_wordcloud(response.choices[0].text, language)
        st.image(wordcloud.to_array())

        # แสดงภาพ word cloud และดาวน์โหลดผลงาน
        st.download_button(label="ดาวน์โหลด Word Cloud", data=open("wordcloud.png", "rb"), file_name="wordcloud.png")

