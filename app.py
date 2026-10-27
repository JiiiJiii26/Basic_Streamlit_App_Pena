import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Christian Jay Pena | Portfolio",
    page_icon="👋",
    layout="wide",
)


if "visits" not in st.session_state:
    st.session_state.visits = 0
if "feedback" not in st.session_state:
    st.session_state.feedback = []

st.session_state.visits += 1


with st.sidebar:
    st.image(
        "https://placehold.co/300x300/1f3c88/ffffff?text=CJP",
        caption="Christian Jay Pena — stand-in photo",
    )
    st.header("Navigate")
    section = st.radio(
        "Jump to a section:",
        ["About", "Autobiography", "Skills", "Projects", "Contact"],
    )
    st.divider()
    st.metric("Page visits this session", st.session_state.visits)
    dark = st.checkbox("Enable dark-mode theme", value=False)
    st.caption("CSIT 349 · Section G01")


st.title("👋 Hi, I'm Christian Jay Pena")
st.subheader("CSIT 349 · Applied AI · Section G01 · Cebu Institute of Technology – University")
st.write(
    "I'm a 3rd-year BSIT student and a beginner in coding, learning Python, "
    "web basics, and data. This page is my autobiography and portfolio."
)
st.divider()


if section == "About" or True:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(
            "https://placehold.co/400x400/1f3c88/ffffff?text=Christian+Jay+Pena",
            caption="Stand-in photo of Christian Jay Pena",
        )
    with col2:
        st.header("About Me")
        st.markdown(
            """
            I'm **Christian Jay Pena**, a 3rd-year BSIT student at
            **Cebu Institute of Technology – University**. I started coding
            in school and I'm still a beginner, but I enjoy learning by
            building small projects — a to-do app here, a calculator there —
            and seeing them actually work. My goal this year is to get
            comfortable with Python and basic web development.
            """
        )
        m1, m2, m3 = st.columns(3)
        m1.metric("Projects built", "3")
        m2.metrics("Languages learning", "3") if False else m2.metric("Languages learning", "3")
        m3.metric("Year level", "3rd")


st.header("📖 Autobiography")
with st.expander("Read my full story", expanded=False):
    st.markdown(
        """
        **Background.** I grew up in Cebu and went to a local public high school.
        I wasn't into computers as a kid, but when I had to pick a college course,
        Information Technology felt like a practical choice — something with a
        clear job path. Now that I'm in it, I've actually come to enjoy the
        problem-solving side of programming.

        **Education.** I'm pursuing a **BS in Information Technology** at
        **Cebu Institute of Technology – University** (expected **2027**).
        Relevant coursework so far: Programming 1 & 2, Data Structures,
        Databases, and now Applied AI.

        **Interests.** Mobile games, watching coding tutorials on YouTube,
        basketball, and hanging out with classmates after class.

        **Milestones.**
        """
    )
    st.markdown(
        """
        - **2023** — Started BSIT at CIT-U; wrote my first "Hello World" in Python.
        - **2024** — Finished Programming 2 with a final project: a simple grade calculator.
        - **2025** — Built my first basic website using HTML/CSS as a class exercise.
        - **2026** — Enrolled in Applied AI and built this Streamlit portfolio.
        """
    )


st.header("🛠 Skills")
left, right = st.columns(2)
with left:
    st.write("**Proficiency (self-rated, beginner level):**")
    skills = pd.DataFrame(
        {
            "Skill": ["Python", "HTML/CSS", "SQL", "Git", "Pandas", "Streamlit"],
            "Level": [55, 50, 40, 30, 45, 50],
        }
    )
    st.table(skills.set_index("Skill"))
with right:
    st.write("**Visualized:**")
    st.bar_chart(skills.set_index("Skill"))


st.header("🚀 Projects")
tab1, tab2, tab3 = st.tabs(["Grade Calculator", "Class Website", "To-Do App"])

with tab1:
    st.subheader("Grade Calculator (Programming 2 project)")
    st.write("**Role:** Solo developer (class project)")
    st.write("**Tools:** Python")
    st.write(
        "**Outcome:** Built a console program that computes a student's final "
        "grade from weighted quiz, activity, and exam scores. It was my first "
        "finished program and taught me how to use functions and input validation."
    )

with tab2:
    st.subheader("Simple Class Website")
    st.write("**Role:** Solo developer (practice project)")
    st.write("**Tools:** HTML, CSS")
    st.write(
        "**Outcome:** Made a 3-page static website about our class schedule and "
        "section info. It was my first time using HTML and CSS and helped me "
        "understand how layouts work."
    )

with tab3:
    st.subheader("To-Do List App")
    st.write("**Role:** Solo developer (self-study)")
    st.write("**Tools:** Python, Streamlit")
    st.write(
        "**Outcome:** A small Streamlit app where you can add, check off, and "
        "remove tasks. My first exposure to Streamlit and how it uses session "
        "state to remember data."
    )


st.header("✉️ Contact & Feedback")
with st.form("contact_form", clear_on_submit=True):
    c1, c2 = st.columns(2)
    name = c1.text_input("Your name")
    email = c2.text_input("Your email")
    rating = st.slider("How useful was this page?", 1, 5, 3)
    topics = st.multiselect(
        "What would you like to hear more about?",
        ["Beginner coding", "Python", "Web basics", "Streamlit"],
    )
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send feedback")

if submitted:
    if name and email and message:
        st.session_state.feedback.append(
            {"name": name, "email": email, "rating": rating,
             "topics": topics, "message": message}
        )
        st.success(f"Thanks, {name}! Your feedback was recorded. ⭐ {rating}/5")
        st.balloons()
    else:
        st.error("Please fill in name, email, and message.")


if st.session_state.feedback:
    df = pd.DataFrame(st.session_state.feedback)
    st.download_button(
        "⬇ Download feedback as CSV",
        data=df.to_csv(index=False),
        file_name="feedback.csv",
        mime="text/csv",
    )


st.divider()
st.caption("© 2026 Christian Jay Pena · CSIT 349 Section G01 · Cebu Institute of Technology – University · Built with Streamlit")