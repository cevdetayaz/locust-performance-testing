class Data:

    @classmethod
    def user_create_payload(cls):
        payload = {
            "id": 5555624421,
            "username": "cevdetpost",
            "firstName": "cevdet",
            "lastName": "ayaz",
            "email": "cevdetayaz@hotmail.com",
            "password": "231312",
            "phone": "565465",
            "userStatus": 0
        }
        return payload

    @classmethod
    def headers_payload(cls):
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        return headers

    @classmethod
    def params_payload(cls):
        params = {
            "username": "cevdet",
            "password": "123456"
        }
        return params

    @classmethod
    def create_user_with_list(cls):
        payload = [
            {
                "id": 1,
                "username": "testcevdet1",
                "firstName": "testcevdet1",
                "lastName": "testcevdet1",
                "email": "testcevdet1",
                "password": "testcevdet1",
                "phone": "111111",
                "userStatus": 0
            },
            {
                "id": 2,
                "username": "testcevdet2",
                "firstName": "testcevdet2",
                "lastName": "testcevdet2",
                "email": "testcevdet2",
                "password": "testcevdet2",
                "phone": "222222",
                "userStatus": 0
            }, {
                "id": 3,
                "username": "testcevdet3",
                "firstName": "testcevdet3",
                "lastName": "testcevdet3",
                "email": "testcevdet3",
                "password": "testcevdet3",
                "phone": "33333",
                "userStatus": 0
            },
            {
                "id": 4,
                "username": "testcevdet4",
                "firstName": "testcevdet4",
                "lastName": "testcevdet4",
                "email": "testcevdet4",
                "password": "testcevdet4",
                "phone": "444444",
                "userStatus": 0
            },
            {
                "id": 5,
                "username": "testcevdet5",
                "firstName": "testcevdet5",
                "lastName": "testcevdet5",
                "email": "testcevdet5",
                "password": "testcevdet5",
                "phone": "555555",
                "userStatus": 0
            }
        ]
        return payload

    @classmethod
    def create_user_with_array(cls):
        payload = [
            {
                "id": 111111111,
                "username": "testcevdet1",
                "firstName": "testcevdet1",
                "lastName": "testcevdet1",
                "email": "testcevdet1",
                "password": "testcevdet1",
                "phone": "111111",
                "userStatus": 0
            },
            {
                "id": 111111112,
                "username": "testcevdet2",
                "firstName": "testcevdet2",
                "lastName": "testcevdet2",
                "email": "testcevdet2",
                "password": "testcevdet2",
                "phone": "222222",
                "userStatus": 0
            }, {
                "id": 111111113,
                "username": "testcevdet3",
                "firstName": "testcevdet3",
                "lastName": "testcevdet3",
                "email": "testcevdet3",
                "password": "testcevdet3",
                "phone": "33333",
                "userStatus": 0
            },
            {
                "id": 111111114,
                "username": "testcevdet4",
                "firstName": "testcevdet4",
                "lastName": "testcevdet4",
                "email": "testcevdet4",
                "password": "testcevdet4",
                "phone": "444444",
                "userStatus": 0
            },
            {
                "id": 111111115,
                "username": "testcevdet5",
                "firstName": "testcevdet5",
                "lastName": "testcevdet5",
                "email": "testcevdet5",
                "password": "testcevdet5",
                "phone": "555555",
                "userStatus": 0
            },
            {
                "id": 111111116,
                "username": "testcevdet6",
                "firstName": "testcevdet6",
                "lastName": "testcevdet6",
                "email": "testcevdet6",
                "password": "testcevdet6",
                "phone": "666666",
                "userStatus": 0
            },
            {
                "id": 111111117,
                "username": "testcevdet7",
                "firstName": "testcevdet7",
                "lastName": "testcevdet7",
                "email": "testcevdet7",
                "password": "testcevdet7",
                "phone": "777777777",
                "userStatus": 0
            }, {
                "id": 3,
                "username": "testcevdet8",
                "firstName": "testcevdet8",
                "lastName": "testcevdet3",
                "email": "testcevdet8",
                "password": "testcevdet8",
                "phone": "888888",
                "userStatus": 0
            },
            {
                "id": 111111118,
                "username": "testcevdet8",
                "firstName": "testcevdet8",
                "lastName": "testcevdet8",
                "email": "testcevdet8",
                "password": "testcevdet8",
                "phone": "88888888",
                "userStatus": 0
            },
            {
                "id": 111111119,
                "username": "testcevdet9",
                "firstName": "testcevdet9",
                "lastName": "testcevdet9",
                "email": "testcevdet9",
                "password": "testcevdet9",
                "phone": "99999999",
                "userStatus": 0
            }
        ]
        return payload




