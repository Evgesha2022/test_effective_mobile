from actions import Data

test= Data()

''''''
test.get_data()

test.add_data("Паршунин", "Вася", "Витальевич", "лалаленд", "+67456721276", "+765432907843")
test.get_data()

test.add_data(last_name="Дфвф", first_name="Анна", middle_name="Витальевна", organization="лалаленд", work_phone="+67456721276")
test.get_data()

condition = test.data['Last Name'].str.startswith('Ш')
cond_data=test.find(condition=condition )
test.get_data(cond_data)

condition1 = test.data['Last Name'].str.len()==4
cond_data1=test.find(condition=condition1 )
test.get_data(cond_data1)

condition2 = (test.data['Organization']=="Company B") & (test.data['Middle Name']=="Со")
cond_data2=test.find(condition=condition2 )
test.get_data(cond_data2)

condition2 = test.data['Organization']=="Company C" 
change_data1=test.change(func=lambda x:  "Пятерочка", condition=condition2, param='Organization')
test.get_data(change_data1)

test.save_data(data=change_data1, csv_filename="organization_5.csv")#сохраним данные в отдельный файл
#test.save_data()#сохранятся все изменения

