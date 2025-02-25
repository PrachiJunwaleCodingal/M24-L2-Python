#pip install pandas (on terminal)
import pandas as pd
import numpy as np

exam_data={'name':['Prachi', 'Pihu', 'Ayan', 'Ahmed', 'Swati', 'Mic', 'Ayana', 'Lisa', 'John', 'Aru'],
        'score': [12, 10.5, 16.5, np.nan, 9.5, 20, 14.5, 20, 8, 19],
        'attmpt': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}


sr_no = [1,2,3,4,5,6,7,8,9,10]
df = pd.DataFrame(exam_data , index=sr_no)
print("DataFrame and its data:")
print(df.info())