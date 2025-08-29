import streamlit as st

# Set page config with white background
st.set_page_config(
    page_title="College Result Manager",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import page modules
from pages import upload_pdf, dashboard, top_students, division_analysis, pass_fail_analysis, subject_analysis, student_search, excel_report

# Initialize session state for data storage
if 'stored_data' not in st.session_state:
    st.session_state.stored_data = {}

def save_data(path, info):
    """Save data to session state"""
    st.session_state.stored_data[path] = info

def load_data(path):
    """Load data from session state"""
    return st.session_state.stored_data.get(path, [])

def main():
    st.title("🎓 College Result Management System")
    st.markdown("---")
    
    st.sidebar.title("Navigation")
    menu_options = [
        "Upload PDF",
        "Performance Dashboard",
        "View Top Students",
        "Division Analysis",
        "Pass/Fail Analysis",
        "Subject-wise Analysis",
        "Student Search",
        "Generate Excel Report"
    ]
    choice = st.sidebar.selectbox("Select Option", menu_options)
    
    # Route to the appropriate page
    if choice == "Upload PDF":
        upload_pdf.show()
    elif choice == "Performance Dashboard":
        dashboard.show()
    elif choice == "View Top Students":
        top_students.show()
    elif choice == "Division Analysis":
        division_analysis.show()
    elif choice == "Pass/Fail Analysis":
        pass_fail_analysis.show()
    elif choice == "Subject-wise Analysis":
        subject_analysis.show()
    elif choice == "Student Search":
        student_search.show()
    elif choice == "Generate Excel Report":
        excel_report.show()
    
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.9em;">
        <p>Developed by Shreyash Patil | Analytics Dashboard</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()