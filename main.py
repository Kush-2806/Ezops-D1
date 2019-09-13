from flask import Flask,send_file,render_template
import urllib, json 
import pandas as pd
import zipfile
import os

app = Flask(__name__, static_url_path="/static", static_folder='/home/dubspher/mysite/static')

@app.route('/')
def home():
    return render_template('base.html')

@app.route("/csvmaker/")
def csvmaker():
    # reading csv file to a DataFrame 
    df=pd.read_csv("train.csv") 

    #reverse Columns
    columns = df.columns.tolist()
    columns = columns[::-1]
    dataf = df[columns]

    if not os.path.exists('output'):
        os.makedirs('output')
    #write to new csv file
    dataf.to_csv('output/reverse.csv',index=False)

    #alternate columns to new file
    (df.iloc[:,::2]).to_csv('output/alternate.csv',index=False)
    
    zipf = zipfile.ZipFile('Output.zip','w', zipfile.ZIP_DEFLATED)
    for root,dirs, files in os.walk('output/'):
        for file in files:
            zipf.write('output/'+file)
    zipf.close()
    return send_file('Output.zip',
            mimetype = 'zip',
            attachment_filename= 'Converted_files.zip',
            as_attachment = True)


@app.route('/alphavantage/')
def alphavantage():
    with urllib.request.urlopen("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo") as url:
        data = json.loads(url.read().decode())
        df = pd.DataFrame(data["Time Series (Daily)"])
        df = df.T
        exfile = df.to_excel ('export_dataframe.xlsx', header=True)
    return send_file("export_dataframe.xlsx",as_attachment=True,mimetype="application/vnd.ms-excel",attachment_filename="Result.xlsx")


if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0')