import pandas as pd
import re
import nltk
nltk.download('all')
from nltk.tokenize import word_tokenize
from nltk.text import Text
import streamlit as st

from collections import Counter

@st.cache_data
def load_data(file):
    df = pd.read_excel(file)
    return df


def clean_and_analyze_text(data, text_columns):
    """ Cleans the text data in specific columns of a given DataFrame by removing specific HTML-like tags
    such as <reference_list>, <references_list>, and <in_text_reference>, along with
    their enclosed content. It also removes any instances of 'reference_list' or
    'references_list' as extracted words, and calculates word frequency.

    Parameters:
    data (pd.DataFrame): A pandas DataFrame containing text data.
    text_columns (list): List of columns containing text to be processed.
    output_folder (str): The folder where the output file will be saved (default is 'output').
    output_filename (str): The name of the output CSV file (default is 'word_frequency.csv').

    Returns:
    pd.DataFrame: A cleaned DataFrame where word frequency is calculated and saved.
    """


    combined_words = ' '.join(data[text_columns].astype(str).fillna('').values.flatten())


    cleaned_content = re.sub(r'<references?_list>[\s\S]*?</references?_list>', '', combined_words, flags=re.DOTALL)
    cleaned_content = re.sub(r'<in_text_reference>[\s\S]*?</in_text_reference>', '', cleaned_content, flags=re.DOTALL)
    cleaned_content = re.sub(r'<original=[^>]>(.?)</original>', r'\1', cleaned_content)

    cleaned_content_new = cleaned_content.lower()

    words = re.findall(r"\b\w+(?:[-']\w+)*\b", cleaned_content_new)
    words = [word for word in words if word not in ['reference_list', 'references_list']]

    word_count = Counter(words)
    word_count_df = pd.DataFrame(word_count.items(), columns=['Word', 'Frequency']).sort_values(by='Frequency', ascending=False)

    return word_count_df


text_columns = [
'Practice Paragraph', 'Task 1.1.1', 'Task 1.1.2', 'Task 1.2.1',
'Task 1.2.2', 'Task 2.1.1', 'Task 2.1.2', 'Task 2.2.1', 'Task 2.2.2',
'Exam Term 2', 'Essay 3.1.1', 'Essay 3.1.2', 'Essay 3.2.1',
'Essay 3.2.2', 'Exam Term 3', 'Task 4.1', 'Task 4.2', 'Task 4.3',
]


st.title("Word frequency")
df = load_data(st.secrets['path'])
st.write("First 5 rows of your data:")
st.dataframe(df.head(5))


selected_columns = st.multiselect(
"Select text columns to analyze for word frequency:",
options=text_columns
)

if st.button('Word Frequency'):
    if selected_columns: # this condition only works if we have selected at least 1 column
        word_freq_df = clean_and_analyze_text(df, selected_columns)

        st.header('Word Frequency results:')
        st.dataframe(word_freq_df)

        csv = word_freq_df.to_csv(index=False)
        st.download_button(
        label="Download Word Frequency",
        data=csv,
        file_name="frequency.csv",
        mime="text/csv"
        )

    else:
        st.warning('No columns were selected. Please select at least 1 column for analysis')
