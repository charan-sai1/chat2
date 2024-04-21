import google.generativeai as genai
import streamlit as st
import os
import PyPDF2

api = "AIzaSyB7R_31L1M5H3Qjwqd1LKy3QrHPM2zMbZM"
genai.configure(api_key=api)


model = genai.GenerativeModel(model_name="gemini-pro")


def read_pdf(file):
    # Create a PDF file reader object
    pdf_reader = PyPDF2.PdfFileReader(file)
    
    # Initialize an empty string to store the concatenated content
    full_text = ""
    
    # Loop through each page of the PDF
    for page_num in range(pdf_reader.numPages):
        # Extract text from the current page
        page_text = pdf_reader.getPage(page_num).extractText()
        
        # Append the page text to the full text string
        full_text += page_text
    
    return full_text

def ask(question:str):
    try:
        if question!='':
            response = chat.send_message(content=question)
    
    except "invalid_grant" as e:
        token_path = f'\\token.json'
        if os.path.exists(token_path):
           os.remove(token_path)
        print("\n\n\n\!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n")
        return 
           
    except Exception as e:
        return
    return response.text

import streamlit as st
import os

if __name__ == "__main__":
    st.title("Chat with pdf")
    
    # File upload section
    st.header("Upload a File")
    uploaded_file = st.file_uploader("Choose a file", type=['PDF', 'doc'])
    if uploaded_file is not None:
        pdf_content = read_pdf(uploaded_file)
        if pdf_content:
            hist = [
                    {"parts": [{"text": pdf_content}], "role": "user"},
                    {"parts": [{"text": "okay. what do you want me to do ?"}], "role": "model"},
                    {"parts": [{"text": "now with the give data answer my questions in a detiled manner.strictly do not give the information which is beyond the given data. Help me to prepare for my exams explain all the things i should know related to the question asked."}], "role": "user"},
                    {"parts": [{"text": "shure. i wll not give any information beyond the give context.i will defenitely help you for your exams."}], "role": "model"},
            ]
            chat = model.start_chat(history=hist)
        else:
            st.write("Invalid file")    
    # Text input section
    st.header("Enter Text")
    text_input = st.text_input("Enter text here:")
    if st.button("Submit"):
        st.write(pdf_content)
