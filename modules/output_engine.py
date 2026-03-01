def generate_structured_plan(project_data):
    modules = project_data.get("modules", {})
    snapshot = modules.get("snapshot", {})
    problem = modules.get("problem", {})
    market = modules.get("market", {})
    revenue = modules.get("revenue", {})
    operations = modules.get("operations", {})
    risk = modules.get("risk", {})
    
    sections = []
    
    sections.append("# BUSINESS PLAN")
    sections.append(f"## {snapshot.get('business_name', 'Untitled Business')}")
    sections.append("")
    sections.append("---")
    sections.append("")
    
    sections.append("## 1. EXECUTIVE SUMMARY")
    sections.append("")
    if snapshot.get("business_name"):
        sections.append(f"**Business Name:** {snapshot.get('business_name')}")
    if snapshot.get("location"):
        sections.append(f"**Location:** {snapshot.get('location')}")
    if snapshot.get("stage"):
        sections.append(f"**Stage:** {snapshot.get('stage')}")
    sections.append("")
    if snapshot.get("description"):
        sections.append("**Overview:**")
        sections.append(snapshot.get("description"))
    sections.append("")
    if snapshot.get("owner_background"):
        sections.append("**Owner Background:**")
        sections.append(snapshot.get("owner_background"))
    sections.append("")
    sections.append("---")
    sections.append("")
    
    sections.append("## 2. PROBLEM & OPPORTUNITY")
    sections.append("")
    if problem.get("problem_statement"):
        sections.append("**Problem Statement:**")
        sections.append(problem.get("problem_statement"))
        sections.append("")
    if problem.get("affected_customer"):
        sections.append("**Affected Customer:**")
        sections.append(problem.get("affected_customer"))
        sections.append("")
    if problem.get("consequence"):
        sections.append("**Consequence of Inaction:**")
        sections.append(problem.get("consequence"))
        sections.append("")
    if problem.get("why_now"):
        sections.append("**Why Now:**")
        sections.append(problem.get("why_now"))
        sections.append("")
    sections.append("---")
    sections.append("")
    
    sections.append("## 3. MARKET & CUSTOMERS")
    sections.append("")
    if market.get("primary_customer"):
        sections.append("**Primary Customer:**")
        sections.append(market.get("primary_customer"))
        sections.append("")
    if market.get("geographic_reach"):
        sections.append(f"**Geographic Reach:** {market.get('geographic_reach')}")
        sections.append("")
    if market.get("alternatives"):
        sections.append("**Alternatives:**")
        sections.append(market.get("alternatives"))
        sections.append("")
    if market.get("differentiation"):
        sections.append("**Differentiation:**")
        sections.append(market.get("differentiation"))
        sections.append("")
    sections.append("---")
    sections.append("")
    
    sections.append("## 4. REVENUE MODEL")
    sections.append("")
    streams = revenue.get("streams", [])
    active_streams = [s for s in streams if s.get("name")]
    
    if active_streams:
        for i, stream in enumerate(active_streams, 1):
            sections.append(f"### Revenue Stream {i}: {stream.get('name')}")
            if stream.get("pricing_method"):
                sections.append(f"**Pricing Method:** {stream.get('pricing_method')}")
            if stream.get("sales_frequency"):
                sections.append(f"**Sales Frequency:** {stream.get('sales_frequency')}")
            if stream.get("estimated_volume"):
                sections.append(f"**Estimated Monthly Volume:** {stream.get('estimated_volume')}")
            if stream.get("seasonality"):
                sections.append(f"**Seasonality:** {stream.get('seasonality')}")
            sections.append("")
    else:
        sections.append("*No revenue streams defined.*")
        sections.append("")
    sections.append("---")
    sections.append("")
    
    sections.append("## 5. OPERATIONS PLAN")
    sections.append("")
    if operations.get("location"):
        sections.append(f"**Location:** {operations.get('location')}")
        sections.append("")
    if operations.get("staffing_roles"):
        sections.append("**Staffing Roles:**")
        sections.append(operations.get("staffing_roles"))
        sections.append("")
    if operations.get("equipment"):
        sections.append("**Equipment:**")
        sections.append(operations.get("equipment"))
        sections.append("")
    if operations.get("suppliers"):
        sections.append("**Suppliers:**")
        sections.append(operations.get("suppliers"))
        sections.append("")
    if operations.get("regulatory"):
        sections.append("**Regulatory Considerations:**")
        sections.append(operations.get("regulatory"))
        sections.append("")
    sections.append("---")
    sections.append("")
    
    sections.append("## 6. RISK & SUSTAINABILITY")
    sections.append("")
    sections.append("**Key Risks:**")
    if risk.get("risk_1"):
        sections.append(f"1. {risk.get('risk_1')}")
    if risk.get("risk_2"):
        sections.append(f"2. {risk.get('risk_2')}")
    if risk.get("risk_3"):
        sections.append(f"3. {risk.get('risk_3')}")
    sections.append("")
    if risk.get("break_even"):
        sections.append("**Break-even Intuition:**")
        sections.append(risk.get("break_even"))
        sections.append("")
    if risk.get("contingency"):
        sections.append("**Contingency Plan:**")
        sections.append(risk.get("contingency"))
        sections.append("")
    if risk.get("vision"):
        sections.append("**12–24 Month Vision:**")
        sections.append(risk.get("vision"))
        sections.append("")
    
    return "\n".join(sections)

def check_completeness(project_data):
    flags = []
    modules = project_data.get("modules", {})
    
    revenue = modules.get("revenue", {})
    streams = revenue.get("streams", [])
    for i, stream in enumerate(streams, 1):
        if stream.get("name") and not stream.get("estimated_volume"):
            flags.append(f"Revenue stream {i} missing volume estimate")
    
    operations = modules.get("operations", {})
    if not operations.get("staffing_roles"):
        flags.append("No staffing roles entered")
    
    risk = modules.get("risk", {})
    if not risk.get("risk_1") and not risk.get("risk_2") and not risk.get("risk_3"):
        flags.append("No risks entered")
    
    return flags
