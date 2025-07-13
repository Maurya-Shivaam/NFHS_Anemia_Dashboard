## NFHS Anemia Dashboard:
An interactive Streamlit web app to explore anemia-related indicators from the National Family Health Survey (NFHS) dataset. This tool simplifies complex public health data into clean, visual insights across Indian states and union territories.

## Features:
📂 Upload NFHS Excel datasets (.xlsx)
🧹 Auto-cleans column names and filters out national aggregates
🔢 Converts survey indicators into numeric format
📈 Visualize data using:
1.Bar Chart
2.Histogram
3.Boxplot
4.Line Chart
5.Pie Chart (Top 10 States/UTs)
📌 Summary statistics for any selected indicator
⬇️ Download cleaned dataset as CSV

## How to Use:
1.Clone the repository:
git clone https://github.com/yourusername/nfhs-anemia-dashboard.git
cd nfhs-anemia-dashboard

2.Install dependencies:
pip install -r requirements.txt

3.Run the Streamlit app:
streamlit run streamlit_app.py

4.Upload your NFHS Excel file (e.g., NFHS4_Anemia_Data_Final.xlsx)
5.Select an indicator and choose a chart type to visualize

## Requirements:
streamlit
pandas
matplotlib
seaborn
openpyxl
