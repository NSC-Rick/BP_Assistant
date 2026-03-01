# BP_Web Quick Start Guide

## Installation

1. **Install Streamlit** (if not already installed):
```bash
pip install streamlit
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## Using Client Mode

1. Click **"Enter Client Mode"**
2. Create a new project or load an existing one
3. Complete the 6 modules in order:
   - Module 1: Business Snapshot
   - Module 2: Problem & Opportunity
   - Module 3: Market & Customers
   - Module 4: Revenue Model
   - Module 5: Operations Plan
   - Module 6: Risk & Sustainability
4. Click **"Generate Draft"** in the sidebar
5. Your structured business plan is ready!

## Using Advisor Mode

1. Click **"Enter Advisor Mode"**
2. Select a project to review
3. Check completeness flags (if any)
4. View raw module data (expandable)
5. Edit the structured draft
6. Click **"Save Revised Draft"**

## Data Location

All projects are saved as JSON files in:
```
c:/Users/reeco/NSBI/BP_Web/data/plans/
```

## Tips

- **Auto-save**: Each module saves automatically when you click "Save Module"
- **Progress**: Track completion in the sidebar (X/6 modules)
- **Navigation**: Use sidebar buttons to move between modules
- **Regenerate**: Advisors can regenerate drafts from module data anytime
- **No calculations**: Revenue estimates are text-only (by design)

## Troubleshooting

**Issue**: Application won't start  
**Solution**: Ensure Streamlit is installed: `pip install streamlit`

**Issue**: Changes not saving  
**Solution**: Click "Save Module" button after entering data

**Issue**: Draft is empty  
**Solution**: Click "Generate Draft" button in sidebar

## Next Steps

After completing your business plan:
1. Copy the draft text for external use
2. Export to your preferred format (copy/paste)
3. Continue refining in Advisor Mode
4. Create additional projects as needed

---

**Need Help?** See `README.md` for full documentation
