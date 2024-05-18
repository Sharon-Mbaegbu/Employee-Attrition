# Exploratory Data Analysis Project

## Project Overview

This project involves an exploratory data analysis (EDA) of the physicochemical properties of red Vinho Verde wine samples. The primary goal was to uncover patterns and correlations that influence wine quality, focusing specifically on alcohol content, sulphates, and pH levels.

## Dataset

- **Source**: [Wine Quality Dataset](https://archive.ics.uci.edu/dataset/186/wine+quality)
- **Description**: The dataset comprises 1,599 red wine samples, each with 11 features and 1 target variable (quality).

## Tools and Libraries Used

- **Python**
- **Pandas**: Data manipulation and preparation
- **Seaborn & Matplotlib**: Data visualization
- **NumPy**: Numerical operations

## Analysis Methodology

1. **Correlation Heatmap**
   - Created a heatmap to visualize linear relationships between variables.
   - Found a strong positive correlation between alcohol content and wine quality.
   - Sulphates had a modest positive correlation, while pH levels showed a minimal negative correlation with quality.

2. **3D Scatter Plot**
   - Visualized interactions between alcohol content, sulphates, and pH levels.
   - Higher alcohol and sulphate levels were associated with higher quality wines, regardless of pH levels.

3. **Trellis Plot**
   - Examined the relationship between alcohol content and quality across different pH levels.
   - Consistent pattern: higher alcohol content generally led to higher quality scores, especially within the medium pH category.

## Conclusions

- **Key Findings**:
  - Alcohol content is a significant predictor of wine quality.
  - Sulphates contribute positively to wine quality.
  - pH levels interact with alcohol content, influencing quality outcomes.

- **Implications**:
  - Understanding the balance of these variables is crucial for optimizing wine production processes and enhancing quality control.

## How to Run the Analysis

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/Sharon-Mbaegbu/Employee-Attrition
   ```
2. **Navigate to the Project Directory:**
   cd [your-project-directory]
3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
    ```
4. **Run the Analysis Script:**
   ```sh
   python dv_ass_3.py
   ```
## File Descriptions
- dv_ass_3.py: Main analysis script containing the data processing and visualization code.
- winequality-red.csv: Dataset file.
- Exploratory_Data_Analysis.pdf: Detailed report of the analysis.

## References
- Dataset retrieved from https://archive.ics.uci.edu/dataset/186/wine+quality
