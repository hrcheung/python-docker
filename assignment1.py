#this flask is just to show Hello World on screen.
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return ['Hello World! 1234']

@app.route('/q')
def cardinality_items():
    import pandas as pd
    #df=pd.read_csv("/app/basket_data.csv")
    df=pd.read_csv("/Users/haoranzhang/CS6220/homework-1/basket_data.csv",sep='delimiter', header=None,engine='python')
    df=df[0].str.split(',',expand=True)
    rows=df.shape[0]
    cols=df.shape[1]
    car_set=set()
    for i in range(100):
        for j in range(4):
            car_set.add(df[j][i])
    return(len(car_set))


# docker run -d -it --name python-docker -v /Users/haoranzhang/CS6220/homework-1:/app -e FLASK_APP=assignment1.py --publish 8000:5000 python-docker

# docker run -e FLASK_APP=assignment1.py --publish 8000:5000 -v /Users/haoranzhang/CS6220/homework-1/basket_data.csv:/home/6220_data -it python-docker /bin/bash