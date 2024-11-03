 #Set the color 
color = 'orange' 
 
# Create the regression scatter plot with the specified color 
sns.regplot(x=data1['TreatmentCost'],y=data1['TreatmentTime'], color=color) 
 
# Customize scatter plot by adding a title and labels 
plt.title("Regression Plot: Treatment Cost vs Treatment time") 
plt.xlabel("Treatment Cost") 
plt.ylabel("Treatment time") 
 
# Show the plot 
plt.show()
