import streamlit as st
from utils.storage import save_module_data

def render(project_id, existing_data=None):
    st.header("Module 2: Problem & Opportunity")
    st.markdown("Define the problem your business solves.")
    
    existing_data = existing_data or {}
    
    with st.form("problem_form"):
        problem_statement = st.text_area(
            "Problem Statement",
            value=existing_data.get("problem_statement", ""),
            height=150
        )
        
        affected_customer = st.text_area(
            "Affected Customer",
            value=existing_data.get("affected_customer", ""),
            height=100
        )
        
        consequence = st.text_area(
            "Consequence of Inaction",
            value=existing_data.get("consequence", ""),
            height=100
        )
        
        why_now = st.text_area(
            "Why Now",
            value=existing_data.get("why_now", ""),
            height=100
        )
        
        submitted = st.form_submit_button("Save Module")
        
        if submitted:
            data = {
                "problem_statement": problem_statement,
                "affected_customer": affected_customer,
                "consequence": consequence,
                "why_now": why_now
            }
            save_module_data(project_id, "problem", data)
            st.success("✓ Module 2 saved successfully")
            st.rerun()
