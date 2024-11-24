import pandas as pd

def fetch_df(fname, param_indexcol, param_header):
    old_df = pd.read_excel(fname, index_col=param_indexcol, header=param_header)
    return old_df
    pass    

def update_new_df(newfile, new_df, row):
    row_df = pd.DataFrame.from_dict([row])
    
    # Just to suppress warning about concat to empty df
    if new_df.empty:
        new_df = row_df
    else:
        new_df = pd.concat([new_df, row_df])
        
    new_df.to_excel(newfile)
    return new_df


def extractRowData(row):
    u_data = {
    "u_id" : row['ID'], 
    "u_firstname" : row['First Name'],
    "u_lastname" : row['Last Name'],
    "u_url" : row['URL'],
    "u_email" : row['Email Address'],
    "u_company" : row['Company'],
    "u_position" : row['Position'],
    "u_connected" : row['Connected On'],
    "u_gender" : row['Gender'],
    "u_ethnicity" : row['Ethnicity'],
    "u_age" : row['Age Bracket'],
    "u_industry" : row['Industry']
    }

    return u_data

def constructOutputRowDict(f_data):
    row_dict = {
        "ID" :f_data["f_id"],
        "First Name" :f_data["f_firstname"],
        "Last Name" :f_data["f_lastname"],
        "URL" :f_data["f_url"],
        "Email Address" :f_data["f_email"],
        "Company" :f_data["f_company"],
        "Position" :f_data["f_position"],
        "Connected On" :f_data["f_connected"],
        "Gender" :f_data["f_gender"],
        "Ethnicity" :f_data["f_ethnicity"],
        "Age Bracket" :f_data["f_age"],
        "Industry" :f_data["f_industry"]
    }
    
    print(row_dict["ID"])
    
    return row_dict
    
