#FE-595
#HW2 - Webscraper
#Jake Vick

#packages ----
import requests #for pulling HTML from URLs
from bs4 import BeautifulSoup #helps parse html
import pandas as pd #want to create dataframe so export to excel is easy 
#----

results = [] #create an empty array for all results

for _ in range(50):

    #define the url, request the page, and parse the HTML
    url = "http://18.206.38.144:8000/random_company"
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    #print(soup.prettify()) #print out full HTML
    
    #for loop ----
    company = [] #create an empty array
    #look for each "li" in the HTML - once we find a line extract the text
    #test if the text has "Name:" or "Purpose:" in that line
    #if it does store it if not go to next line
    for li in soup.find_all("li"):
        #company.append(li.text.strip())
        line = li.text.strip()
        if "Name:" in line:
            company.append(line.replace("Name: ","")) #remove "Name: " to clean the text
            #print(line)
        if "Purpose:" in line:
            company.append(line.replace("Purpose: ",""))
            #print(line)
    results.append(company)

#create dataframe with all 50 results with column headers Name and Purpose
df = pd.DataFrame(data = results, columns = ["Name", "Purpose"])
print(df.head())

#store df in csv
df.to_csv(r"C:\Users\JVick\Desktop\PlayGround\School\50companyData.csv")