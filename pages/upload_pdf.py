import streamlit as st
import pdfplumber
import pandas as pd
import re
from io import BytesIO
import traceback

def extract_student_data_from_bytes(pdf_bytes):
    try:
        # Your existing extraction code
        student_info_all_with_marks = []
        # ... rest of your function
        
        return student_info_all_with_marks
    except Exception as e:
        st.error(f"Error extracting data from PDF: {str(e)}")
        return None

def store_data(uploaded_file):
    try:
        if uploaded_file is None:
            st.warning("Please upload a PDF file first.")
            return
        
        # Process directly from uploaded file bytes
        pdf_bytes = uploaded_file.getvalue()
        student_info = extract_student_data_from_bytes(pdf_bytes)
        
        if not student_info:
            st.error("No student data found in the PDF.")
            return
        
        data = []
        for record in student_info:
            data.append({
                "Seat No": record['Seat No'], 
                "Name": record['Name'], 
                "Percentage": record['Percentage'], 
                "Status": record['Status']
            })
        
        # Save to session state
        st.session_state.stored_data['Result_dict'] = student_info
        st.session_state.stored_data["Shoert_data"] = data
        
        st.success("✅ All data saved successfully!")
        st.subheader("Sample Data")
        st.dataframe(pd.DataFrame(data).head())
        
    except Exception as e:
        st.error(f"Error processing PDF: {str(e)}")
        st.code(traceback.format_exc())

def show():
    try:
        st.header("📤 Upload Result PDF")
        uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
        if st.button("Process PDF"):
            store_data(uploaded_file)
    except Exception as e:
        st.error(f"Error in upload page: {str(e)}")
        st.code(traceback.format_exc())
