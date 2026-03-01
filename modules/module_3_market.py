import streamlit as st
from utils.storage import save_module_data

def render(project_id, existing_data=None):
    st.header("Module 3: Market & Customers")
    st.markdown("Describe your target market and competitive position.")
    
    existing_data = existing_data or {}
    
    with st.form("market_form"):
        primary_customer = st.text_area(
            "Primary Customer",
            value=existing_data.get("primary_customer", ""),
            height=100
        )
        
        geographic_reach = st.text_input(
            "Geographic Reach",
            value=existing_data.get("geographic_reach", "")
        )
        
        alternatives = st.text_area(
            "Alternatives",
            value=existing_data.get("alternatives", ""),
            height=100
        )
        
        differentiation = st.text_area(
            "Differentiation",
            value=existing_data.get("differentiation", ""),
            height=150
        )
        
        submitted = st.form_submit_button("Save Module")
        
        if submitted:
            data = {
                "primary_customer": primary_customer,
                "geographic_reach": geographic_reach,
                "alternatives": alternatives,
                "differentiation": differentiation
            }
            save_module_data(project_id, "market", data)
            st.success("✓ Module 3 saved successfully")
            st.rerun()
