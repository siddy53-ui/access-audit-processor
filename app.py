import streamlit as st
import pandas as pd
import os
from process_audit import process_audit_logs

# Configure the Streamlit page
st.set_page_config(page_title="Enterprise Access Auditor", layout="wide")

st.title("Enterprise Access Auditor")
st.markdown("Automated processing, validation, and visualization of endpoint security logs.")

# File uploader and optional inputs
uploaded_file = st.file_uploader("Upload Raw Audit CSV", type=['csv'])
analyst = st.text_input("Analyst Name (Optional)", value="Sourav")

if uploaded_file is not None:
    # 1. Preview and Visualize Raw Data
    raw_df = pd.read_csv(uploaded_file)
    
    st.subheader("Data Overview")
    with st.expander("Preview Uploaded Data"):
        st.dataframe(raw_df.head(10))
        
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Event Type Distribution**")
        st.bar_chart(raw_df['Event_Type'].value_counts())
    with col2:
        st.write("**Target Group Distribution**")
        st.bar_chart(raw_df['Target_Group'].value_counts())

    # 2. Trigger the Backend Processing
    if st.button("Generate Audit Report"):
        with st.spinner("Applying exclusion rules and deduplicating..."):
            # Save uploaded file temporarily for the processor to read
            temp_input = "temp_uploaded_logs.csv"
            output_excel = "Processed_Audit_Report.xlsx"
            
            with open(temp_input, "wb") as f:
                f.write(uploaded_file.getbuffer())
                
            # Execute the core logic from process_audit.py
            total, valid, excluded, duplicates = process_audit_logs(
                temp_input, 
                output_excel, 
                analyst_name=analyst
            )
            
            # Clean up the temporary input file
            if os.path.exists(temp_input):
                os.remove(temp_input)
                
            st.success("Processing Complete!")
            
            # 3. Display Processing Metrics
            st.subheader("Processing Summary")
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Total Rows", total)
            m2.metric("Valid Records (BAU)", valid)
            m3.metric("Exclusions Removed", excluded)
            m4.metric("Duplicates Removed", duplicates)
            
            # 4. Provide the Download Button
            with open(output_excel, "rb") as excel_file:
                st.download_button(
                    label="Download Excel Workbook",
                    data=excel_file,
                    file_name="Validated_Audit_Report.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )