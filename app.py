import streamlit as st
import time
from datetime import datetime, timedelta

# Set page config with white background
st.set_page_config(
    page_title="College Result Manager",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Maintenance mode control
MAINTENANCE_MODE = False  # Set to False when you want the app to be live

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
    
    # Set maintenance end time (you can adjust this to your actual maintenance schedule)
    maintenance_end = datetime.now() + timedelta(hours=24)
    
    # Create a placeholder for the countdown
    countdown_placeholder = st.empty()
    
    # Update countdown in real-time
    while datetime.now() < maintenance_end:
        time_left = maintenance_end - datetime.now()
        
        # Calculate days, hours, minutes, seconds
        days = time_left.days
        hours, remainder = divmod(time_left.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        # Display countdown
        if days > 0:
            countdown_text = f"Estimated time until maintenance completes: {days}d {hours:02d}:{minutes:02d}:{seconds:02d}"
        else:
            countdown_text = f"Estimated time until maintenance completes: {hours:02d}:{minutes:02d}:{seconds:02d}"
        
        countdown_placeholder.info(countdown_text)
        time.sleep(1)
    
    # Maintenance completed message
    st.success("Maintenance completed! The app is now live.")
    
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.9em;">
        <p>Developed by Shreyash Patil | Analytics Dashboard</p>
    </div>
    """, unsafe_allow_html=True)

def show_main_app():
    # Import page modules
    try:
        from pages import upload_pdf, dashboard, top_students, division_analysis, pass_fail_analysis, subject_analysis, student_search, excel_report
    except ImportError:
        st.error("Page modules not found. Please make sure the 'pages' directory exists with all required modules.")
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

def main():
    if MAINTENANCE_MODE:
        show_maintenance_page()
    else:
        show_main_app()

if __name__ == '__main__':
    main()
