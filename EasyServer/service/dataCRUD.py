import pandas as pd
import os

class EasyData:
    def __init__(self,dataname):
        self.datapath = self.setFilePath(dataname)
        self.data = self.retrieve()  # 文件中的数据(DataFrame)

    # 设置文件地址
    def setFilePath(self,dataname):
        parentPath = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
        return f"{parentPath}/data/{dataname}.csv"

    # 增
    def create(self,new2DArray):
        # 新数据new2DArray: 二维数组[[x,x,x]]
        self.data.append(new2DArray)
        self.data.to_csv(self.datapath)

    # 查
    def retrieve(self):
        df = pd.read_csv(self.datapath,index_col="id")
        return df

    # 改
    def update(self,rowNo,colNo,newValue):
        # 新数据newValue: 单个值
        df = self.data.copy()
        df.iloc[rowNo,colNo] = newValue
        df.to_csv(self.datapath)
        self.data = df

    # 删
    def delete(self,deleteType,condition):
        # 删列 condition：如[x,x]
        # 删行 condition：如{colName:x,value:x}
        if deleteType=="column":
            self.data.drop(columns=condition)
        else:
            idx = self.data.loc[self.data[condition["column"]]==condition["value"]].index
            self.data.drop(index=(idx))
        self.data.to_csv(self.datapath)

if __name__ == "__main__":
    ed = EasyData("data")
    print(ed)
