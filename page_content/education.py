import streamlit as st

def education_page():
    st.markdown("## Education")
    
    st.markdown("""
    ### Master of Science in Marketing
    **Chinese University of Hong Kong** | *Aug. 2024 - Nov. 2025*
    
    - GPA: 3.8/4.0
    - Main Courses: Marketing Management, Marketing Research, Digital Marketing, Machine Learning in Marketing, etc.
    
    ### Bachelor of Economics
    **Zhongnan University of Economics and Law** | *Sept. 2019 - Jun. 2023*
    
    - GPA: 3.5/4.0
    - Main Courses: Microeconomics, Macroeconomics, Statistics, Econometrics, International Economics, etc.
    - Honors: Outstanding Student Leader, Outstanding Youth League Member, “Xixian Cup” Campus Debate Team Runner-up
    """)
    
    st.markdown("---")
    
    st.markdown("## Certifications")

    cert1, cert2 = st.columns(2)

    with cert1:
        st.markdown("""
        ### Japanese-Language Proficiency Test-N2
        **Japan Foundation** | *Jul. 2024*
                    
        Demonstrated expertise in Japanese knowledge, reading ability, and listening ability
    """)
        
    with cert2:
        st.markdown("""
        ### Test of Proficiency in Korean-Level 4
        **National Institute for International Education** | *Apr. 2024*
                    
        Demonstrated expertise in Reading, listening, speaking and writing of the Korean language
    """)

    st.markdown("---") 