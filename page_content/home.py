import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>LU Tingxin</h4>
        <p>Recent Master's Graduate in Marketing<br>
        Chinese University of Hong Kong<br>
        12 Chak Cheung St., Ma Liu Shui, HKSAR<br>
        <a href="mailto:1155218670@link.cuhk.edu.hk">1155218670@link.cuhk.edu.hk</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "image.jpg")
    if os.path.exists(image_path):
        try:
            image = Image.open(image_path)
            right_col.image(image, width=200)
        except Exception as e:
            st.error(f"Error loading image: {str(e)}")
            right_col.warning("Could not load profile image")
    else:
        right_col.warning(f"Profile image not found at: {image_path}")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        I am currently pursuing a Master's degree in Marketing with a focus on Big Data at The Chinese University of Hong Kong, after earning my Bachelor's in Economics from Zhongnan University of Economics and Law.

        With strong analytical and communication skills, I have hands-on experience in data analysis, digital marketing, and international operations, and I'm proficient in Python, Excel, and various marketing tools.

        I'm a fast learner, highly adaptable, and passionate about consumer insights and global marketing, and I aspire to contribute to innovative, data-driven strategies in the future.
        """
    )

    st.markdown(
        """
        ### Skills and Self-Evaluation
        - Programming Languages: Python, R, SQL
        - Data Analysis: Pandas, NumPy, Matplotlib, Seaborn
        - Data Visualization: Tableau, Power BI
        - Office Skills: MS Office (Excel, PowerPoint, Word, Outlook), Adobe (Photoshop, Premiere)
        - Language Skills: English (CET-6: 599, IELTS: 7.5, GRE Verbal: 159), Japanese (N2), Korean (TOPIK-Level 4), Mandarin(Native), Cantonese(Native)
        - Self-Evaluation: Personal Evaluation: Strong learning ability, stress resilience, and logical thinking. Skilled in multi-tasking;; responsible, enthusiastic in work
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 