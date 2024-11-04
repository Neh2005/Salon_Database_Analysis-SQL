# Set a custom color palette  
 
custom_palette = "husl"  # Example: "Set1", "Blues", "husl", etc. 
 
#Create a box plot 
 
plt.figure(figsize=(12, 10)) 
sns.boxplot(x="TOTALLengthofAppointment", data=data, palette=custom_palette) 
plt.title("Customized Box Plot") 
plt.xlabel("Total length of appointment") 
plt.show()
