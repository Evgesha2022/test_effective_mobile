import numpy as np
import pandas as pd
class Data:
    def __init__(self) :
        csv_filename = "data.csv"
        self.data=pd.read_csv(csv_filename,dtype={'Work Phone': str, 'Personal Phone': str})
        
    
    def save_data(self, csv_filename="data.csv"):
        self.data.to_csv(csv_filename, index=False)

    def get_data(self, data=None,  rows_per_page=10)->None:
        
        if data is None:
            data=self.data
        total_rows = len(data)
        for start_idx in range(0, total_rows, rows_per_page):
            print(data[start_idx:start_idx + rows_per_page])
            input("При нажатии Enter, переход на новую страницу ") 
        print("Конец файла\n"+"\n")
        

    def add_data(self, last_name:str = None, first_name: str = None, middle_name: str =None, organization: str = None, work_phone: str = None,
                 personal_phone: str = None,  code:int = None ):
        new_row = {
    'Last Name': last_name,
    'First Name': first_name,
    'Middle Name': middle_name,
    'Organization': organization,
    'Work Phone': work_phone,
    'Personal Phone': personal_phone,
    'Code': code
    }
        self.data = pd.concat([self.data, pd.DataFrame([new_row])], ignore_index=True)
        self.save_data()
    
    def change(self,func,  condition, param):
        if self.data.loc[condition, param].empty==False:
            self.data.loc[condition, param] =self.data.loc[condition, param].apply(func)
            self.get_data()
            self.save_data()
        else:
            print("Данные не найдены")

    def find(self, condition):
        if self.data.loc[condition].empty==False:
            self.get_data(self.data.loc[condition])
        else:
            print("Данные не найдены")

    
    
    


