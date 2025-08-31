import streamlit as st
import time
from datetime import datetime, timedelta
import traceback
import sys
import os

# Set page config with white background
st.set_page_config(
    page_title="College Result Manager",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Maintenance mode control - Set to False for live app
MAINTENANCE_MODE = False

# Initialize session state for data storage
if 'stored_data' not in st.session_state:
    st.session_state.stored_data = {}

def save_data(path, info):
    """Save data to session state"""
    st.session_state.stored_data[path] = info

def load_data(path):
    """Load data from session state"""
    return st.session_state.stored_data.get(path, [])

def show_maintenance_page():
    st.title("🔧 College Result Management System")
    st.markdown("---")
    
    # Maintenance message with styling
    st.markdown(
        """
        <div style='
            background: linear-gradient(135deg, #ff6b6b, #feca57);
            padding: 2rem;
            border-radius: 10px;
            text-align: center;
            color: white;
            margin: 2rem 0;
        '>
            <h1 style='color: white; margin-bottom: 1rem;'>🚧 Under Maintenance 🚧</h1>
            <p style='font-size: 1.2rem;'>
                Our application is currently undergoing maintenance to improve your experience.
            </p>
            <p style='font-size: 1.2rem;'>
                Please check back later. We apologize for any inconvenience.
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Set maintenance end time
    maintenance_end = datetime.now() + timedelta(hours=2)
    
    # Create a placeholder for the countdown
    countdown_placeholder = st.empty()
    
    # Display static countdown (Streamlit Cloud doesn't support real-time updates well)
    time_left = maintenance_end - datetime.now()
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    countdown_placeholder.info(f"Estimated time until maintenance completes: {hours:02d}:{minutes:02d}:{seconds:02d}")
    
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.9em;">
        <p>Developed by Shreyash Patil | Analytics Dashboard</p>
    </div>
    """, unsafe_allow_html=True)

def load_page_modules():
    """Safely load page modules with error handling"""
    try:
        # Add the current directory to Python path
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        
        from pages import upload_pdf, dashboard, top_students, division_analysis, pass_fail_analysis, subject_analysis, student_search, excel_report
        return {
            "upload_pdf": upload_pdf,
            "dashboard": dashboard,
            "top_students": top_students,
            "division_analysis": division_analysis,
            "pass_fail_analysis": pass_fail_analysis,
            "subject_analysis": subject_analysis,
            "student_search": student_search,
            "excel_report": excel_report
        }
    except ImportError as e:
        st.error(f"Error importing page modules: {str(e)}")
        st.code(traceback.format_exc())
        return None
    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")
        st.code(traceback.format_exc())
        return None

def show_main_app():
    # Load page modules with error handling
    page_modules = load_page_modules()
    if page_modules is None:
        st.error("Failed to load application modules. Please check the logs.")
        return
    
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
    
    # Route to the appropriate page with error handling
    try:
        if choice == "Upload PDF":
            page_modules["upload_pdf"].show()
        elif choice == "Performance Dashboard":
            page_modules["dashboard"].show()
        elif choice == "View Top Students":
            page_modules["top_students"].show()
        elif choice == "Division Analysis":
            page_modules["division_analysis"].show()
        elif choice == "Pass/Fail Analysis":
            page_modules["pass_fail_analysis"].show()
        elif choice == "Subject-wise Analysis":
            page_modules["subject_analysis"].show()
        elif choice == "Student Search":
            page_modules["student_search"].show()
        elif choice == "Generate Excel Report":
            page_modules["excel_report"].show()
    except Exception as e:
        st.error(f"Error loading {choice} page: {str(e)}")
        st.code(traceback.format_exc())
    
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.9em;">
        <p>Developed by Shreyash Patil | Analytics Dashboard</p>
    </div>
    """, unsafe_allow_html=True)

def main():
    # Add debug information in sidebar
    with st.sidebar:
        if st.checkbox("Show debug info", False):
            st.write("Python version:", sys.version)
            st.write("Current directory:", os.getcwd())
            st.write("Files in directory:", os.listdir('.'))
            if os.path.exists('pages'):
                st.write("Pages directory:", os.listdir('pages'))
    
    if MAINTENANCE_MODE:
        show_maintenance_page()
    else:
        show_main_app()

if __name__ == '__main__':
    main()
