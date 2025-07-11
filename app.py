import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="NFHS Anemia Dashboard", layout="wide")
st.title("📊 NFHS Anemia Data Explorer")

uploaded_file = st.file_uploader("Upload the NFHS Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    # Clean column names
    df.columns = df.columns.str.strip().str.replace("\n", " ").str.replace("’", "'")

    # Remove 'India' aggregate row
    df = df[df["State/UT"] != "India"].copy()

    # Convert numeric columns
    numeric_cols = df.columns[3:]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

    st.subheader("📍 Data Preview")
    st.dataframe(df)

    # Select a column for visualization
    col_to_plot = st.selectbox("Select Indicator to Visualize", options=numeric_cols)

    # Select chart type
    chart_type = st.selectbox("Choose Chart Type", ["Bar Chart", "Histogram", "Boxplot", "Line Chart", "Pie Chart"])

    st.subheader(f"📊 {chart_type}")

    if chart_type == "Bar Chart":
        df_sorted = df.sort_values(col_to_plot, ascending=False)
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(data=df_sorted, x=col_to_plot, y="State/UT", palette="viridis", ax=ax)
        ax.set_title(f"{col_to_plot} across States/UTs")
        st.pyplot(fig)

    elif chart_type == "Histogram":
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(df[col_to_plot], kde=True, color="skyblue", ax=ax)
        ax.set_title(f"Distribution of {col_to_plot}")
        st.pyplot(fig)

    elif chart_type == "Boxplot":
        fig, ax = plt.subplots(figsize=(10, 3))
        sns.boxplot(x=df[col_to_plot], color="lightgreen", ax=ax)
        ax.set_title(f"Boxplot of {col_to_plot}")
        st.pyplot(fig)

    elif chart_type == "Line Chart":
        df_sorted = df.sort_values("State/UT")
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(df_sorted["State/UT"], df_sorted[col_to_plot], marker="o")
        ax.set_title(f"{col_to_plot} Line Chart")
        ax.set_xlabel("State/UT")
        ax.set_ylabel(col_to_plot)
        plt.xticks(rotation=90)
        st.pyplot(fig)

    elif chart_type == "Pie Chart":
        df_sorted = df.sort_values(col_to_plot, ascending=False).head(10)  # Top 10 for clarity
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(df_sorted[col_to_plot], labels=df_sorted["State/UT"], autopct="%1.1f%%", startangle=140)
        ax.set_title(f"Top 10 States by {col_to_plot}")
        st.pyplot(fig)

    # Summary Stats
    st.subheader("📌 Summary Statistics")
    st.write(df[col_to_plot].describe())

    # Download cleaned data
    st.subheader("⬇️ Download Cleaned Data")
    @st.cache_data
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df(df)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='nfhs_cleaned.csv',
        mime='text/csv',
    )
else:
    st.warning("Please upload an NFHS Excel file to begin.")
# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 16px;'>Made with ❤️ by <b>Shivam Maurya</b> | AI/ML Engineer</p>",
    unsafe_allow_html=True
)
