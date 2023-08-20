from actions import Data

test= Data()

'''
test.get_data()

test.add_data("Паршунин", "Вася", "Витальевич", "лалаленд", "+67456721276", "+765432907843", "9087")
test.get_data()
test.add_data(last_name="Дфвф", first_name="Анна", middle_name="Витальевна", organization="лалаленд", work_phone="+67456721276", code="9087")
test.get_data()
'''
condition = test.data['Last Name'].str.startswith('Ш')
test.find(condition=condition )
condition1 = test.data['Last Name'].str.len()==4
test.find(condition=condition1 )
condition2 = (test.data['Organization']=="Company B") & (test.data['Middle Name']=="Со")
test.find(condition=condition2 )
condition2 = test.data['Organization']=="Company C" 
test.change(func=lambda x:  "Пятерочка", condition=condition2, param='Organization')
