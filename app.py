import streamlit as st
from utils.storage import create_project, load_project, list_existing_projects, update_structured_draft
from modules import (
    module_1_snapshot,
    module_2_problem,
    module_3_market,
    module_4_revenue,
    module_5_operations,
    module_6_risk
)
from modules.output_engine import generate_structured_plan, check_completeness

st.set_page_config(
    page_title="BP_Web - Business Plan Builder",
    page_icon="📊",
    layout="wide"
)

def init_session_state():
    if "mode" not in st.session_state:
        st.session_state.mode = None
    if "project_id" not in st.session_state:
        st.session_state.project_id = None
    if "current_module" not in st.session_state:
        st.session_state.current_module = "snapshot"

init_session_state()

st.title("📊 BP_Web - Business Plan Builder")
st.markdown("**Lightweight MVP for structured business plan development**")
st.divider()

if st.session_state.mode is None:
    st.subheader("Select Mode")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 👤 Client Mode")
        st.markdown("Create a new business plan through structured modules")
        if st.button("Enter Client Mode", use_container_width=True):
            st.session_state.mode = "client"
            st.rerun()
    
    with col2:
        st.markdown("### 🔍 Advisor Mode")
        st.markdown("Review and edit existing business plans")
        if st.button("Enter Advisor Mode", use_container_width=True):
            st.session_state.mode = "advisor"
            st.rerun()

elif st.session_state.mode == "client":
    
    if st.session_state.project_id is None:
        st.subheader("Client Mode: Create or Load Project")
        
        tab1, tab2 = st.tabs(["Create New Project", "Load Existing Project"])
        
        with tab1:
            with st.form("new_project_form"):
                project_name = st.text_input("Project Name")
                create_btn = st.form_submit_button("Create Project")
                
                if create_btn and project_name:
                    project_id = create_project(project_name)
                    st.session_state.project_id = project_id
                    st.success(f"✓ Project '{project_name}' created")
                    st.rerun()
        
        with tab2:
            projects = list_existing_projects()
            if projects:
                for proj in projects:
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.markdown(f"**{proj['project_name']}**")
                        st.caption(f"Last modified: {proj['last_modified'][:10]}")
                    with col2:
                        if st.button("Load", key=proj['project_id']):
                            st.session_state.project_id = proj['project_id']
                            st.rerun()
            else:
                st.info("No existing projects found")
        
        if st.button("← Back to Mode Selection"):
            st.session_state.mode = None
            st.rerun()
    
    else:
        project_data = load_project(st.session_state.project_id)
        
        st.sidebar.title("Navigation")
        st.sidebar.markdown(f"**Project:** {project_data['project_name']}")
        st.sidebar.divider()
        
        modules = {
            "snapshot": "1. Snapshot",
            "problem": "2. Problem",
            "market": "3. Market",
            "revenue": "4. Revenue",
            "operations": "5. Operations",
            "risk": "6. Risk"
        }
        
        st.sidebar.subheader("Modules")
        for key, label in modules.items():
            completed = bool(project_data['modules'].get(key))
            icon = "✓" if completed else "○"
            if st.sidebar.button(f"{icon} {label}", key=f"nav_{key}", use_container_width=True):
                st.session_state.current_module = key
                st.rerun()
        
        st.sidebar.divider()
        
        completed_count = sum(1 for m in project_data['modules'].values() if m)
        st.sidebar.progress(completed_count / 6)
        st.sidebar.caption(f"Progress: {completed_count}/6 modules")
        
        st.sidebar.divider()
        
        if st.sidebar.button("📄 Generate Draft", use_container_width=True):
            draft = generate_structured_plan(project_data)
            update_structured_draft(st.session_state.project_id, draft)
            st.sidebar.success("✓ Draft generated")
            st.rerun()
        
        if st.sidebar.button("← Back to Projects"):
            st.session_state.project_id = None
            st.session_state.current_module = "snapshot"
            st.rerun()
        
        if st.sidebar.button("← Change Mode"):
            st.session_state.mode = None
            st.session_state.project_id = None
            st.session_state.current_module = "snapshot"
            st.rerun()
        
        module_data = project_data['modules'].get(st.session_state.current_module, {})
        
        if st.session_state.current_module == "snapshot":
            module_1_snapshot.render(st.session_state.project_id, module_data)
        elif st.session_state.current_module == "problem":
            module_2_problem.render(st.session_state.project_id, module_data)
        elif st.session_state.current_module == "market":
            module_3_market.render(st.session_state.project_id, module_data)
        elif st.session_state.current_module == "revenue":
            module_4_revenue.render(st.session_state.project_id, module_data)
        elif st.session_state.current_module == "operations":
            module_5_operations.render(st.session_state.project_id, module_data)
        elif st.session_state.current_module == "risk":
            module_6_risk.render(st.session_state.project_id, module_data)

elif st.session_state.mode == "advisor":
    
    if st.session_state.project_id is None:
        st.subheader("Advisor Mode: Select Project")
        
        projects = list_existing_projects()
        if projects:
            for proj in projects:
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"**{proj['project_name']}**")
                    st.caption(f"Last modified: {proj['last_modified'][:10]}")
                with col2:
                    if st.button("Review", key=proj['project_id']):
                        st.session_state.project_id = proj['project_id']
                        st.rerun()
        else:
            st.info("No projects available for review")
        
        if st.button("← Back to Mode Selection"):
            st.session_state.mode = None
            st.rerun()
    
    else:
        project_data = load_project(st.session_state.project_id)
        
        st.sidebar.title("Advisor Tools")
        st.sidebar.markdown(f"**Project:** {project_data['project_name']}")
        st.sidebar.divider()
        
        if st.sidebar.button("← Back to Projects"):
            st.session_state.project_id = None
            st.rerun()
        
        if st.sidebar.button("← Change Mode"):
            st.session_state.mode = None
            st.session_state.project_id = None
            st.rerun()
        
        st.header("Advisor Review")
        
        flags = check_completeness(project_data)
        if flags:
            st.warning("**Completeness Flags:**")
            for flag in flags:
                st.markdown(f"- {flag}")
            st.divider()
        
        with st.expander("📋 View Raw Module Data", expanded=False):
            st.json(project_data['modules'])
        
        st.divider()
        st.subheader("Structured Draft")
        
        if not project_data.get('structured_draft'):
            st.info("No draft generated yet. Generate one from the module data.")
            if st.button("Generate Draft Now"):
                draft = generate_structured_plan(project_data)
                update_structured_draft(st.session_state.project_id, draft)
                st.rerun()
        else:
            st.markdown("**Current Draft:**")
            edited_draft = st.text_area(
                "Edit the draft below:",
                value=project_data['structured_draft'],
                height=600,
                key="draft_editor"
            )
            
            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button("💾 Save Revised Draft", use_container_width=True):
                    update_structured_draft(st.session_state.project_id, edited_draft)
                    st.success("✓ Draft saved")
                    st.rerun()
            
            with col2:
                if st.button("🔄 Regenerate from Modules", use_container_width=True):
                    draft = generate_structured_plan(project_data)
                    update_structured_draft(st.session_state.project_id, draft)
                    st.success("✓ Draft regenerated")
                    st.rerun()
