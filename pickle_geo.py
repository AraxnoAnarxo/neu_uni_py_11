import pickle
from home_work import Geologic_time_scale

# Сериализация

data = Geologic_time_scale(100000)
f = open('geo.pkl', 'wb')
pickle.dump(data, f)
f.close()

# Десериализация - выдает ошибку

f = open('geo.pkl', 'rb')
new_data = pickle.load(f)
print(new_data)
f.close()