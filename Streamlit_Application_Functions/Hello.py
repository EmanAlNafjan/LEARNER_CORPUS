import streamlit as st

st.set_page_config(page_title="KSAUHS Learner Corpus", page_icon="📝")

st.markdown(
"""
<style>
/* Select the default sidebar nav element */
[data-testid="stSidebarNav"]::before {
content: "Select what you would like to search.";
font-size: 16px;
font-weight: bold;
color: green;
margin: 0 0 10px 10px;
display: block;
}
</style>
""",
unsafe_allow_html=True
)

st.markdown("# KSAUHS Learner Corpus 📝")

st.markdown(
"""
## The KSAUHS Learner Corpus is a longitudinal corpus made of EFL health sciences students writing assignments and exams in Saudi.""")
st.markdown(
"""
👈 Select how you would like to search the corpus from the sidebar
### Want to learn more?
- Check out our paper at https://assets-eu.researchsquare.com/files/rs-4755662/v1/f425c3c0-48fd-4433-be7d-6c10a83d11b3.pdf?c=1725076036
"""
)
