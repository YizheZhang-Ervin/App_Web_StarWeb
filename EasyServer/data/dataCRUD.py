import pandas as pd

def createData(rawData,newData,dataName):
    df = rawData.append(newData)
    saveData(df,dataName)

def retrieveData(dataName):
    df = pd.read_csv(f"../data/{dataName}.csv",index_col="id")
    return df

def updateData(rowNo,rawData,newData,dataName):
    df = rawData.copy()
    df.iloc[rowNo,:] = newData
    saveData(df,dataName)

def deleteData(data,dataName,condition):
    df = data.loc[condition]
    saveData(df,dataName)
    
def saveData(data,dataName):
    data.to_csv(f"../data/{dataName}.csv")



