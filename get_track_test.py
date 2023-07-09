# Марат Гайфуллин, 6-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request


# Функция для позитивной проверки
def test_positive_assert():
    track_response = sender_stand_request.get_track_order()
    # Проверяем, что код ответа получения номера заказа равен 200
    assert track_response.status_code == 200