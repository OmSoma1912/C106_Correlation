import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x = "Temperature", y = "Ice-cream Sales( ₹ )")
        fig.show()

def getDataSource(data_path):
    icecream_sales = []
    colddrink_sales = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            icecream_sales.append(float(row["Temperature"]))
            colddrink_sales.append(float(row["Ice-cream Sales( ₹ )"]))

        return{"x" : icecream_sales, "y" : colddrink_sales}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between temperatures and icecream sales :- /n--->", correlation[0,1])

def setup():
    data_path = "icecream-vs-tem.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()