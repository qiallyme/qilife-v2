import streamlit as st

class Dashboard:
    """
    Main dashboard showing quick-access cards to each module.
    """
    MODULES = [
        ("Folder Monitor", "📁"),
        ("File Review", "🔍"),
        ("Activity Timeline", "📊"),
        ("Export Logs", "🗂"),
        ("Settings", "⚙️")
    ]

    def render(self):
        st.title("🚀 QLife AI Dashboard")
        st.markdown("Welcome to **EmpowerQNow-713** – select a module to begin.")
        cols = st.columns(2, gap="large")
        for idx, (name, icon) in enumerate(self.MODULES):
            col = cols[idx % len(cols)]
            if col.button(f"{icon} {name}", key=name):
                st.session_state.page = name
                st.rerun()
