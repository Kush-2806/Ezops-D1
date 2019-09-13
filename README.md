# Flask-webApp

The web application does two things:  
1 It takes data from the Kaggle titanic dataset (Downloaded file Train.csv), reads it, and writes it to two files:  
File 1: Column order reversed  
File 2: Just print alternate columns  
2 Reads data from the Alphavantage site providing just the Microsoft Stock time series daily quotes, and exports that to an excel downloadable file.  


Requirements: Python 3  
USAGE:  
Clone the repository  
Open repo root dir in terminal
Run flaskenv\Scripts\activate
Run pip install -r requirements.txt  
Run python main.py  
Open localhost:5000   
The Kaggle Script will ask to download a Zip file containing both the files mentioned above  
The Alphavantage Script will ask to download a Excel file, giving the desired output  
  
DOCKERFILE:  
This will export the application and dependencies as a Docker Image  
Requirements  
Docker installed and running  
Usage:  
CD to the root dir  
Run docker build --tag my-python-app .  
  
Run the Container:  
Run docker run --name python-app -p 5000:5000 my-python-app  
  
Open localhost:5000  
  
Same stuff...  
