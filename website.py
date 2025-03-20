import streamlit as st
from PIL.Image import Image
from numpy.ma.core import left_shift
from pandas.core.computation.align import align_terms

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://static.vecteezy.com/system/resources/previews/002/099/443/large_2x/programming-code-coding-or-hacker-background-programming-code-icon-made-with-binary-code-digital-binary-data-and-streaming-digital-code-vector.jpg");
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.header("My Profile")
st.image("./anoop.jpg",caption="I am")

st.header("Display video")
video_file = open("./match.mp4","rb")
video_bytes = video_file.read()

st.video(video_bytes)







name = st.text_input("Enter Your Name : ")
Fname = st.text_input("Enter Your Father Name : ")
Adress = st.text_area("Enter Your Adress : ")
Qualification = st.selectbox("Enter Your Qualification : ",("Selected","Fresher","Graduated","Post Graduate"))
button = (st.button("Submit"))
if button:
    st.markdown(f"""
    Name: {name}
    Father: {Fname}
    Adress: {Adress}
    Qualification: {Qualification}""")

st.write("Please follow my instagram Account")
from PIL import Image
img = Image.open("its_raj09.lucky_qr.png")
st.image(img)
st.link_button("visit instagram","https://www.instagram.com/its_raj09.lucky/")
st.link_button("visit GitHub","https://github.com/iamanoopraj")
st.image("./follow.png",width=100)










