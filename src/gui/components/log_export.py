## File: log_export.py
# Log Export Component for Streamlit
import streamlit as st
from datetime import datetime
import io
import csv

class LogExport:
    """Component for exporting logs and activity data"""

    def __init__(self, db_manager):
        self.db = db_manager

    def render(self):
        st.header("📤 Export Logs")

        if st.button("Download Logs CSV"):
            try:
                rows = self.db.export_logs()   # should return list of dicts or CSV string
                if isinstance(rows, str):
                    data = rows
                else:
                    # convert list of dicts to CSV
                    buf = io.StringIO()
                    writer = csv.DictWriter(buf, fieldnames=rows[0].keys())
                    writer.writeheader()
                    writer.writerows(rows)
                    data = buf.getvalue()

                filename = f"qilife_logs_{datetime.now():%Y%m%d_%H%M%S}.csv"
                st.download_button("Download", data, file_name=filename, mime="text/csv")
            except Exception as e:
                st.error(f"Error exporting logs: {e}")
