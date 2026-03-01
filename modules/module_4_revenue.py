import streamlit as st
from utils.storage import save_module_data

def render(project_id, existing_data=None):
    st.header("Module 4: Revenue Model")
    st.markdown("Define up to 3 revenue streams.")
    
    existing_data = existing_data or {}
    streams = existing_data.get("streams", [])
    
    while len(streams) < 3:
        streams.append({
            "name": "",
            "pricing_method": "",
            "sales_frequency": "",
            "estimated_volume": "",
            "seasonality": "No"
        })
    
    with st.form("revenue_form"):
        revenue_streams = []
        
        for i in range(3):
            st.subheader(f"Revenue Stream {i+1}")
            
            name = st.text_input(
                f"Name",
                value=streams[i].get("name", ""),
                key=f"stream_name_{i}"
            )
            
            pricing_method = st.text_input(
                f"Pricing Method",
                value=streams[i].get("pricing_method", ""),
                key=f"pricing_{i}"
            )
            
            sales_frequency = st.text_input(
                f"Sales Frequency",
                value=streams[i].get("sales_frequency", ""),
                key=f"frequency_{i}"
            )
            
            estimated_volume = st.text_input(
                f"Estimated Monthly Volume (text)",
                value=streams[i].get("estimated_volume", ""),
                key=f"volume_{i}"
            )
            
            seasonality = st.radio(
                f"Seasonality",
                options=["Yes", "No"],
                index=0 if streams[i].get("seasonality", "No") == "Yes" else 1,
                key=f"seasonality_{i}",
                horizontal=True
            )
            
            revenue_streams.append({
                "name": name,
                "pricing_method": pricing_method,
                "sales_frequency": sales_frequency,
                "estimated_volume": estimated_volume,
                "seasonality": seasonality
            })
            
            if i < 2:
                st.divider()
        
        submitted = st.form_submit_button("Save Module")
        
        if submitted:
            data = {"streams": revenue_streams}
            save_module_data(project_id, "revenue", data)
            st.success("✓ Module 4 saved successfully")
            st.rerun()
