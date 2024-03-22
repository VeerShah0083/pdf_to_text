import streamlit as st
import pdfplumber
from googletrans import Translator

# Streamlit UI
def main():
    st.set_page_config(page_title="PDF Translator", page_icon="📚", layout="wide")

    # Include CSS styles
    st.markdown('<link rel="stylesheet" href="style.css">', unsafe_allow_html=True)

    st.title("PDF Translator")
    st.write("Upload a PDF file and select the language you want to translate the text into.")

    # File uploader
    uploaded_file = st.file_uploader("Upload PDF", type=['pdf'])

    # Language selection
    target_lang = st.selectbox("Select Language for Translation", ["English", "Hindi", "Marathi", "Gujarati"])

    lang_code_mapping = {
        "English": "en",
        "Hindi": "hi",
        "Marathi": "mr",
        "Gujarati": "gu"
    }

    if uploaded_file:
        st.write("Original PDF Text:")
        
        # Initialize translator
        translator = Translator()

        # Open PDF file using pdfplumber
        with pdfplumber.open(uploaded_file) as pdf:
            # Iterate through each page of the PDF
            for page in pdf.pages:
                # Extract text from the current page
                text = page.extract_text()

                # Translate the extracted text to the selected language
                translated_text = translator.translate(text, dest=lang_code_mapping[target_lang.title()]).text

                # Display the translated text
                st.write("Translated PDF Text:")
                st.write(translated_text)

                # Write the translated text to a file
                with open("translated_text.txt", mode='a', encoding='utf-8') as txt_file:
                    txt_file.write(translated_text + '\n')

# Run the Streamlit app
if __name__ == "__main__":
    main()
