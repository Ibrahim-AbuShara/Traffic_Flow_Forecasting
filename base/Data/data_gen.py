import pandas as pd

metra=pd.read_csv("/home/ibrahim/projects/Traffic_Flow_Forecasting/base/Data/metra_la/metra_test_df.csv")
metra=metra.drop("date",axis=1)
bay=pd.read_csv("/home/ibrahim/projects/Traffic_Flow_Forecasting/base/Data/pems_bay/bay_test_df.csv")
bay=bay.drop("date",axis=1)

df=pd.DataFrame(columns=["sensor_id","varimax_path","rfr_path"])

for col in metra.columns:
    lst=[]
    lst.append(col)
    lst.append(f"./Models/metra_VARMAX_Models/{col}.joblib")
    lst.append(f"./Models/metra_RFR_Models/{col}.joblib")
    df.loc[len(df)] = lst
    
for col in bay.columns:
    lst=[]
    lst.append(col)
    lst.append(f"./Models/bay_VARMAX_Models/{col}.joblib")
    lst.append(f"./Models/bay_RFR_Models/{col}.joblib")
    df.loc[len(df)] = lst
    
df.to_csv("data_gen.csv",index=False)