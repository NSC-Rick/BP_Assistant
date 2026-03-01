import streamlit as st
from utils.storage import save_module_data

def render(project_id, existing_data=None):
    st.header("Module 1: Business Snapshot")
    st.markdown("Provide a high-level overview of your business.")
    
    existing_data = existing_data or {}
    
    with st.form("snapshot_form"):
        business_name = st.text_input(
            "Business Name",
            value=existing_data.get("business_name", "")
        )
        
        location = st.text_input(
            "Location",
            value=existing_data.get("location", "")
        )
        
        stage = st.selectbox(
            "Stage",
            options=["Startup", "Acquisition", "Expansion"],
            index=["Startup", "Acquisition", "Expansion"].index(existing_data.get("stage", "Startup"))
        )
        
        description = st.text_area(
            "Brief Description",
            value=existing_data.get("description", ""),
            height=150
        )
        
        owner_background = st.text_area(
            "Owner Background",
            value=existing_data.get("owner_background", ""),
            height=150
        )
        
        submitted = st.form_submit_button("Save Module")
        
        if submitted:
            data = {
                "business_name": business_name,
                "location": location,
                "stage": stage,
                "description": description,
                "owner_background": owner_background
            }
            save_module_data(project_id, "snapshot", data)
            st.success("✓ Module 1 saved successfully")
            st.rerun()
