# BP_Web - Business Plan Builder MVP

A lightweight, modular Streamlit application for structured business plan development.

## Features

- **Client Mode**: Create business plans through 6 structured modules
- **Advisor Mode**: Review and edit existing plans with completeness checks
- **Local Storage**: JSON-based data persistence
- **Deterministic Output**: Generate structured drafts from user input only

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

## Structure

```
BP_Web/
├── app.py                      # Main application
├── modules/
│   ├── module_1_snapshot.py    # Business overview
│   ├── module_2_problem.py     # Problem & opportunity
│   ├── module_3_market.py      # Market & customers
│   ├── module_4_revenue.py     # Revenue model
│   ├── module_5_operations.py  # Operations plan
│   ├── module_6_risk.py        # Risk & sustainability
│   └── output_engine.py        # Draft generation
├── utils/
│   └── storage.py              # JSON persistence
├── data/
│   └── plans/                  # Project JSON files
└── docs/
    └── windsurf_reports/       # Build reports
```

## Modules

1. **Snapshot**: Business name, location, stage, description, owner background
2. **Problem**: Problem statement, affected customers, consequences, timing
3. **Market**: Target customers, geographic reach, alternatives, differentiation
4. **Revenue**: Up to 3 revenue streams with pricing and volume estimates
5. **Operations**: Location, staffing, equipment, suppliers, regulatory
6. **Risk**: Key risks, break-even, contingency, 12-24 month vision

## Data Storage

Projects are stored as JSON files in `data/plans/` with the following structure:

```json
{
  "project_id": "uuid",
  "project_name": "string",
  "created_at": "ISO timestamp",
  "last_modified": "ISO timestamp",
  "modules": {
    "snapshot": {},
    "problem": {},
    "market": {},
    "revenue": {},
    "operations": {},
    "risk": {}
  },
  "structured_draft": "markdown text"
}
```

## MVP Constraints

- No AI rewriting
- No external APIs
- No authentication
- No financial projections
- No database layer
- Clean, minimal implementation
