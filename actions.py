import numpy as np
import pandas as pd
class Data:
    def __init__(self) :
        csv_filename = "data.csv"
        self.data=pd.read_csv(csv_filename,dtype={'Work Phone': str, 'Personal Phone': str})
        
    #Метод сохранения
    #аргументы: название файла.
    def save_data(self, data: pd.DataFrame=None, csv_filename:str="data.csv") ->None:
        if data is None:
            self.data.to_csv(csv_filename, index=False)
        else:
            data.to_csv(csv_filename, index=False)
        
    #Метод получения данных в консоль по страницам
    #аргументы: данные, если они не передались, выводятся все; размер страницы (количество строк).
    def get_data(self, data: pd.DataFrame=None,  rows_per_page: int=10)->None:
        
        if data is None:
            data=self.data
        total_rows = len(data)
        for start_idx in range(0, total_rows, rows_per_page):
            print(data[start_idx:start_idx + rows_per_page])
            input("При нажатии Enter, переход на новую страницу ") 
        print("Конец файла\n"+"\n")

    #Метод добавления
    #аргументы: все значения строки по столбцам, в случае если что-то не дано прописывается None.
    def add_data(self, last_name:str = None, first_name: str = None, middle_name: str =None, organization: str = None, work_phone: str = None,
                 personal_phone: str = None ) ->None:
        new_row = {
    'Last Name': last_name,
    'First Name': first_name,
    'Middle Name': middle_name,
    'Organization': organization,
    'Work Phone': work_phone,
    'Personal Phone': personal_phone,
    }
        self.data = pd.concat([self.data, pd.DataFrame([new_row])], ignore_index=True)
        self.save_data()

    #Метод изменения данных
    #аргументы: функция для изменений данных, условие поиска данных, столбец в котором меняются данные.
    #возвращает измененные данные согласно условию
    def change(self,func,  condition: pd.core.series.Series, param: str) ->pd.DataFrame():
        if self.data.loc[condition, param].empty==False:
            self.data.loc[condition, param] =self.data.loc[condition, param].apply(func)
            return self.data.loc[condition]
        else:
            print("Данные не найдены")

    #Метод поиска данных
    #аргументы: условие поиска данных.
    #возвращает Dataframe с необходимыми данными.
    def find(self, condition: pd.core.series.Series) ->pd.DataFrame():
        if self.data.loc[condition].empty==False:
            return self.data.loc[condition]
        else:
            print("Данные не найдены")

    
    
    


