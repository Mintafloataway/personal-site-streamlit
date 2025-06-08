import streamlit as st
from components.interactive import display_interactive_chart

def experience_page():
    st.markdown("## Professional Experience")
    
    st.markdown("""
    ### Overseas Channel Operations Intern
    **Ctrip (Trip.com)** | Car Rental SBU | *Feb. 2024 - Jul. 2024*
    
    - Distribution Channel Strategy: Monitored UV, SOV, and conversion rates for Skyscanner and Kayak; adjusted pricing and supplier resources per market to increase ROI. Collaborated with the business team to optimize supplier terms
    - Direct Channel Operations Optimization: Worked with the Trip.com team to close traffic gaps in the overseas car rental business. Developed new entry points and optimized user pathways
    - Competitor Research: Analyzed competitors like Klook and Discover Cars on user profiles, pricing, and product terms, providing insights for growth strategies
    - CRM and User Reach: Designed Push and EDM strategies for Trip.com
    """)
    
    st.markdown("""
    ### Cross-border E-commerce Intern
    **Zuoyebang** | Hardware Center | *Dec. 2022 - Mar. 2023*
    
    - Data Analysis & Sales Optimization: Integrated sales and traffic data across Shopee’s sub-sites to monitor key metrics, suggesting stocking and promotional strategies
    - Advertising Optimization: Focused on keyword ads, banners, and related ads
    - Competitor & Product Selection Analysis: Analyzed top-selling products on Shopee for pricing, visuals, and customer pain points to advise on product selection
    - Shop Operations: Managed product launches, listing optimization, copy updates, and promotional strategy design
    """)
    
    st.markdown("---")
    
    st.markdown("## Projects")
    
    projects = [
        {
            "title": "Marketing Consultant Project for Towngas Telecom",
            "description": "Conducted an in-depth marketing analysis of telecom industry in mainland China and Developed a blueprint for Marketing AI Agent for Towngas Telecom",
            "skills": ["LDA analysis", "Sentiment analysis", "Statistical analysis", "Descriptive analysis"],
            "outcome": 'Key insights regarding AI marketing Agent development'
        },
        {
            "title": "Research for the structual unemployment of the disabled in Hubei, Mainland China",
            "description": "Analyzed the situation and causes of structural unemployment among the disabled",
            "skills": ["Descriptive analysis", "filed investigation", "Statistical Analyisis"],
            "outcome": "Put forward recommendations regarding facilitating employment of the disabled"
        },
    ]
    
    for i, project in enumerate(projects):
        with st.expander(f"{project['title']}", expanded=i==0):
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Skills Used:** {', '.join(project['skills'])}")
            st.markdown(f"**Outcome:** {project['outcome']}")
    
    # Add the interactive visualization demo
    with st.expander("Interactive Data Visualization Demo", expanded=False):
        st.markdown("**Description:** An interactive demonstration of various data visualization techniques.")
        display_interactive_chart()
    
    st.markdown("---")
    
    st.markdown("## Professional Skills")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R, SQL
        - **Data Processing:** Pandas, NumPy, PySpark
        - **Visualization:** Matplotlib, Seaborn, Tableau, PowerBI
        """)
        
    with col2:
        st.markdown("""
        ### Office Skills
        - **Microsoft Office:** MS Excel, PowerPoint, Word, Outlook, Teams
        - **Picture Editing:** Adobe Photoshop
        - **Video Editing:** Adobe Premiere, Capcut
        - **Others:** Xmind
        """)
    
    with col3:
        st.markdown("""
        ### Language Skills
        - **English:** IELTS-7.5, GRE-329, CET6-599
        - **Japanese:** N2
        - **Korean:** TOPIK-Level4
        - **Mandarin:** Native
        - **Cantonese:** Native
        """)

    
    st.markdown("---") 