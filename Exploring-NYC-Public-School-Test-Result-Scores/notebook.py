# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# ![New York City schoolbus](schoolbus.jpg)
#
# Photo by [Jannis Lucas](https://unsplash.com/@jannis_lucas) on [Unsplash](https://unsplash.com).
# <br>
#
# Every year, American high school students take SATs, which are standardized tests intended to measure literacy, numeracy, and writing skills. There are three sections - reading, math, and writing, each with a **maximum score of 800 points**. These tests are extremely important for students and colleges, as they play a pivotal role in the admissions process.
#
# Analyzing the performance of schools is important for a variety of stakeholders, including policy and education professionals, researchers, government, and even parents considering which school their children should attend. 
#
# You have been provided with a dataset called `schools.csv`, which is previewed below.
#
# You have been tasked with answering three key questions about New York City (NYC) public school SAT performance.

# %% id="bA5ajAmk7XH6" executionTime=50 lastSuccessfullyExecutedCode="# Re-run this cell \nimport pandas as pd\n\n# Read in the data\nschools = pd.read_csv(\"schools.csv\")\n\n# Preview the data\nschools.head()\n\n# Start coding here...\n# Add as many cells as you like..." executionCancelledAt lastExecutedAt=1781542373496 lastScheduledRunId outputsMetadata={"0": {"height": 550, "type": "dataFrame", "tableState": {}, "chartState": {"chartModel": {"modelType": "range", "chartId": "id-gg1p52i1qnr", "chartType": "groupedColumn", "chartThemeName": "datalabTheme", "chartOptions": {"common": {"animation": {"enabled": true}}}, "chartPalette": {"fills": ["#6568A0", "#43D7A4", "#4095DB", "#FACC5F", "#CAE279", "#F08083", "#5BCDF2", "#F099DC", "#965858", "#7DB64F", "#A98954"], "strokes": ["#6568A0", "#43D7A4", "#4095DB", "#FACC5F", "#CAE279", "#F08083", "#5BCDF2", "#F099DC", "#965858", "#7DB64F", "#A98954"], "up": {"fill": "#459d55", "stroke": "#1e652e"}, "down": {"fill": "#ef5452", "stroke": "#a82529"}, "neutral": {"fill": "#b5b5b5", "stroke": "#575757"}, "altUp": {"fill": "#5090dc", "stroke": "#2b5c95"}, "altDown": {"fill": "#ffa03a", "stroke": "#cc6f10"}, "altNeutral": {"fill": "#b5b5b5", "stroke": "#575757"}}, "cellRange": {"rowStartIndex": null, "rowStartPinned": null, "rowEndIndex": null, "rowEndPinned": null, "columns": ["school_name"]}, "switchCategorySeries": false, "suppressChartRanges": false, "unlinkChart": false, "version": "32.2.2"}, "rangeChartModel": {"rangeColumns": ["school_name"], "switchCategorySeries": false}, "pivotMode": {"enabled": false}, "activeTab": "data"}}} visualizeDataframe=false version="ag-charts-v1" lastExecutedByKernel="14f737c2-c782-44ab-b41a-b930c64b0494"
# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# Start coding here...
# Add as many cells as you like...

# %% [markdown]
# ### NYC schools with the best math results

# %% executionCancelledAt executionTime=58 lastExecutedAt=1781542373554 lastExecutedByKernel="14f737c2-c782-44ab-b41a-b930c64b0494" lastScheduledRunId lastSuccessfullyExecutedCode="# Calculate the minimum math score for 'best' results (80% of 800)\nmin_math_score = 0.8 * 800\n\n# Filter for schools with average math scores greater than or equal to the minimum\nbest_math_schools = schools[schools['average_math'] >= min_math_score]\n\n# Select the required columns and sort by 'average_math' in descending order\nbest_math_schools = best_math_schools[['school_name', 'average_math']].sort_values(by='average_math', ascending=False)\n\n# Display the results\ndisplay(best_math_schools)" outputsMetadata={"0": {"height": 550, "type": "dataFrame", "tableState": {}}}
# Calculate the minimum math score for 'best' results (80% of 800)
min_math_score = 0.8 * 800

# Filter for schools with average math scores greater than or equal to the minimum
best_math_schools = schools[schools['average_math'] >= min_math_score]

# Select the required columns and sort by 'average_math' in descending order
best_math_schools = best_math_schools[['school_name', 'average_math']].sort_values(by='average_math', ascending=False)

# Display the results
display(best_math_schools)

# %% [markdown]
# ### Top 10 Performing Schools by Combined SAT Score

# %% executionCancelledAt executionTime=50 lastExecutedAt=1781542373604 lastExecutedByKernel="14f737c2-c782-44ab-b41a-b930c64b0494" lastScheduledRunId lastSuccessfullyExecutedCode="# Calculate 'total_SAT' for each school\nschools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']\n\n# Sort by 'total_SAT' in descending order and select the top 10\ntop_10_schools = schools.sort_values(by='total_SAT', ascending=False)[['school_name', 'total_SAT']].head(10)\n\n# Display the results\ndisplay(top_10_schools)" outputsMetadata={"0": {"height": 550, "type": "dataFrame", "tableState": {}}}
# Calculate 'total_SAT' for each school
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']

# Sort by 'total_SAT' in descending order and select the top 10
top_10_schools = schools.sort_values(by='total_SAT', ascending=False)[['school_name', 'total_SAT']].head(10)

# Display the results
display(top_10_schools)

# %% [markdown]
# ### Borough with the Largest Standard Deviation in Combined SAT Score

# %% executionCancelledAt executionTime=51 lastExecutedAt=1781542373655 lastExecutedByKernel="14f737c2-c782-44ab-b41a-b930c64b0494" lastScheduledRunId lastSuccessfullyExecutedCode="# Group by borough and calculate required statistics\nborough_stats = schools.groupby('borough')['total_SAT'].agg([\n    ('num_schools', 'count'),\n    ('average_SAT', 'mean'),\n    ('std_SAT', 'std')\n]).reset_index()\n\n# Find the borough with the largest standard deviation\nlargest_std_dev = borough_stats.sort_values(by='std_SAT', ascending=False).head(1)\n\n# Round numeric values to two decimal places\nlargest_std_dev = largest_std_dev.round(2)\n\n# Display the results\ndisplay(largest_std_dev)" outputsMetadata={"0": {"height": 550, "type": "dataFrame", "tableState": {}}}
# Group by borough and calculate required statistics
borough_stats = schools.groupby('borough')['total_SAT'].agg([
    ('num_schools', 'count'),
    ('average_SAT', 'mean'),
    ('std_SAT', 'std')
]).reset_index()

# Find the borough with the largest standard deviation
largest_std_dev = borough_stats.sort_values(by='std_SAT', ascending=False).head(1)

# Round numeric values to two decimal places
largest_std_dev = largest_std_dev.round(2)

# Display the results
display(largest_std_dev)
