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