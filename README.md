# Data Analytics Portfolio

Welcome to my data analytics portfolio! This repository showcases projects that demonstrate my skills in Python, SQL, Excel, and real-world data analysis. 

This portfolio is a **journey**: starting with foundational analyses and building toward more advanced, data-driven insights. Check back for new projects as I continue to expand my analytics skills.

---

## 1. Uber Driving Analysis — Expected Earnings & Surge Probability

**Overview:**  
This was my **first practical analytics project**, designed to apply foundational data analysis techniques to a real-world dataset.

**Goal:**  
Identify the best hours and days to drive Uber in Minneapolis to maximize earnings.

**Dataset:**  
- Personal Uber dataset (693k rides, 10 columns)  
- Features used: `distance`, `price`, `surge_multiplier`, `time_stamp` → converted to `hour`, `day_of_week`

**Analysis:**  
- Cleaned missing prices  
- Created new features: 
  - `is_surge` (whether surge applied)  
  - `expected_earnings = price × surge_multiplier`  
- Grouped by `day_of_week` and `hour` to compute averages  
- Generated pivot tables and heatmaps  

**Visualizations:**  
- Heatmap of **surge probability by day and hour**  
- Heatmap of **expected earnings by day and hour** (red = high earnings)  
- Highlighted the top 5 highest earning windows  

**Insights:**  
- Certain windows (e.g., Wednesday 1–2 AM, Thursday 5–6 AM) have the highest expected earnings  
- Midday hours have low surge probability → lower expected earnings  
- Data-driven recommendations for optimal Uber driving schedule  

**Next Steps / Future Analytics:**  
- More advanced analyses will include predicting surge hours using machine learning  
- Exploring ride demand trends, clustering, and forecasting earnings  
- This project lays the **foundation** for deeper, more sophisticated analytics in the portfolio  

**Notebook / Code:**  
[View the Colab notebook](https://colab.research.google.com/drive/1FtsLE9xElDLsYwVr36eakY3IIrj3Bgr9?usp=sharing)

---

*More projects coming soon — stay tuned for advanced analytics and predictive modeling!*
