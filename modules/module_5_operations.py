import streamlit as st
from utils.storage import save_module_data

def render(project_id, existing_data=None):
    st.header("Module 5: Operations Plan")
    st.markdown("Describe how your business will operate.")
    
    existing_data = existing_data or {}
    
    with st.form("operations_form"):
        location = st.text_input(
            "Location",
            value=existing_data.get("location", "")
        )
        
        staffing_roles = st.text_area(
            "Staffing Roles (list)",
            value=existing_data.get("staffing_roles", ""),
            height=100
        )
        
        equipment = st.text_area(
            "Equipment",
            value=existing_data.get("equipment", ""),
            height=100
        )
        
        suppliers = st.text_area(
            "Suppliers",
            value=existing_data.get("suppliers", ""),
            height=100
        )
        
        regulatory = st.text_area(
            "Regulatory Considerations",
            value=existing_data.get("regulatory", ""),
            height=100
        )
        
        submitted = st.form_submit_button("Save Module")
        
        if submitted:
            data = {
                "location": location,
                "staffing_roles": staffing_roles,
                "equipment": equipment,
                "suppliers": suppliers,
                "regulatory": regulatory
            }
            save_module_data(project_id, "operations", data)
            st.success("✓ Module 5 saved successfully")
            st.rerun()
