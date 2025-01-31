import pandas as pd
import numpy as np
import pandas as pd
import re
import os
from collections import Counter
import streamlit as st
pd.set_option('display.max_columns', 500)


@st.cache_data
def load_data(file):
    df = pd.read_excel(file)
    return df



def mistakes_data_analysis(data, text_columns):
    """"
    # TODO: write proper summary of how to use this function
    """
   

    all_mistakes_list = []

    for column in text_columns:
        if column in data.columns:
            for text_id, text in zip(data['Major'],  data[column].dropna()):
                if not pd.isnull(text):

                    corrected_text = re.sub(r"<original=([^>']+)>", r"<original='\1'>", text)

                    mistakes = re.findall(r"<original='([^']+)'>([^<]+)</original>", corrected_text)

                    all_mistakes_list.extend([{'Major': text_id, "Original":mistake[0], 'Corrected':mistake[1] } for mistake in mistakes])

    mistakes_data = pd.DataFrame(all_mistakes_list, columns=['Major', 'Original', 'Corrected'])

    
    return mistakes_data

text_columns = [
       'Practice Paragraph', 'Task 1.1.1', 'Task 1.1.2', 'Task 1.2.1',
       'Task 1.2.2', 'Task 2.1.1', 'Task 2.1.2', 'Task 2.2.1', 'Task 2.2.2',
       'Exam Term 2', 'Essay 3.1.1', 'Essay 3.1.2', 'Essay 3.2.1',
       'Essay 3.2.2', 'Exam Term 3', 'Task 4.1', 'Task 4.2', 'Task 4.3',
]

st.title("Mistakes Data Analysis")
df = load_data(st.secrets['path'])
st.write("First 5 rows of your data:")
st.dataframe(df.head(5))

selected_columns = st.multiselect(
"Select text columns to analyze for mistakes:",
options=text_columns
)

if st.button("Extract Mistakes"):
    mistakes_data = mistakes_data_analysis(df, selected_columns)
    if not mistakes_data.empty:
        st.write("Extracted Mistakes:")
        st.dataframe(mistakes_data)

    csv = mistakes_data.to_csv(index=False)
    st.download_button(
        label="Download Mistakes Data",
        data=csv,
        file_name="mistakes.csv",
        mime="text/csv"
        )
else:
    st.warning("No mistakes found in the text columns.")
