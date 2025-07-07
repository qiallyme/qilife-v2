## File: file_review.py
import streamlit as st

class FileReview:
    """Component for reviewing and approving file rename suggestions"""

    def __init__(self, db_manager):
        self.db = db_manager

    def render(self):
        st.header("🔍 File Review & Approval")
        pending = self.db.get_pending_reviews()

        if not pending:
            st.info("✅ No files pending review")
            return

        # Bulk selection
        if 'selected_files' not in st.session_state:
            st.session_state.selected_files = set()

        for file in pending:
            fid = file['id']
            cols = st.columns([0.2, 2, 2, 1])
            sel = cols[0].checkbox("", key=f"sel_{fid}", value=(fid in st.session_state.selected_files))
            if sel:
                st.session_state.selected_files.add(fid)
            else:
                st.session_state.selected_files.discard(fid)

            cols[1].write(f"**{file['original_name']}**")
            cols[2].text_input(
                "New Name",
                value=file['suggested_name'],
                key=f"name_{fid}",
                label_visibility="collapsed"
            )
            action = cols[3].radio(
                "",
                options=["✅ Approve", "❌ Reject"],
                key=f"act_{fid}",
                label_visibility="collapsed"
            )

        if st.button("Apply Actions"):
            for fid in list(st.session_state.selected_files):
                choice = st.session_state.get(f"act_{fid}")
                new_name = st.session_state.get(f"name_{fid}")
                if choice == "✅ Approve":
                    self.db.approve_file_rename(fid, new_name)
                else:
                    self.db.reject_file_rename(fid)
            st.success("Actions applied")
            st.experimental_rerun()
