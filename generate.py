import numpy as np
import pandas as pd
import random

def generate_phone_number():
    digits = random.choices("0123456789", k=9)  
    return str("+7" + ''.join(digits) )

num_records = 32#количество строк

first_names = np.random.choice(['Анна', 'Андрей', 'Василий', 'Джек', 'Рита'], num_records)
last_names = np.random.choice(['Шукшин(а)', 'Роро', 'Нана', 'Лоло', 'Заза'], num_records)
middle_names = np.random.choice(['До', 'РЕ', 'мИ', 'ФА', 'Со'], num_records)
organizations = np.random.choice(['Company A', 'Company B', 'Company C', 'Company D', 'Company E'], num_records)
work_phones = [generate_phone_number() for _ in range(num_records)]
personal_phones =  [generate_phone_number() for _ in range(num_records)]
codes = np.random.randint(1000, 9999, num_records)

# Создание DataFrame из данных
data = {
    'Last Name': last_names,
    'First Name': first_names,
    'Middle Name': middle_names,
    'Organization': organizations,
    'Work Phone': work_phones,
    'Personal Phone': personal_phones
}
df = pd.DataFrame(data)
df['Work Phone'] = df['Work Phone'].astype(str)
csv_filename = "data.csv"
df.to_csv(csv_filename, index=False)

print(f"Данные сохранены в {csv_filename}")

 
