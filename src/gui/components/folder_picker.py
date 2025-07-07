# Folder Picker Component for Streamlit
# This component allows users to select a folder to monitor for file changes.
import streamlit as st
import os
from pathlib import Path
from src.monitor.file_event_monitor import FileMonitor

class FolderSelector:
    """Component for selecting and managing folder monitoring"""

    SUPPORTED_EXTS = {'.pdf', '.docx', '.doc', '.txt', '.md',
                      '.jpg', '.jpeg', '.png', '.bmp', '.tiff'}

    def render(self):
        st.header("📁 Folder Monitor")
        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader("Select Folder to Monitor")
            folder = st.text_input(
                "Folder Path",
                value=st.session_state.get('selected_folder', ''),
                placeholder="Enter full folder path to monitor"
            )

            if folder and os.path.isdir(folder):
                st.success(f"✅ Valid folder: {folder}")
                self._show_folder_stats(folder)

                if not st.session_state.monitoring_active:
                    if st.button("Start Monitoring"):
                        monitor = FileMonitor(
                            folder,
                            st.session_state.db_manager,
                            st.session_state.context_memory,
                            st.session_state.vector_storage
                        )
                        monitor.start()
                        st.session_state.file_monitor = monitor
                        st.session_state.monitoring_active = True
                        st.session_state.selected_folder = folder
                        st.success(f"Started monitoring: {folder}")
                else:
                    st.info("🟢 Monitoring is already active")

            elif folder:
                st.error("❌ Invalid folder path or not a directory")

            st.subheader("Quick Access")
            for p in [Path.home() / d for d in ("Desktop", "Documents", "Downloads")]:
                if p.exists():
                    if st.button(f"📁 {p.name}", key=f"quick_{p.name}"):
                        st.session_state.selected_folder = str(p)
                        st.experimental_rerun()

        with col2:
            st.subheader("Status")
            if st.session_state.monitoring_active:
                st.success("🟢 Active")
                if st.button("Stop Monitoring"):
                    st.session_state.file_monitor.stop()
                    st.session_state.monitoring_active = False
                    st.success("Stopped monitoring")
            else:
                st.info("🔴 Inactive")

            st.subheader("Supported File Types")
            st.write(", ".join(sorted(self.SUPPORTED_EXTS)).upper())

    def _show_folder_stats(self, folder: str):
        """Inline folder statistics without external utils."""
        p = Path(folder)
        total = sum(1 for _ in p.rglob('*') if _.is_file())
        supported = sum(1 for _ in p.rglob('*') if _.suffix.lower() in self.SUPPORTED_EXTS)
        size = sum(f.stat().st_size for f in p.rglob('*') if f.is_file())

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Files", total)
        col2.metric("Supported", supported)
        col3.metric("Size (MB)", f"{size/1e6:.1f}")
