from flask import Flask, render_template, flash, redirect, url_for, request
import pandas as pd


app = Flask(__name__)
app.secret_key = "My Secret key"

 
# web app routing
# home page
@app.route('/', methods=['GET','POST'])
def home():
    return render_template('home.html')

# graph edges url
@app.route('/graphedges/<topic>', methods= ['GET'])
def getGraphEdges(topic):
    df = pd.read_csv("Final_Data/Graph/edges_df.csv")
    df.drop(columns='Unnamed: 0',inplace=True)
    if int(topic) != -1:
        df = df[df['topic']==int(topic)]
        
    result = df.to_json(orient="records")
    return result

# graph nodes url
@app.route('/graphnodes/<topic>', methods= ['GET'])
def getGraphNodes(topic):
    df = pd.read_csv("Final_Data/Graph/node_df.csv")
    df.drop(columns='Unnamed: 0',inplace=True)
    
    if int(topic) != -1:
        df = df[df['topic']==int(topic)]
        
    result = df.to_json(orient="records")
    return result

# distance url
@app.route('/distance', methods= ['GET'])
def getDistnace():
    df = pd.read_csv("Final_Data/Distance/Distance_Data.csv")
    df.drop(columns='Unnamed: 0',inplace=True)
    result = df.to_json(orient="records")
    return result

# inter-topic barchart url
@app.route('/intertopic', methods= ['GET'])
def getInterTopic():
    df = pd.read_csv("Final_Data/Inter-Topic Barchart/topic_view.csv")
    result = df.to_json(orient="records")
    return result

# intra-topic barchart url
@app.route('/intratopic', methods= ['GET'])
def getIntraTopic():
    df = pd.read_csv("Final_Data/Intra-Topic Barchart/Frequency_df.csv")
    result = df.to_json(orient="records")
    return result

# timeseries url
@app.route('/timeseries', methods= ['GET'])
def getTimeSeries():
    df = pd.read_csv("Final_Data/Time Series/Time_series.csv")
    result = df.to_json(orient="records")
    return result

if __name__ == '__main__':
    # using host and port to integrate d3.js
    app.run(
        debug=True
    )