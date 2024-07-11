import pandas as pd 

df = pd.read_csv('students_data.csv') 
print("Basic Information about the Data Frame:") 
print (df.info()) 
print("\nSummary Statistics:") 
print(df.describe()) 
print("Display Top 5 Rows:") 
print(df.head()) 
print("Display Bottom 5 Rows:")
print(df.tail())
data = {'Name':['Alice', 'Bob','Charlie',None],'Age':[25,30,None,42],'City':['New York','London',None,'Paris']} 
df = pd.DataFrame(data) 
print(df) #Replacing None with a suitable value 
df.fillna('N/A',inplace=True) 
print(df) #convert a specific column to numeric datatype, replace errors(non numeric) with NaN 
df['Age'] = pd.to_numeric(df['Age'],errors = 'coerce') #Drop a column(axis 1 = cols, axis 0 = rows) 
df.drop('Name',axis=1,inplace=True) 
print(df)