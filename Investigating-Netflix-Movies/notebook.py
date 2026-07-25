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
#     display_name: .venv (3.12.3.final.0)
#     language: python
#     name: python3
# ---

# %% [markdown]
# <center><img src="redpopcorn.jpg"></center>

# %% [markdown]
# **Netflix**! What started in 1997 as a DVD rental service has since exploded into one of the largest entertainment and media companies.
#
# Given the large number of movies and series available on the platform, it is a perfect opportunity to flex your exploratory data analysis skills and dive into the entertainment industry.
#
# You work for a production company that specializes in nostalgic styles. You want to do some research on movies released in the 1990's. You'll delve into Netflix data and perform exploratory data analysis to better understand this awesome movie decade!
#
# You have been supplied with the dataset `netflix_data.csv`, along with the following table detailing the column names and descriptions. Feel free to experiment further after submitting!
#
# ## The data
# ### **netflix_data.csv**
# | Column | Description |
# |--------|-------------|
# | `show_id` | The ID of the show |
# | `type` | Type of show |
# | `title` | Title of the show |
# | `director` | Director of the show |
# | `cast` | Cast of the show |
# | `country` | Country of origin |
# | `date_added` | Date added to Netflix |
# | `release_year` | Year of Netflix release |
# | `duration` | Duration of the show in minutes |
# | `description` | Description of the show |
# | `genre` | Show genre |

# %% executionCancelledAt lastScheduledRunId executionTime=63 lastExecutedAt=1776180349273 lastExecutedByKernel="e3a2a874-2b6b-489f-90dd-e7a0b1031e55" lastSuccessfullyExecutedCode="# Importing pandas and matplotlib\nimport pandas as pd\nimport matplotlib.pyplot as plt\n\n# Read in the Netflix CSV as a DataFrame\nnetflix_df = pd.read_csv(\"netflix_data.csv\")"
# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# %% executionCancelledAt lastScheduledRunId executionTime=50 lastExecutedAt=1776180349324 lastExecutedByKernel="e3a2a874-2b6b-489f-90dd-e7a0b1031e55" lastSuccessfullyExecutedCode="# Start coding here! Use as many cells as you like\n\n# Filter for movies released in the 1990s\nnetflix_movies_90s = netflix_df[\n    (netflix_df['type'] == 'Movie') & \n    (netflix_df['release_year'] >= 1990) & \n    (netflix_df['release_year'] <= 1999)\n]\n\n# What was the most frequent movie duration in the 1990s?\nduration = int(netflix_movies_90s['duration'].mode()[0])\n\nprint(duration)" outputsMetadata={"0": {"height": 38, "type": "stream"}}
# Start coding here! Use as many cells as you like

# Filter for movies released in the 1990s
netflix_movies_90s = netflix_df[
    (netflix_df['type'] == 'Movie') & 
    (netflix_df['release_year'] >= 1990) & 
    (netflix_df['release_year'] <= 1999)
]

# What was the most frequent movie duration in the 1990s?
duration = int(netflix_movies_90s['duration'].mode()[0])

print(duration)

# %% executionCancelledAt lastScheduledRunId executionTime=49 lastExecutedAt=1776180349373 lastExecutedByKernel="e3a2a874-2b6b-489f-90dd-e7a0b1031e55" lastSuccessfullyExecutedCode="# A movie is considered short if it is less than 90 minutes.\n# Count the number of short action movies released in the 1990s\nshort_action_movies_90s = netflix_movies_90s[\n    (netflix_movies_90s['duration'] < 90) & \n    (netflix_movies_90s['genre'].str.contains('Action', case=False, na=False))\n]\nshort_movie_count = len(short_action_movies_90s)\n\nprint(short_movie_count)" outputsMetadata={"0": {"height": 38, "type": "stream"}}
# A movie is considered short if it is less than 90 minutes.
# Count the number of short action movies released in the 1990s
short_action_movies_90s = netflix_movies_90s[
    (netflix_movies_90s['duration'] < 90) & 
    (netflix_movies_90s['genre'].str.contains('Action', case=False, na=False))
]
short_movie_count = len(short_action_movies_90s)

print(short_movie_count)
