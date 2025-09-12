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
### The KSAUHS Learner Corpus contains over 800,000 words from 157 students tracked across four trimesters. It is the first longitudinal collection of English academic writing by Arabic L1 learners in Saudi Arabia.

Use the tools provided to explore the corpus:
	•	Concordancer: search words and collocations in context
	•	Frequency Lists: compare vocabulary use across terms and tasks
	•	Spelling Errors: discover common error patterns

Built on FAIR data principles, the corpus supports research on language development, academic writing, and the role of new technologies in education.

Contact: ksauhslearnercorpus@gmail.com
"""
)
