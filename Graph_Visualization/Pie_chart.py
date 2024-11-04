#importing all the libraries required for creating graphs 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px 
import matplotlib 
 
#creating a data for inserting dataset that is required to be visualised.  
data=pd.read_csv("BeezKneezVisualisation.csv") 
 
#In order to assign colors 
colors = ['Green','Purple','pink','Red'] 
 
# to separate segments of pie chart. 
explode = (0.05, 0.05, 0.05,0.05)  
 
# to display percentage values(rounded values) and labels on pie chart 
ax = data["MembershipLevel"].value_counts().plot(kind="pie", title="Memberships", 
autopct='%1.0f%%',colors=colors, explode=explode)  
