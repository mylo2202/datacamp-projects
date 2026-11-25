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

# %% [markdown] id="Jy67-HhaxSv6"
# # Analyzing Crime in Los Angeles

# %% [markdown] id="31ab2131-3049-4d8d-b9dc-d195f72af27a"
# ![Los Angeles skyline](la_skyline.jpg)
#
# Los Angeles, California 😎. The City of Angels. Tinseltown. The Entertainment Capital of the World!
#
# Known for its warm weather, palm trees, sprawling coastline, and Hollywood, along with producing some of the most iconic films and songs. However, as with any highly populated city, it isn't always glamorous and there can be a large volume of crime. That's where you can help!
#
# You have been asked to support the Los Angeles Police Department (LAPD) by analyzing crime data to identify patterns in criminal behavior. They plan to use your insights to allocate resources effectively to tackle various crimes in different areas.
#
# ## The Data
#
# They have provided you with a single dataset to use. A summary and preview are provided below.
#
# It is a modified version of the original data, which is publicly available from Los Angeles Open Data.
#
# ### crimes.csv
#
# | Column     | Description              |
# |------------|--------------------------|
# | `'DR_NO'` | Division of Records Number: Official file number made up of a 2-digit year, area ID, and 5 digits. |
# | `'Date Rptd'` | Date reported - MM/DD/YYYY. |
# | `'DATE OCC'` | Date of occurrence - MM/DD/YYYY. |
# | `'TIME OCC'` | In 24-hour military time. |
# | `'AREA NAME'` | The 21 Geographic Areas or Patrol Divisions are also given a name designation that references a landmark or the surrounding community that it is responsible for. For example, the 77th Street Division is located at the intersection of South Broadway and 77th Street, serving neighborhoods in South Los Angeles. |
# | `'Crm Cd Desc'` | Indicates the crime committed. |
# | `'Vict Age'` | Victim's age in years. |
# | `'Vict Sex'` | Victim's sex: `F`: Female, `M`: Male, `X`: Unknown. |
# | `'Vict Descent'` | Victim's descent:<ul><li>`A` - Other Asian</li><li>`B` - Black</li><li>`C` - Chinese</li><li>`D` - Cambodian</li><li>`F` - Filipino</li><li>`G` - Guamanian</li><li>`H` - Hispanic/Latin/Mexican</li><li>`I` - American Indian/Alaskan Native</li><li>`J` - Japanese</li><li>`K` - Korean</li><li>`L` - Laotian</li><li>`O` - Other</li><li>`P` - Pacific Islander</li><li>`S` - Samoan</li><li>`U` - Hawaiian</li><li>`V` - Vietnamese</li><li>`W` - White</li><li>`X` - Unknown</li><li>`Z` - Asian Indian</li> |
# | `'Weapon Desc'` | Description of the weapon used (if applicable). |
# | `'Status Desc'` | Crime status. |
# | `'LOCATION'` | Street address of the crime. |

# %% [markdown] id="alSVI_v3x4Ms"
# ## Project Instructions
#
# Explore the `crimes.csv` dataset and use your findings to answer the following questions:
#
# - Which hour has the highest frequency of crimes? Store as an integer variable called `peak_crime_hour`.
#
# - Which area has the largest frequency of night crimes (crimes committed between 10pm and 3:59am)? Save as a string variable called `peak_night_crime_location`.
#
# - Identify the number of crimes committed against victims of different age groups. Save as a pandas Series called `victim_ages`, with age group labels `"0-17"`, `"18-25"`, `"26-34"`, `"35-44"`, `"45-54"`, `"55-64"`, and `"65+"` as the index and the frequency of crimes as the values.

# %% colab={"base_uri": "https://localhost:8080/", "height": 417} executionCancelledAt executionTime=304 id="7c6c3c36-5c8b-4cce-8681-95292b8f0861" lastExecutedAt=1742912296156 lastExecutedByKernel="f1481d25-46a8-4581-9591-361900f606fb" lastScheduledRunId lastSuccessfullyExecutedCode="# Re-run this cell\n#\u00a0Import required libraries\nimport pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport seaborn as sns\ncrimes = pd.read_csv(\"crimes.csv\", dtype={\"TIME OCC\": str})\ncrimes.head()" outputId="ce3a78d0-916a-4946-b167-1ceda62216c8" outputsMetadata={"0": {"height": 550, "tableState": {"quickFilterText": ""}, "type": "dataFrame"}}
# Re-run this cell
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
crimes = pd.read_csv("crimes.csv", dtype={"TIME OCC": str})
crimes.head()

# %% id="53eada96-447c-46c3-9848-f4ca3de53d06"
# Start coding here
# Use as many cells as you need

# %% id="cjDoudNn08mB"
# Convert 'TIME OCC' to numeric and extract the hour
crimes['TIME OCC'] = pd.to_numeric(crimes['TIME OCC'], errors='coerce')
crimes['HOUR OCC'] = crimes['TIME OCC'] // 100
crimes.head()

# %% [markdown] id="30a08bc4"
# ### 1. Which hour has the highest frequency of crimes?

# %% colab={"base_uri": "https://localhost:8080/"} id="1a0f94c1" outputId="7d0d9908-f2bd-4469-a562-6317c1ec49c3"
# Calculate the frequency of crimes per hour
crime_frequency_by_hour = crimes['HOUR OCC'].value_counts().sort_index()

# Find the hour with the highest frequency
peak_crime_hour = crime_frequency_by_hour.idxmax()

print(f"The hour with the highest frequency of crimes is: {int(peak_crime_hour)}")

# %% [markdown] id="669d5c86"
# ### 2. Which area has the largest frequency of night crimes?

# %% colab={"base_uri": "https://localhost:8080/"} id="a012c2a9" outputId="d673a0ee-56b3-4318-d130-0c54f9289cee"
# Identify night crimes (between 10pm and 3:59am)
night_crimes = crimes[(crimes['HOUR OCC'] >= 22) | (crimes['HOUR OCC'] < 4)]

# Group by 'AREA NAME' and count the frequency of night crimes
night_crime_frequency_by_area = night_crimes['AREA NAME'].value_counts()

# Find the area with the largest frequency of night crimes
peak_night_crime_location = night_crime_frequency_by_area.idxmax()

print(f"The area with the largest frequency of night crimes is: {peak_night_crime_location}")

# %% [markdown] id="5eb4d3fb"
# ### 3. Number of crimes committed against victims of different age groups

# %% colab={"base_uri": "https://localhost:8080/", "height": 370} id="8845835d" outputId="9bccda36-2f23-4c6f-8d40-e47d8f254602"
# Define age bins and labels
age_bins = [0, 17, 25, 34, 44, 54, 64, np.inf]
age_labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]

# Categorize 'Vict Age' into age groups
crimes['Vict Age Group'] = pd.cut(
    crimes['Vict Age'],
    bins=age_bins,
    labels=age_labels,
    right=True,
    include_lowest=True
)

# Count the frequency of crimes for each age group
victim_ages = crimes['Vict Age Group'].value_counts().reindex(age_labels)

print("Crimes by victim age group:\n")
display(victim_ages)
