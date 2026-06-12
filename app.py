import streamlit as st
import pandas as pd
from serpGoogleSearch import scalable_serp_lookup
from dotenv import load_dotenv
from io import BytesIO
import os

load_dotenv()

api_key = os.getenv("SERPAPI_KEY")


st.title("LinkedIn Profile Finder")

query = st.text_input("Enter Boolean Search String")

if st.button("Search"):
    if query.strip():
        st.write(f"Searching for: {query}")
        results = scalable_serp_lookup(f"site:linkedin.com (person) {query}", api_key)
        df = pd.DataFrame(results)
        st.dataframe(
            df,
            column_config={
                "link": st.column_config.LinkColumn(
                    "LinkedIn URL"
                )
            },
            use_container_width=True
        )
        #st.dataframe(df)

        csv = df.to_csv(index=False)

        st.download_button(
            "Download CSV",
            csv,
            file_name="candidates.csv",
            mime="text/csv"
        )

        output = BytesIO()

        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            df.to_excel(writer, index=False)

        excel_data = output.getvalue()

        st.download_button(
            "Download EXCEL",
            data=excel_data,
            file_name="candidates.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.error("Please enter a query")
    