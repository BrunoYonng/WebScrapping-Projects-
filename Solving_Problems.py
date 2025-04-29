

# The information required from the web page

information = ['Film', 'Year', 'Rotten Tomatoes Top 100']


# STEP-1:

import pandas as pd 
import requests 
from bs4 import BeautifulSoup 
import sqlite3 


# STEP-2:

url = 'https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'

db_name = 'Movies_db'

table_name = 'Top_25_Movies'

csv_name = 'top_25_films_csv'

df = pd.DataFrame(columns=['Film', 'Year', 'Rotten Tomatoes Top 100'])

count = 0


# STEP-3:

# Requests 
html_page = requests.get(url).text
html_page


# Beautiful Soup 
data = BeautifulSoup(html_page, 'html.parser')
data


# STEP-4:

# Extraction of all Tables From html 
tables = data.find_all('tbody')
tables

# Extraction only the rows of the first table 
rows = tables[0].find_all('tr')
rows


# STEP-5:

# Iterate each element of all 25 rows

for row in rows:

    if count < 25: 

        col = row.find_all('td')

        if len(col)!=0:

            data_dict = {'Film': col[1].contents[0],
                         'Year': col[2].contents[0],
                         'Rotten Tomatoes Top 100': col[3].contents[0]}
            
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)

            count += 1

    else:
        break 


# STEP-6:

# Visualize the data base
# Consulting the type of the 'Year' variables
# Transform the type of data in 'Year' variables
# Filter the where Year is equal 2000's includinfg the 2000's

print(df)
df['Year'].dtype
df['Year'] = df['Year'].astype(int)
df.loc[df['Year'] >= 2000]


# STEP-7:

# Storing the data
# Save the DataFrame as CSV file

df.to_csv(csv_name)


# STEP-8:

# initialize the connection the Database 
# Save the dataframe as a table 
# Close the connection 

conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()


