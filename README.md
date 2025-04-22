# 🌍 Pollution Data Analysis Dashboard

An interactive **Streamlit** dashboard to analyze and visualize air pollution data across cities. Gain insights from trends, detect outliers, and understand pollutant patterns using powerful charts and easy-to-use controls.

---

## 📁 Dataset

**File:** `python.xlsx`  
The dataset contains pollution data collected from various cities. It includes details such as pollutant types, pollution levels, and the date of last update.

**Key Columns:**

- `city`: Name of the city
- `pollutant_id`: Type of pollutant (e.g., PM2.5, NO2)
- `pollutant_min`: Minimum pollution level
- `pollutant_max`: Maximum pollution level
- `pollutant_avg`: Average pollution level
- `last_update`: Date when the record was last updated

---

## 🎯 Project Objectives

The app provides insights into:

- 📊 **Distribution of Average Pollution Levels** – Histogram
- 🏙️ **City-wise Pollution Comparison** – Bar Chart
- 🌐 **Pollution Type Patterns** – Scatter Plot
- 🚩 **Top 10 Most Polluted Cities** – Bar Chart
- 📦 **Outlier Detection** – Box Plot
- 🧪 **Pollutant Type Distribution** – Pie Chart
- 📈 **Correlation of Pollution Metrics** – Heatmap
- 🔎 **Outlier Removal (IQR method)** – Cleaned Histogram
- 🧠 **User-defined Analysis** – Choose your chart and data

---

## 🧹 Data Preprocessing

- Handled missing values with user-selected strategies (mean, median, mode)
- Converted `last_update` to proper `datetime` format
- Removed duplicate entries
- Detected and removed outliers using IQR (Interquartile Range)
- Filtered top polluted cities for clearer visual insights

---

## 💻 App Features

- ✅ Dropdown-based visualization selector
- ⚙️ Missing value imputation options
- 🔄 Real-time plot updates
- 📋 Dataset overview (Head, Tail, Info, Describe)
- 📌 Outlier removal
- 🛠️ **"Create Your Own Analysis"** option (select chart type + data columns)

---

## 🛠️ Technologies Used

- **Python** – Core programming
- **Streamlit** – Interactive web interface
- **Pandas** – Data manipulation
- **NumPy** – Numerical operations
- **Matplotlib** – Basic plotting
- **Seaborn** – Statistical data visualization
- **OpenPyXL** – Read Excel files

---

## ▶️ How to Run the App

```bash
# Step 1: Clone the repository
git clone https://github.com/your-username/pollution-analysis-streamlit.git
cd pollution-analysis-streamlit

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run the app
streamlit run app.py
