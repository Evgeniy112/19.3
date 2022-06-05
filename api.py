import requests


class Moyklass:
    def __init__(self):
        self.base_url = "https://app.moyklass.com/"


    def get_api_key(self, email, password):
        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url + 'settings/settings/api/api/api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result


    def get_api_lessonRecords(self, date, paid, userId, includeLessons,
                              includeBills, includeUserSubscriptions, limit,
                              offset, sort):
        headers = {
            'date': date,
            'paid': paid,       #boolean paid = true только платные записи
            'userId': userId,   #userId = 123 ID записанного ученика
            'includeLessons': includeLessons, #boolean Default: false
            'includeBills': includeBills, #boolean Default: false
            'includeUserSubscriptions': includeUserSubscriptions,   #boolean Default: false Example:
            'limit': limit,     #integer <= 500 Default: 100 Максимальное количество
                                # возвращаемых строк.Используется для постраничного вывода.
            'offset': offset,  #integer Default: 0 Номер первой записи.Используется для постраничного вывода.
            'sort': sort,    #string Default: "id" Enum: "id" "date" Поле сортировки
        }

        res = requests.get(self.base_url + 'v1/user/lessonRecords', headers=headers)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result