
#Create a bar chart 
ax = data['SpaTreatmentID'].value_counts().plot(kind='bar', title="Popularity of Treatments") 
 
#Customize bar charts by adding labels to x-axis and y-axis 
ax.set_xlabel("Type of Treatments") 
ax.set_ylabel("Number of customers") 
