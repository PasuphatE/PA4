import streamlit as st

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

st.title("🎈 Welcome to WordCloud generator ☁️")
st.write(
    "We can generate any WordCloud from your conditions using AI! Try Now!"
)

    # กล่องข้อความสำหรับผู้ใช้ใส่ข้อมูล
    user_input = st.text_area("ใส่ข้อความที่นี่", "Streamlit is awesome! Word Cloud is fun!")


if __name__ == "__main__":
    main()
