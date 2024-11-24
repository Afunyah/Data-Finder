import pandas as pd
import os

originalfile = "CRM_Connections.xlsx"

odf = pd.read_excel(originalfile, header=0)

size = 50
list_of_dfs = [odf.loc[i:i+size-1,:] for i in range(0, len(odf),size)]

for df in list_of_dfs:
    # print(df)
    start_id = df.iloc[0]["ID"]
    end_id = df.iloc[len(df)-1]["ID"]
    
    batch_dir = f"batches/batch_{start_id}_{end_id}"
    
    if not os.path.exists(batch_dir):
        os.makedirs(batch_dir)
    
    input_fname = f"{batch_dir}/original_{start_id}_{end_id}.xlsx"
    output_fname = f"{batch_dir}/output_{start_id}_{end_id}.xlsx"
    
    df.to_excel(input_fname)
    
    out_df = pd.DataFrame(columns=df.columns)
    out_df.to_excel(output_fname)

