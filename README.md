🌍 Pollution Data Analysis Project
This project focuses on the analysis and visualization of pollution data using Python and its data science libraries. The aim is to identify pollution levels, types, patterns across cities, and derive insights useful for environmental studies and action planning.

📁 Dataset
The dataset used in this project is python.xlsx, which includes pollution-related data across multiple cities.

Key Columns:
city: Name of the city

pollutant_id: Type of pollutant (e.g., PM2.5, NO2)

pollutant_min: Minimum pollution level recorded

pollutant_max: Maximum pollution level recorded

pollutant_avg: Average pollution level

last_update: Last date the data was updated

🎯 Objectives & Insights
The project allows users to perform multiple analyses interactively. Each objective was tied to visualizations and summaries to uncover hidden patterns:

Distribution of Average Pollution

Visualized using a histogram to understand overall air quality spread.

City-wise Average Pollution Levels

Bar chart comparing pollution averages among cities.

Pollution Types in Top 20 Most Polluted Cities

Scatter plot showing pollution types across the 20 cities with highest averages.

Top 10 Most Polluted Cities

Bar plot of cities with the highest average pollution.

Outlier Detection

Box plot for spotting extreme pollution levels.

Pollution Types Distribution

Pie chart showing frequency of each pollutant type.

Correlation Heatmap

Relationship among min, max, and average pollution levels.

Outlier Removal using IQR

Interquartile Range (IQR) method used to remove outliers and re-plot histograms.

Custom Analysis Mode

Users can select what type of chart to create and choose the data to analyze, such as line, bar, scatter, etc.

📊 Interactive Features
Menu-based console app: User chooses analysis via menu (options 1-9)

User-defined analysis: A "Create Your Own Analysis" option lets users:

Select columns

Choose chart type (bar, line, scatter, pie)

Generate custom plots

Missing Value Handling:

Prompts user to choose strategy for filling missing data (mean, median, or mode)

Repeats until user exits (press 0 or type exit)

🧹 Data Cleaning & Preprocessing
Checked and imputed missing values using user-selected methods

Converted last_update to proper datetime format

Removed duplicates for clean analysis

Handled outliers using IQR

Filtered top polluted cities for focused visualization

🛠️ Technologies Used
Python – Core programming

Pandas – Data handling

NumPy – Numeric operations

Matplotlib & Seaborn – Visualization

📌 Conclusion
This pollution analysis project provides:

Clear visual trends of pollution across cities and pollutants

Interactive exploration for users of all levels

Insightful analytics such as correlation, outlier spotting, and top city rankings

Flexibility to generate new charts based on user input

It is an ideal tool for researchers, students, analysts, and environmental enthusiasts to study pollution patterns and make informed decisions or recommendations.
