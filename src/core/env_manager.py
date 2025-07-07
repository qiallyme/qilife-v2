# TODO
import streamlit as st
from src.memory.vector_store import VectorStorage
from src.memory.embedder import ContextMemory
from src.fileflow.rename_rules import DatabaseManager

def init_session_state():
    if 'db_manager' not in st.session_state:
        st.session_state.db_manager = DatabaseManager()

    if 'vector_storage' not in st.session_state:
        st.session_state.vector_storage = VectorStorage()

    if 'context_memory' not in st.session_state:
        st.session_state.context_memory = ContextMemory(st.session_state.db_manager)

    if 'file_monitor' not in st.session_state:
        st.session_state.file_monitor = None

    if 'monitoring_active' not in st.session_state:
        st.session_state.monitoring_active = False

    if 'selected_folder' not in st.session_state:
        st.session_state.selected_folder = None
