# FE-595-HW-2

In this py file I pull 50 company names and their purpose.

Packages:
To start import request, this will be for requesting the html from a given url. Next we add in BeautifulSoup this will be for parsing the HTML into more managable chunck. The last package is optional when working with webscrapping I added it so I could create a dataframe and export that to a csv file. 

Code:
First step here was creating an empty array which will store the results. Majority of the code is within a for loop which simply runs the inner code 50 times. I define the url, request and parse it using BeautifulSoup. 

Next, I created a for loop which will run for each line in the HTML which has "li" class. "Li" is where the Name and Purpose of each company is stored. I then do a simple if statement asking if the line has "Name: " or "Purpose: " in it. If true we appended it to an empty array called company which gets overwritten each time the for loop runs. Once we have the company name and purpose stored in the company array the if statements and for statement is done.

With the company now stored we append it to results. Recall the results array was outside of the inital for loop so now we have an array of an array which is populated with company name and company purpose. This append happens for all 50 companies. 

Finally with all 50 companies defined I put it all into a pd.DataFrame with two columns "Name" & "Purpose" and export it to csv. 
