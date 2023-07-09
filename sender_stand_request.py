import configuration
import requests
import data


# Функция для создания нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.ORDER_CREATION_PATH,
                         json=body)


response = post_new_order(data.body_order);

print(response.status_code)
print(response.json()["track"])

# Сохраняем в переменную номер трекера созданного заказа
t = response.json()["track"]


# Функция для получения заказа по его номеру
def get_track_order():
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK_PATH, params={"t": t})


response = get_track_order();

print(response.status_code)
print(response.json())
