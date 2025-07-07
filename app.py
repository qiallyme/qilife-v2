import streamlit as st
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Core application modules
from src.core.config_loader import get_config, update_config
from src.core.env_manager import init_session_state
from src.core.log_setup import setup_logging

# Monitoring and logic modules
from src.monitor.file_event_monitor import FileMonitor
from src.context.metadata_extractor import ContentExtractor
from src.memory.vector_store import VectorStorage
from src.memory.embedder import ContextMemory
from src.fileflow.mover import run_full_pipeline
from src.fileflow.rename_rules import DatabaseManager

# GUI components
from src.gui.components.folder_picker import FolderSelector
from src.gui.components.file_review import FileReview
from src.gui.components.timeline import ActivityTimeline
from src.gui.components.log_export import LogExport

# Initialize the session state at the beginning
init_session_state()

class App:
    """
    A class to encapsulate the Streamlit application.
    """

    def __init__(self):
        """
        Initializes the application and sets up the page configuration.
        """
        self.db_manager = st.session_state.db_manager
        self.vector_storage = st.session_state.vector_storage
        self.setup_page_config()

    def setup_page_config(self):
        """
        Configures the Streamlit page settings.
        """
        st.set_page_config(
            page_title="QLife AI – The One App",
            page_icon="🧠",
            layout="wide",
            initial_sidebar_state="expanded"
        )

    def render_sidebar(self):
        """
        Renders the sidebar navigation and status.
        """
        with st.sidebar:
            st.header("Navigation")
            page = st.selectbox("Select Page", [
                "Folder Monitor", "File Review", "Activity Timeline", "Export Logs", "Settings"
            ])

            self.display_api_key_status()
            self.display_monitoring_status()

            return page

    def display_api_key_status(self):
        """
        Displays the status of the OpenAI API key.
        """
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            st.success("✅ OpenAI API Key loaded")
        else:
            st.warning("⚠️ OpenAI API Key not found")

    def display_monitoring_status(self):
        """
        Displays the folder monitoring status and control button.
        """
        if st.session_state.get('monitoring_active', False):
            st.success(f"📁 Monitoring: {st.session_state.get('selected_folder', 'N/A')}")
            if st.button("Stop Monitoring"):
                st.session_state.monitoring_active = False
                st.rerun()
        else:
            st.info("📁 No folder being monitored")

    def render_page(self, page):
        """
        Renders the selected page.
        """
        page_routes = {
            "Folder Monitor": FolderSelector().render,
            "File Review": FileReview(self.db_manager).render,
            "Activity Timeline": ActivityTimeline(self.db_manager).render,
            "Export Logs": LogExport(self.db_manager).render,
            "Settings": self.render_settings_page,
        }
        
        # Get the render function for the selected page
        render_function = page_routes.get(page)
        if render_function:
            render_function()
        else:
            st.error("Page not found")

    def render_settings_page(self):
        """
        Renders the settings page with database stats, system actions, and API key management.
        """
        st.header("⚙️ Settings")
        col1, col2, col3 = st.columns(3)

        with col1:
            self.render_database_stats()
        with col2:
            self.render_system_actions()
        with col3:
            self.render_api_key_settings()

    def render_database_stats(self):
        """
        Displays database statistics.
        """
        st.subheader("Database Stats")
        try:
            stats = self.db_manager.get_database_stats()
            st.metric("Total Files", stats.get("total_files", 0))
            st.metric("Pending Reviews", stats.get("pending_reviews", 0))
            st.metric("Total Embeddings", stats.get("total_embeddings", 0))
        except Exception as e:
            st.error(f"Failed to load database stats: {e}")

    def render_system_actions(self):
        """
        Provides system action buttons like clearing data and rebuilding the index.
        """
        st.subheader("System Actions")
        if st.button("Clear All Data"):
            self.handle_clear_all_data()
        
        if st.button("Rebuild Vector Index"):
            self.handle_rebuild_vector_index()

    def handle_clear_all_data(self):
        """
        Handles the logic for clearing all data.
        """
        if st.checkbox("Confirm deletion of all data"):
            try:
                self.db_manager.clear_all_data()
                self.vector_storage.clear_all_vectors()
                st.success("All data has been cleared successfully.")
            except Exception as e:
                st.error(f"An error occurred while clearing data: {e}")

    def handle_rebuild_vector_index(self):
        """
        Handles the logic for rebuilding the vector index.
        """
        try:
            with st.spinner("Rebuilding vector index..."):
                self.vector_storage.rebuild_index()
            st.success("Vector index rebuilt successfully.")
        except Exception as e:
            st.error(f"An error occurred during rebuild: {e}")

    def render_api_key_settings(self):
        """
        Renders the settings for managing the OpenAI API key.
        """
        st.subheader("API Keys")
        config = get_config()
        new_api_key = st.text_input(
            "OpenAI API Key", 
            value=config.get("OPENAI_API_KEY", ""), 
            type="password"
        )

        if st.button("Save API Key"):
            self.handle_save_api_key(new_api_key)

    def handle_save_api_key(self, new_api_key):
        """
        Handles the logic for saving the new API key.
        """
        try:
            update_config("OPENAI_API_KEY", new_api_key)
            load_dotenv(override=True)  # Reload environment variables
            st.success("API Key saved successfully.")
        except Exception as e:
            st.error(f"Failed to save API Key: {e}")

    def run(self):
        """
        The main entry point to run the Streamlit application.
        """
        st.title("🧠 QLife AI – EmpowerQNow-713")
        st.markdown("*Capture, vectorize, and make all computer activity searchable through AI-powered content analysis*")
        
        page = self.render_sidebar()
        self.render_page(page)

if __name__ == "__main__":
    app = App()
    app.run()