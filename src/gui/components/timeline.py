## File: timeline.py
# Activity Timeline Component for Streamlit
import streamlit as st
from datetime import datetime, timedelta

class ActivityTimeline:
    """Component for displaying activity timeline"""

    def __init__(self, db_manager):
        self.db = db_manager

    def render(self):
        st.header("📈 Activity Timeline")

        days = st.selectbox("Time Range", ["24h", "3d", "7d", "30d"], index=0)
        delta = {
            "24h": 1,
            "3d": 3,
            "7d": 7,
            "30d": 30
        }[days]

        try:
            activities = self.db.get_activity_timeline(delta)
            if not activities:
                st.info("No activities found")
                return

            # Show as table
            st.table(activities)

        except Exception as e:
            st.error(f"Error loading timeline: {e}")

