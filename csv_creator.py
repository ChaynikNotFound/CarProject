import pandas as pd
import os
d = {'Model':[0],'Path':[0]}
df = pd.DataFrame(data=d)
df = df.drop(0)
os.chdir("C:/Users/79166/Desktop/флуд")
pathes = os.listdir()
for path in pathes:
    # print(path)
    file = "C:/Users/79166/Desktop/флуд/"+path
    # print(file)
    os.chdir(file)
    nd = {'Model':path,'Path':[os.listdir()]}
    # print(os.getcwd())
    df2 = pd.DataFrame(data = nd)
    # print(df2)
    df = pd.concat([df,df2])
df.to_csv (r"C:/Users/79166/Desktop/флуд/Auto.csv", index= False)