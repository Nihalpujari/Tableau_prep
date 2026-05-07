import pandas as pd

def process_employees(df): 
    avg_salary = df['Salary'].mean()
    oldest_idx = df['Age'].idxmax()
    oldest_name = df.loc[oldest_idx, 'Employee_Name']
    oldest_dept = df.loc[oldest_idx, 'Department']
    it_df = df[df['Department'] == 'IT'].copy()
    it_df['Average_Salary_All_Employees'] = round(avg_salary, 2)
    it_df['Oldest_Employee_Name'] = oldest_name
    it_df['Oldest_Employee_Department'] = oldest_dept
    it_df = it_df.reset_index(drop=True)
    return it_df

def get_output_schema():
    return pd.DataFrame({
        'Employee_ID':                   prep_string(),
        'Employee_Name':                 prep_string(),
        'Department':                    prep_string(),
        'Age':                           prep_int(),
        'Salary':                        prep_decimal(),
        'Hire_Date':                     prep_string(),
        'City':                          prep_string(),
        'Average_Salary_All_Employees':  prep_decimal(),
        'Oldest_Employee_Name':          prep_string(),
        'Oldest_Employee_Department':    prep_string(),
    })