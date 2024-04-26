### CSE 6242: TEAM 094
YouTube Trending Topic Modeling Analysis

### Description
This project package is a compilation of post processed data from YouTube's Trending Video Dataset (Kaggle) and YouTube API using the BERTopic algorithm 
which uses an ensemble of techniques to identify topic clusters.

Web App Views:

*Intertopic Distance: Intertopic distance graph shows the similarity between topics. When hovered over the points show a graph of frequent words and bigrams for the topic. 
    User can double click the point to be taken to a directed graph of the topic.
*Topic View Counts: Topic view counts graph shows the overall popularity of a topic in terms of views.
*Topic Line Chart: Topic line chart shows how much the topics have changed over time and gives a word list when hovered over.
*Graph All Topics: All topics graph has pan and zoom features that shows the connectedness of a topic. 
    Hovering over a point will display the word. Green = Noun, Red = Verb, Blue = Adjective. 
    The graph has force that pulls more connected nodes toward the center.


### Installation
After creating a virtual environment, install the packages in the file `requirements.txt` with the code below:
    pip install -r requirements.txt

Make sure to download all the folders located in the the DropBox link below and save them locally in the existing `Final_Data` folder:
https://www.dropbox.com/scl/fo/dz2q1b0qkhnzkttuo1afp/h?rlkey=r4bvd59w5s4xboqkx3fds8sb3&dl=0

### Execution
The web app can be started by running `flask run` in the terminal in the same directory as `app.py`.
View the web app running on `http://127.0.0.1:5000/`