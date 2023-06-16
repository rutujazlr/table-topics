import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Zelar | Debate Topics",
    page_icon="https://cdn-icons-png.flaticon.com/512/2572/2572201.png",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None,
)
hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
st.markdown(hide_st_style, unsafe_allow_html=True)

c1, c2, c3 = st.columns([1, 5, 1])
c1.image("Zelarsoft Logo.png")
c2.markdown(
    """
<h1 style="font-family:layton"><center>Zelar's Eloquent Speakers</center></h1>
""",
    unsafe_allow_html=True,
)

st.markdown("***", unsafe_allow_html=True)

c1, c2, c3 = st.columns([1, 3, 1])
c2.markdown(
    """
<h2 style="font-family:Garamond;color:#3378b0"><center>Debate Topics</center></h2>
""",
    unsafe_allow_html=True,
)
c2.markdown("***", unsafe_allow_html=True)


@st.cache_data(show_spinner=True)
def getTopics(filepath):
    with open(filepath, "r") as f:
        content = f.read()
    return content.split("\n")


topics = getTopics("topics.txt")

c1, c2, c3 = st.columns([2, 1, 2])

if c2.button("Generate Random Topic", use_container_width=True):
    st.markdown("""<p><center>Today's Topic is</center></p>""", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 3, 1])
    c2.markdown(
        f"""<h2 style="font-family:ravnsara sans"><center>{np.random.choice(topics)}</center></h2>""",
        unsafe_allow_html=True,
    )
