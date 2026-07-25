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
# # Visualizing the History of Nobel Prize Winners
#
# The Nobel Prize has been among the most prestigious international awards since 1901. Each year, awards are bestowed in chemistry, literature, physics, physiology or medicine, economics, and peace. In addition to the honor, prestige, and substantial prize money, the recipient also gets a gold medal with an image of Alfred Nobel (1833 - 1896), who established the prize.
#
# ![](Nobel_Prize.png)
#
# The Nobel Foundation has made a dataset available of all prize winners from the outset of the awards from 1901 to 2023. The dataset used in this project is from the Nobel Prize API and is available in the `nobel.csv` file in the `data` folder.
#
# In this project, you'll get a chance to explore and answer several questions related to this prizewinning data. And we encourage you then to explore further questions that you're interested in!
#
# Analyze Nobel Prize winner data and identify patterns by answering the following questions:
#
# What is the most commonly awarded gender and birth country?
#
# - Store your answers as string variables `top_gender` and `top_country`.
#
# Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?
#
# - Store this as an integer called `max_decade_usa`.
#
# Which decade and Nobel Prize category combination had the highest proportion of female laureates?
#
# - Store this as a dictionary called `max_female_dict` where the decade is the key and the category is the value. There should only be one key:value pair.
#
# Who was the first woman to receive a Nobel Prize, and in what category?
#
# - Save your string answers as `first_woman_name` and `first_woman_category`.
#
# Which individuals or organizations have won more than one Nobel Prize throughout the years?
#
# - Store the full names in a list named `repeat_list`.

# %% executionCancelledAt lastScheduledRunId executionTime=47 lastExecutedAt=1784951903325 lastExecutedByKernel="f853f453-eea0-41d3-b679-fe6a913b4293" lastSuccessfullyExecutedCode="# Loading in required libraries\nimport pandas as pd\nimport seaborn as sns\nimport numpy as np\n\n# Start coding here!"
# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np

# Start coding here!

# %% [markdown]
# ### Loading the Nobel Prize Dataset
#
# First, we'll load the `nobel.csv` file into a pandas DataFrame and inspect its first few rows and general information to understand the data structure and types.

# %% executionCancelledAt executionTime lastExecutedAt lastExecutedByKernel lastScheduledRunId lastSuccessfullyExecutedCode outputsMetadata={"0": {"height": 249, "tableState": {}, "type": "dataFrame"}, "1": {"height": 542, "type": "stream"}}
nobel = pd.read_csv('data/nobel.csv')
display(nobel.head())
display(nobel.info())

# %% [markdown]
# ### Question 1: Most Commonly Awarded Gender and Birth Country
#
# To find the most commonly awarded gender and birth country, we'll count the occurrences of each unique value in the `gender` and `birth_country` columns, respectively, and then select the top one.

# %% executionCancelledAt lastScheduledRunId executionTime=48 jupyter={"outputs_hidden": false, "source_hidden": false} lastExecutedAt=1784951903424 lastExecutedByKernel="f853f453-eea0-41d3-b679-fe6a913b4293" lastSuccessfullyExecutedCode="# Most commonly awarded gender\ntop_gender = nobel['sex'].value_counts().index[0]\n\n# Most commonly awarded birth country\ntop_country = nobel['birth_country'].value_counts().index[0]\n\nprint(f\"Most commonly awarded gender: {top_gender}\")\nprint(f\"Most commonly awarded birth country: {top_country}\")" outputsMetadata={"0": {"height": 59, "type": "stream"}}
# Most commonly awarded gender
top_gender = nobel['sex'].value_counts().index[0]

# Most commonly awarded birth country
top_country = nobel['birth_country'].value_counts().index[0]

print(f"Most commonly awarded gender: {top_gender}")
print(f"Most commonly awarded birth country: {top_country}")

# %% [markdown]
# ### Question 2: Decade with Highest Ratio of US-born Nobel Prize Winners
#
# To determine the decade with the highest ratio of US-born winners, we need to first extract the decade from the `year` column. Then, we'll calculate the number of US-born winners and total winners for each decade and compute their ratio.

# %% executionCancelledAt lastScheduledRunId executionTime=51 lastExecutedAt=1784951903476 lastExecutedByKernel="f853f453-eea0-41d3-b679-fe6a913b4293" lastSuccessfullyExecutedCode="# Create a 'decade' column\nnobel['decade'] = (nobel['year'] // 10) * 10\n\n# Filter for US-born winners\nnobel_us_born = nobel[nobel['birth_country'] == 'United States of America']\n\n# Count total winners per decade\ntotal_winners_per_decade = nobel.groupby('decade').size()\n\n# Count US-born winners per decade\nus_born_winners_per_decade = nobel_us_born.groupby('decade').size()\n\n# Calculate ratio of US-born to total winners per decade\nratio_us_to_total = us_born_winners_per_decade / total_winners_per_decade\n\n# Find the decade with the highest ratio\nmax_decade_usa = ratio_us_to_total.idxmax()\n\nprint(f\"Decade with highest ratio of US-born winners: {max_decade_usa}\")" outputsMetadata={"0": {"height": 38, "type": "stream"}}
# Create a 'decade' column
nobel['decade'] = (nobel['year'] // 10) * 10

# Filter for US-born winners
nobel_us_born = nobel[nobel['birth_country'] == 'United States of America']

# Count total winners per decade
total_winners_per_decade = nobel.groupby('decade').size()

# Count US-born winners per decade
us_born_winners_per_decade = nobel_us_born.groupby('decade').size()

# Calculate ratio of US-born to total winners per decade
ratio_us_to_total = us_born_winners_per_decade / total_winners_per_decade

# Find the decade with the highest ratio
max_decade_usa = ratio_us_to_total.idxmax()

print(f"Decade with highest ratio of US-born winners: {max_decade_usa}")

# %% [markdown]
# ### Question 3: Decade and Category with Highest Proportion of Female Laureates
#
# To find the decade and category with the highest proportion of female laureates, we will first filter for female laureates, then group by decade and category to count the number of female winners and total winners in each group, and finally calculate the proportion.

# %% executionCancelledAt lastScheduledRunId executionTime=59 lastExecutedAt=1784951903535 lastExecutedByKernel="f853f453-eea0-41d3-b679-fe6a913b4293" lastSuccessfullyExecutedCode="# Filter for female laureates\nfemales = nobel[nobel['sex'] == 'Female']\n\n# Group by decade and category, then count female winners\nfemale_counts = females.groupby(['decade', 'category']).size().reset_index(name='female_winners')\n\n# Group by decade and category, then count total winners\ntotal_counts = nobel.groupby(['decade', 'category']).size().reset_index(name='total_winners')\n\n# Merge the counts\nmerged_counts = pd.merge(female_counts, total_counts, on=['decade', 'category'], how='left')\n\n# Calculate the proportion of female laureates\nmerged_counts['proportion_female'] = merged_counts['female_winners'] / merged_counts['total_winners']\n\n# Find the row with the highest proportion\nmax_proportion_row = merged_counts.loc[merged_counts['proportion_female'].idxmax()]\n\n# Store as a dictionary\nmax_female_dict = {int(max_proportion_row['decade']): max_proportion_row['category']}\n\nprint(f\"Decade and category with highest proportion of female laureates: {max_female_dict}\")" outputsMetadata={"0": {"height": 38, "type": "stream"}}
# Filter for female laureates
females = nobel[nobel['sex'] == 'Female']

# Group by decade and category, then count female winners
female_counts = females.groupby(['decade', 'category']).size().reset_index(name='female_winners')

# Group by decade and category, then count total winners
total_counts = nobel.groupby(['decade', 'category']).size().reset_index(name='total_winners')

# Merge the counts
merged_counts = pd.merge(female_counts, total_counts, on=['decade', 'category'], how='left')

# Calculate the proportion of female laureates
merged_counts['proportion_female'] = merged_counts['female_winners'] / merged_counts['total_winners']

# Find the row with the highest proportion
max_proportion_row = merged_counts.loc[merged_counts['proportion_female'].idxmax()]

# Store as a dictionary
max_female_dict = {int(max_proportion_row['decade']): max_proportion_row['category']}

print(f"Decade and category with highest proportion of female laureates: {max_female_dict}")

# %% [markdown]
# ### Question 4: First Woman to Receive a Nobel Prize and in What Category
#
# To identify the first woman to receive a Nobel Prize and her category, we will filter the DataFrame for female laureates, sort them by `year` (ascending), and then extract the name and category of the first entry.

# %% executionCancelledAt lastScheduledRunId executionTime=50 lastExecutedAt=1784951903585 lastExecutedByKernel="f853f453-eea0-41d3-b679-fe6a913b4293" lastSuccessfullyExecutedCode="# Filter for female laureates and sort by year\nfirst_woman_winner = nobel[nobel['sex'] == 'Female'].sort_values(by='year').iloc[0]\n\n# Extract name and category\nfirst_woman_name = first_woman_winner['full_name']\nfirst_woman_category = first_woman_winner['category']\n\nprint(f\"First woman to receive a Nobel Prize: {first_woman_name}\")\nprint(f\"Category: {first_woman_category}\")" outputsMetadata={"0": {"height": 59, "type": "stream"}}
# Filter for female laureates and sort by year
first_woman_winner = nobel[nobel['sex'] == 'Female'].sort_values(by='year').iloc[0]

# Extract name and category
first_woman_name = first_woman_winner['full_name']
first_woman_category = first_woman_winner['category']

print(f"First woman to receive a Nobel Prize: {first_woman_name}")
print(f"Category: {first_woman_category}")

# %% [markdown]
# ### Question 5: Individuals or Organizations with Multiple Nobel Prizes
#
# To find individuals or organizations who have won more than one Nobel Prize, we will group the data by `full_name` and count the number of awards for each. Then we will filter for those with more than one award.

# %% executionCancelledAt lastScheduledRunId executionTime=60 lastExecutedAt=1784951903645 lastExecutedByKernel="f853f453-eea0-41d3-b679-fe6a913b4293" lastSuccessfullyExecutedCode="# Count the number of awards per full_name\nrepeat_winners = nobel['full_name'].value_counts()\n\n# Filter for those with more than one award\nrepeat_list = repeat_winners[repeat_winners > 1].index.tolist()\n\nprint(f\"Individuals or organizations with multiple Nobel Prizes: {repeat_list}\")" outputsMetadata={"0": {"height": 80, "type": "stream"}}
# Count the number of awards per full_name
repeat_winners = nobel['full_name'].value_counts()

# Filter for those with more than one award
repeat_list = repeat_winners[repeat_winners > 1].index.tolist()

print(f"Individuals or organizations with multiple Nobel Prizes: {repeat_list}")
