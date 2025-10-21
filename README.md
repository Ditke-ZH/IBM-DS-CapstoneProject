# 🚀 Winning the Space Race with Data Science  
### IBM Data Science Capstone Project – SpaceX Falcon 9 Launch Prediction

![Bangabandhu_Satellite-1_Mission_(42025498972)](https://github.com/user-attachments/assets/8f73c7d1-509e-44a1-94a3-2aba0213452a)


This project is the final capstone of the **IBM Data Science Professional Certificate**.  
It applies end-to-end data science techniques — from data collection to machine learning — to analyze and predict **SpaceX Falcon 9 first-stage landing success**.

---

## 🧭 Project Overview

SpaceX’s innovation in **reusable rocket boosters** has revolutionized space travel, drastically reducing launch costs.  
This project investigates which factors determine **landing success** and builds predictive models to forecast outcomes.

**Goals:**
- Collect and clean real-world launch data from multiple sources  
- Perform **Exploratory Data Analysis (EDA)** using Python, SQL, and visualization  
- Create **interactive geospatial** and **analytical dashboards**  
- Build and evaluate **machine learning models** to predict landing success  

---

## 🗂 Repository Structure

```
├── jupyter-labs-spacex-data-collection-api.ipynb           # Data retrieved from SpaceX REST API
├── jupyter-labs-spacex-data-collection-webscraping.ipynb   # Web scraping Falcon 9 data from Wikipedia
├── jupyter-labs-spacex-data-wrangling.ipynb                # Data cleaning and feature engineering
├── jupyter-labs-spacex-eda-visualization.ipynb             # Exploratory Data Analysis using Python & Plotly
├── jupyter-labs-spacex-eda-with-sql.ipynb                  # SQL-based EDA using SQLite
├── jupyter-labs-spacex-launch-site-location-folium.ipynb   # Interactive map visualization using Folium
├── spacex-dash-app.py                                      # Plotly Dash interactive web dashboard
├── jupyter-labs-spacex-machine-learning-prediction.ipynb   # Predictive modeling (classification)
├── ds-capstone-presentation.pdf                            # Final presentation slides
└── README.md                                               # Project documentation
```

---

## 🧩 Methodology

### 1️⃣ Data Collection
- **SpaceX REST API:** Used Python `requests` to fetch historical Falcon 9 launch data.  
- **Web Scraping:** Extracted complementary data (booster version, payload type, orbit) from Wikipedia using **BeautifulSoup**.  
- Combined both datasets into a unified pandas DataFrame.

### 2️⃣ Data Wrangling
- Cleaned and standardized data columns.  
- Handled missing payload values and created a binary **target variable (`class`)** for success/failure.  
- Final dataset contained over **90 launch records** with features such as payload mass, orbit, site, and landing outcome.

### 3️⃣ Exploratory Data Analysis (EDA)
- Conducted **visual EDA** using **Matplotlib**, **Seaborn**, and **Plotly**.
- Performed **SQL EDA** in SQLite to query patterns in success rate, payload, orbit, and booster type.
- Discovered:
  - Success rates improved over time (notably post-2016).  
  - Payload and orbit strongly influence mission outcome.  
  - VAFB SLC-4E shows the **highest success rate**, though with fewer launches.

### 4️⃣ Interactive Visual Analytics
- **Folium Map:** Mapped launch sites with markers and environmental distances (roads, coasts, railways).  
- **Plotly Dash Dashboard:**  
  - Dropdown for site selection  
  - Pie chart for success rates  
  - Payload range slider  
  - Scatter plot showing payload–success correlation  

### 5️⃣ Predictive Modeling
- Trained supervised learning models to predict landing success:
  - Logistic Regression  
  - Support Vector Machine (SVM)  
  - K-Nearest Neighbors (KNN)  
  - Decision Tree Classifier  
- Used **GridSearchCV** for hyperparameter tuning and 10-fold cross-validation.  
- **Best Model:** Decision Tree – **94% accuracy on test data**.

---

## 📊 Results & Insights

| Focus Area | Key Finding |
|-------------|--------------|
| **Launch Sites** | KSC LC-39A handled most missions; VAFB SLC-4E had highest success rate |
| **Payload Range** | Missions with payloads between 2000–4000 kg showed best outcomes |
| **Orbit Type** | GTO and SSO orbits presented more variability in success |
| **Booster Version** | Block 5 and Full Thrust boosters demonstrated top performance |
| **Modeling** | Decision Tree achieved the highest accuracy (94%), generalizing well to unseen data |

---

## 🌍 Interactive Components

### 🗺️ [Folium Map – Launch Site Visualization](./jupyter-labs-spacex-launch-site-location-folium.ipynb)
- Displays launch site locations and outcomes (success/failure)
- Includes proximity analysis to coastlines and infrastructure

### 📊 [Plotly Dash Dashboard](./spacex-dash-app.py)
- Real-time interaction using dropdowns and sliders
- Visualizes success rates, payload impact, and mission correlation

Run locally:
```bash
python spacex-dash-app.py
```
Then open `http://127.0.0.1:8050` in your browser.

---

## 🤖 Predictive Model Performance

| Model | Test Accuracy |
|--------|----------------|
| Logistic Regression | 0.83 |
| Support Vector Machine (SVM) | 0.83 |
| K-Nearest Neighbors (KNN) | 0.83 |
| **Decision Tree Classifier** | **0.94** |

The **Decision Tree model** provided the best balance between interpretability and accuracy, effectively identifying success patterns from mission attributes.

---

## 🧠 Conclusions

- Data-driven analysis identified key operational factors impacting Falcon 9 landing success.  
- Interactive dashboards enable deeper exploration without manual coding.  
- Decision Tree classifier predicts outcomes with **94% accuracy**.  
- Insights can guide mission planning, risk management, and cost optimization.

---

## 🔭 Future Enhancements

- Integrate **weather and atmospheric data** for enhanced prediction.  
- Use **deep learning models** (e.g., Random Forest, Gradient Boosting).  
- Deploy dashboard as a **web service** (e.g., Heroku or Streamlit Cloud).  

---

## 👩‍💻 Author

**Edit Guntermann**  
📅 *Completed on October 21, 2025*  
🎓 *IBM Data Science Professional Certificate – Capstone Project*  
🌐 GitHub: [Ditke-ZH](https://github.com/Ditke-ZH)

---

> *“Data science fuels innovation — even in orbit.”* 🌌
