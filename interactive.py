import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Streamlit Page Config
st.set_page_config(page_title="🌍 Pollution Insights Dashboard", layout="wide")

# App Header
st.title("🌱 Pollution Data Explorer")
st.markdown("""
Use this interactive dashboard to explore pollution metrics city-wise. 
Upload your dataset and visualize trends, types, outliers, and custom comparisons.
""")

# Upload Dataset
uploaded_file = st.file_uploader("📂 Upload your pollution dataset (.xlsx)", type="xlsx")

if uploaded_file is not None:
    # Load Data
    data = pd.read_excel(uploaded_file)
    st.success("Dataset uploaded successfully!")

    # Initial View
    with st.expander("📊 Preview Dataset"):
        st.dataframe(data.head(10))

    # Clean Missing Values
    st.subheader("🛠️ Data Cleaning")
    method = st.selectbox("Choose method to handle missing values:",
                          ["Fill with Mean", "Fill with Median", "Fill with Mode", "Drop Rows"])

    num_cols = ['pollutant_min', 'pollutant_max', 'pollutant_avg']
    if method == "Fill with Mean":
        for col in num_cols:
            data[col] = data[col].fillna(data[col].mean())
        st.info("Filled with Mean")
    elif method == "Fill with Median":
        for col in num_cols:
            data[col] = data[col].fillna(data[col].median())
        st.info("Filled with Median")
    elif method == "Fill with Mode":
        for col in num_cols:
            data[col] = data[col].fillna(data[col].mode()[0])
        st.info("Filled with Mode")
    elif method == "Drop Rows":
        data.dropna(inplace=True)
        st.info("Dropped rows with missing values")

    # Remove Duplicates
    data.drop_duplicates(inplace=True)

    # Navigation Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Prebuilt Analysis", "🎨 Custom Visualization", "📌 Outliers", "📋 Dataset Info"])

    with tab1:
        st.header("Prebuilt Visualizations")
        option = st.selectbox("Choose an objective:", [
            "Histogram - Pollutant Average",
            "Bar Chart - Avg Pollution by City",
            "Scatter - Pollution Type in Top 20 Cities",
            "Top 10 Most Polluted Cities",
            "Box Plot - Outlier Detection",
            "Pie Chart - Pollution Types",
            "Correlation Heatmap"
        ])

        fig, ax = plt.subplots(figsize=(12, 6))

        if option == "Histogram - Pollutant Average":
            ax.hist(data['pollutant_avg'], bins=30, color='skyblue', edgecolor='black')
            ax.set_title("Distribution of Pollutant Averages")
        elif option == "Bar Chart - Avg Pollution by City":
            city_avg = data.groupby('city')['pollutant_avg'].mean().sort_values(ascending=False)
            city_avg.plot(kind='bar', color='orange', ax=ax)
            ax.set_title("Average Pollution by City")
        elif option == "Scatter - Pollution Type in Top 20 Cities":
            top_cities = data.groupby('city')['pollutant_avg'].mean().sort_values(ascending=False).head(20).index
            top_data = data[data['city'].isin(top_cities)]
            for pollutant in top_data['pollutant_id'].unique():
                pol = top_data[top_data['pollutant_id'] == pollutant]
                ax.scatter(pol['city'], pol['pollutant_avg'], label=pollutant)
            ax.set_title("Pollution by Type in Top 20 Cities")
            ax.legend()
            plt.xticks(rotation=90)
        elif option == "Top 10 Most Polluted Cities":
            top10 = data.groupby('city')['pollutant_avg'].mean().sort_values(ascending=False).head(10)
            top10.plot(kind='bar', color='red', ax=ax)
            ax.set_title("Top 10 Polluted Cities")
        elif option == "Box Plot - Outlier Detection":
            ax.boxplot(data['pollutant_avg'], vert=False)
            ax.set_title("Outlier Detection in Pollutant Avg")
        elif option == "Pie Chart - Pollution Types":
            type_counts = data['pollutant_id'].value_counts()
            ax.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140)
            ax.set_title("Pollution Type Distribution")
        elif option == "Correlation Heatmap":
            corr = data[num_cols].corr()
            fig, ax = plt.subplots()
            sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
            st.pyplot(fig)
            st.stop()

        st.pyplot(fig)

    with tab2:
        st.header("Custom Visualization")
        chart_type = st.selectbox("Chart Type", ["Bar", "Line", "Scatter", "Box", "Histogram"])
        x = st.selectbox("X-axis", data.columns)
        y = st.selectbox("Y-axis (numerical)", data.select_dtypes(include=np.number).columns)

        fig, ax = plt.subplots()
        if chart_type == "Bar":
            data.groupby(x)[y].mean().plot(kind='bar', ax=ax)
        elif chart_type == "Line":
            data.groupby(x)[y].mean().plot(kind='line', ax=ax)
        elif chart_type == "Scatter":
            ax.scatter(data[x], data[y], color='teal')
        elif chart_type == "Box":
            sns.boxplot(x=data[x], y=data[y], ax=ax)
        elif chart_type == "Histogram":
            sns.histplot(data[y], kde=True, ax=ax)
        ax.set_title(f"{chart_type} Plot: {y} vs {x}")
        st.pyplot(fig)

    with tab3:
        st.header("🔍 Outlier Detection (IQR Method)")
        Q1 = np.percentile(data['pollutant_avg'], 25)
        Q3 = np.percentile(data['pollutant_avg'], 75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        outliers = data[(data['pollutant_avg'] < lower) | (data['pollutant_avg'] > upper)]
        st.warning(f"Found {len(outliers)} outliers in pollutant_avg")
        st.dataframe(outliers[['city', 'pollutant_id', 'pollutant_avg']])

        clean_data = data[(data['pollutant_avg'] >= lower) & (data['pollutant_avg'] <= upper)]
        fig, ax = plt.subplots()
        sns.histplot(clean_data['pollutant_avg'], bins=30, kde=True, color='green', ax=ax)
        ax.set_title("Pollutant Average (Outliers Removed)")
        st.pyplot(fig)

    with tab4:
        st.header("📋 Dataset Overview")
        st.markdown("#### Column Descriptions")
        st.dataframe(pd.DataFrame({
            'Column': data.columns,
            'Data Type': [str(data[col].dtype) for col in data.columns],
            'Missing Values': [data[col].isna().sum() for col in data.columns],
        }))

        st.markdown("#### Dataset Summary")
        st.write(data.describe())

else:
    st.info("Please upload an Excel file to begin analysis.")
