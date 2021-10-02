import csv
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("Project108.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"], show_hist = False)
#fig = px.bar(x = "Mobile Brand", y = "Avg Rating")
#fig.show()
fig.show()