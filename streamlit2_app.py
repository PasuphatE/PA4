import streamlit as st
import openai
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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

openai.api_key = "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"

# ฟังก์ชันเรียกใช้งาน ChatGPT
def get_chatgpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # เปลี่ยนเป็น gpt-4 ถ้ามีสิทธิ์ใช้งาน
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500  # จำนวนคำสูงสุดที่ตอบกลับได้
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error: {str(e)}"

# ฟังก์ชันสร้าง Word Cloud
def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    return wordcloud

# UI หลักของ Streamlit
def main():
    st.title("ChatGPT Word Cloud Generator")
    st.write("ส่งคำถามไปยัง ChatGPT และสร้าง Word Cloud จากคำตอบที่ได้")

    # ช่องให้ผู้ใช้งานพิมพ์คำถาม
    user_prompt = st.text_area("ใส่ข้อความหรือคำถามที่คุณต้องการให้ ChatGPT ตอบกลับ:", "บอกข้อมูลเกี่ยวกับเทคโนโลยี AI")

    # ปุ่มส่งข้อความไปยัง ChatGPT
    if st.button("สร้าง Word Cloud"):
        if user_prompt:
            with st.spinner("กำลังประมวลผลคำตอบจาก ChatGPT..."):
                # เรียก ChatGPT เพื่อให้ตอบข้อความกลับมา
                response_text = get_chatgpt_response(user_prompt)
                
                # แสดงข้อความที่ได้จาก ChatGPT
                st.subheader("คำตอบจาก ChatGPT:")
                st.write(response_text)

                # สร้าง Word Cloud จากคำตอบของ ChatGPT
                wordcloud = generate_wordcloud(response_text)
                
                # แสดง Word Cloud โดยใช้ Matplotlib
                st.subheader("Word Cloud จากคำตอบ:")
                fig, ax = plt.subplots()
                ax.imshow(wordcloud, interpolation="bilinear")
                ax.axis("off")
                st.pyplot(fig)  # แสดงผลลัพธ์ใน Streamlit
        else:
            st.warning("กรุณาใส่ข้อความหรือคำถามก่อน!")

if __name__ == "__main__":
    main()
