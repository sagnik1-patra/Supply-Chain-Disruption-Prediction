#  Supply Chain Disruption Analyzer & Map Visualizer

This project analyzes news headlines to detect trends in **supply chain disruptions** using NLP and visualizes **key supply chain locations** on an interactive **satellite map**.

---

##  Files

- `abcnews-date-text.csv`: News dataset used for NLP-based trend analysis.
- `supply_chain_map.py`: Python script to visualize selected locations on an interactive map.
- `supply_chain_map.html`: Output HTML map showing key logistic hubs.
- `Screenshot 2025-08-01 130539.png`: Screenshot of NLP trend analysis results.
- `Supply.png`: Screenshot of the map output in browser.

---

##  Features

-  Extracts and plots keyword trends (like "port", "disruption", "logistics") from news headlines.
-  Interactive map shows critical supply chain cities like Singapore, Rotterdam, and Mumbai.
-  Map uses `Stamen Terrain` tiles with proper attribution.

---

##  Getting Started

### 1. Setup

Install required libraries:

```bash
pip install pandas matplotlib folium
Optional (for interactive use):

bash
Copy
Edit
pip install streamlit streamlit-folium
2. Run the Map Script
bash
Copy
Edit
python supply_chain_map.py
 Output:

bash
Copy
Edit
Map has been saved as 'supply_chain_map.html'. Open it in a browser to view.
3. Run the NLP Plotting (if using Jupyter)
Use the code below in a Jupyter cell:

python
Copy
Edit
import pandas as pd
import matplotlib.pyplot as plt

# Load news data
df = pd.read_csv("abcnews-date-text.csv")

# Filter news for relevant keywords
keywords = ["port", "disruption", "logistics", "container", "shipping"]
df['year'] = pd.to_datetime(df['publish_date'], format='%Y%m%d').dt.year

# Count keyword frequency per year
keyword_freq = {kw: df[df['headline_text'].str.contains(kw, case=False, na=False)].groupby('year').size() for kw in keywords}

# Plotting
plt.figure(figsize=(10,6))
for kw, freq in keyword_freq.items():
    freq.plot(label=kw)

plt.title("Supply Chain Keyword Frequency Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Headlines")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
 Screenshots
 Trend Analysis

 Map View


 Customization
You can add more cities by editing the locations dictionary in supply_chain_map.py:

python
Copy
Edit
locations = {
    "Singapore": (1.3521, 103.8198),
    "Rotterdam": (51.9225, 4.47917),
    "Mumbai": (19.0760, 72.8777),
    "Los Angeles": (34.0522, -118.2437),  # Add more here
}
 Attribution
Map tiles by Stamen Design, under CC BY 3.0.

Data by ABC News Headlines Dataset.

 Author
Sagnik Patra
M.Tech (2023–2025)
IIIT Trichy
