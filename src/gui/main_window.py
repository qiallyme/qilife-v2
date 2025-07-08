import streamlit as st
from src.core.log_setup import setup_logging
from src.gui.splash_screen import show_splash
from src.gui.components.dashboard import Dashboard
from src.gui.components.folder_picker import FolderSelector
from src.gui.components.file_review import FileReview
from src.gui.components.timeline import ActivityTimeline
from src.gui.components.log_export import LogExport

def render_main_ui():
    # Initialize logging
    setup_logging()
    
    # Show splash screen on first load
    if 'splash_shown' not in st.session_state:
        show_splash()
        st.session_state.splash_shown = True

    # Sidebar navigation
    st.sidebar.header("Navigation")
    pages = ["Dashboard", "Folder Monitor", "File Review", "Activity Timeline", "Export Logs", "Settings"]
    if 'page' not in st.session_state:
        st.session_state.page = "Dashboard"
    page = st.sidebar.selectbox("Go to:", pages, index=pages.index(st.session_state.page))
    st.session_state.page = page

    # Route based on selection
    if page == "Dashboard":
        Dashboard().render()
    elif page == "Folder Monitor":
        FolderSelector().render()
    elif page == "File Review":
        FileReview(st.session_state.db_manager).render()
    elif page == "Activity Timeline":
        ActivityTimeline(st.session_state.db_manager).render()
    elif page == "Export Logs":
        LogExport(st.session_state.db_manager).render()
    elif page == "Settings":
        st.header("⚙️ Settings")
        st.write("Settings page under construction. Coming soon!")

