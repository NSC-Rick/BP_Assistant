import streamlit as st
from utils.storage import save_module_data

def render(project_id, existing_data=None):
    st.header("Module 6: Risk & Sustainability")
    st.markdown("Identify risks and outline your long-term vision.")
    
    existing_data = existing_data or {}
    
    with st.form("risk_form"):
        risk_1 = st.text_area(
            "Risk 1",
            value=existing_data.get("risk_1", ""),
            height=80
        )
        
        risk_2 = st.text_area(
            "Risk 2",
            value=existing_data.get("risk_2", ""),
            height=80
        )
        
        risk_3 = st.text_area(
            "Risk 3",
            value=existing_data.get("risk_3", ""),
            height=80
        )
        
        break_even = st.text_area(
            "Break-even Intuition",
            value=existing_data.get("break_even", ""),
            height=100
        )
        
        contingency = st.text_area(
            "Contingency Plan",
            value=existing_data.get("contingency", ""),
            height=100
        )
        
        vision = st.text_area(
            "12–24 Month Vision",
            value=existing_data.get("vision", ""),
            height=100
        )
        
        submitted = st.form_submit_button("Save Module")
        
        if submitted:
            data = {
                "risk_1": risk_1,
                "risk_2": risk_2,
                "risk_3": risk_3,
                "break_even": break_even,
                "contingency": contingency,
                "vision": vision
            }
            save_module_data(project_id, "risk", data)
            st.success("✓ Module 6 saved successfully")
            st.rerun()
