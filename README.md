# Traffic Accident Analysis

A comprehensive Python-based analysis of traffic accident data to uncover patterns related to road conditions, weather, time of day, and geospatial distribution, with visualizations powered by Matplotlib and Seaborn.


## Project Overview
This project analyzes traffic accident data to identify trends and factors contributing to accidents in the United Kingdom. By examining variables such as road conditions, weather, time of day, and geographic locations, the analysis provides actionable insights for researchers, policymakers, and urban planners aiming to enhance road safety.

## Key Features
- **Exploratory Data Analysis (EDA)**: Investigates accident severity and temporal patterns (e.g., day, month, time).
- **Road and Weather Analysis**: Evaluates the impact of road surface conditions and weather on accident frequency.
- **Geospatial Visualization**: Maps accident hotspots to identify high-risk areas.
- **Contributing Factors**: Analyzes factors such as junction control to understand accident causes.
- **Customizable Workflow**: Adaptable to various datasets and analysis objectives.

## Dataset
The analysis utilizes the [UK Road Accident Dataset](https://www.kaggle.com/datasets/devansodariya/road-accident-united-kingdom-uk-dataset) from Kaggle. Download the dataset and place the CSV file (e.g., `your_dataset.csv`) in the project directory.

## System Requirements
- **Python**: Version 3.8 or higher
- **Libraries**:
  - `pandas` for data manipulation
  - `matplotlib` for plotting
  - `seaborn` for advanced visualizations
- **Operating System**: Windows, macOS, or Linux

## Installation Guide
1. **Install Dependencies**:
   ```bash
   pip install pandas matplotlib seaborn
   ```

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-organization/traffic-accident-analysis.git
   cd traffic-accident-analysis
   ```

3. **Prepare the Dataset**:
   Download the dataset from Kaggle and place it in the project root directory as `your_dataset.csv`.

## Usage Instructions
1. **Configure the Dataset Path**:
   Update the dataset file path in `analysis_script.py`:
   ```python
   dataset_path = "your_dataset.csv"
   ```

2. **Run the Analysis**:
   Execute the script from the command line:
   ```bash
   python analysis_script.py
   ```

## Analysis Workflow
The analysis is structured as follows:

1. **Exploratory Data Analysis (EDA)**:
   - Examines the distribution of accident severity.
   - Analyzes temporal patterns, including accidents by day of the week, month, and time of day.

2. **Road Conditions and Weather Analysis**:
   - Visualizes the relationship between accidents and road surface conditions (e.g., wet, dry).
   - Assesses the impact of weather conditions on accident frequency.

3. **Geospatial Analysis**:
   - Maps accident locations to identify hotspots using geographic coordinates.

4. **Contributing Factors Analysis**:
   - Investigates factors such as junction control to uncover underlying causes of accidents.


## Outputs and Visualizations
- **Console Outputs**:
  - Summary statistics and data insights from EDA.
- **Graphical Outputs**:
  - Histograms and bar plots for accident severity and temporal distributions.
  - Heatmaps or scatter plots for geospatial accident hotspots.
  - Visualizations of road and weather condition impacts.
- **Saved Files**:
  - Generated plots are saved as PNG files in the project directory (e.g., `severity_distribution.png`).
