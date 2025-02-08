import pandas as pd
import re
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from collections import Counter
import streamlit as st

@st.cache_data
def load_data(file):
    df = pd.read_excel(file)
    return df

def clean_and_analyze_text(data, text_columns):
    """Cleans and processes text data by applying specific XML tag rules:
    - Removes incorrectly spelled words from <original=...> and keeps the correct version.
    - Removes <reference_list> and <in_text_reference> along with their content.
    - Retains the content inside <title>...</title>.

    Parameters:
    data (pd.DataFrame): DataFrame containing text data.
    text_columns (list): List of columns containing text to process.

    Returns:
    pd.DataFrame: A DataFrame with word frequency counts.
    """

    # Combine all text from the selected columns
    combined_words = ' '.join(data[text_columns].astype(str).fillna('').values.flatten())

    # **PREPROCESSING STEP: Remove non-breaking spaces and zero-width spaces**
    combined_words = combined_words.replace('\xa0', ' ')  # Remove non-breaking spaces
    combined_words = combined_words.replace('\u200b', '')  # Remove zero-width spaces

    # Debugging: Print first 1000 characters to check for hidden characters
    print("Preprocessed Text Before Regex:", combined_words[:1000])

    # Remove <reference_list> and <in_text_reference> along with their content
    cleaned_content = re.sub(r'<reference_list\b[^>]*>[\s\S]*?</reference_list>', '', combined_words, flags=re.DOTALL | re.IGNORECASE)
    cleaned_content = re.sub(r'<in_text_reference\b[^>]*>[\s\S]*?</in_text_reference>', '', cleaned_content, flags=re.DOTALL | re.IGNORECASE)

    # Ensure <original=...> keeps only the correct word
    cleaned_content = re.sub(r'<original=[^>]*?>(.*?)</original>', r'\1', cleaned_content)

    # Extract and keep <title> content
    title_content = re.findall(r'<title>(.*?)</title>', cleaned_content, re.DOTALL)
    if title_content:
        cleaned_content += ' ' + ' '.join(title_content)  # Append titles to the text

    # Debugging: Check after reference removal
    print("Text After Removing References:", cleaned_content[:1000])

    # Convert text to lowercase for uniformity
    cleaned_content = cleaned_content.lower()

    # Tokenize words
    words = re.findall(r"\b\w+(?:[-']\w+)*\b", cleaned_content)

    # Remove unnecessary words (e.g., extracted tags)
    words = [word for word in words if word not in ['reference_list', 'references_list']]

    # Compute word frequencies
    word_count = Counter(words)
    word_count_df = pd.DataFrame(word_count.items(), columns=['Word', 'Frequency']).sort_values(by='Frequency', ascending=False)

    return word_count_df

# Define columns expected in the dataset
text_columns = [
    'Practice Paragraph', 'Task 1.1.1', 'Task 1.1.2', 'Task 1.2.1',
    'Task 1.2.2', 'Task 2.1.1', 'Task 2.1.2', 'Task 2.2.1', 'Task 2.2.2',
    'Exam Term 2', 'Essay 3.1.1', 'Essay 3.1.2', 'Essay 3.2.1',
    'Essay 3.2.2', 'Exam Term 3', 'Task 4.1', 'Task 4.2', 'Task 4.3',
]

# Streamlit UI
st.title("Word Frequency Analyzer")

df = load_data(st.secrets['path'])

st.write("First 5 rows of your data:")
st.dataframe(df.head(5))

selected_columns = st.multiselect(
    "Select text columns to analyze for word frequency:",
    options=text_columns
)

if st.button('Word Frequency'):
    if selected_columns:
        word_freq_df = clean_and_analyze_text(df, selected_columns)

        st.header('Word Frequency Results:')
        st.dataframe(word_freq_df)

        csv = word_freq_df.to_csv(index=False)
        st.download_button(
            label="Download Word Frequency",
            data=csv,
            file_name="frequency.csv",
            mime="text/csv"
        )
    else:
        st.warning('No columns were selected. Please select at least 1 column for analysis.')
