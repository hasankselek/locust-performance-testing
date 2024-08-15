class Data:


    @classmethod
    def headers_payload(cls):
        headers_payload = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        return headers_payload

    @classmethod
    def params_payload(cls):
        params_payload = {
            "username": "hasankselek",
            "password": "Test1234."
        }

        return params_payload

    @classmethod
    def user_create_payload(cls):
        payload = {
            "id": 1187,
            "username": "hasankselek",
            "firstName": "hasan",
            "lastName": "kucukselek",
            "email": "testotomasyonu09@gmail.com",
            "password": "Test1234.",
            "phone": "5555555555",
            "userStatus": 1
        }

        return payload

    @classmethod
    def user_update_payload(cls):
        payload = {
            "id": 2342342342,
            "username": "hasankselek",
            "firstName": "haasan",
            "lastName": "kselek",
            "email": "testotomasyonu@gmail.com",
            "password": "Test123",
            "phone": "3333333333",
            "userStatus": 1
        }

        return payload

    @classmethod
    def user_create_with_list(cls):
        payload = [
            {
                "id": 11111,
                "username": "hasan1",
                "firstName": "hasan1",
                "lastName": "kselek1",
                "email": "testotomasyonu@gmail.com",
                "password": "Test123",
                "phone": "123123123123",
                "userStatus": 1
            },
            {
                "id": 11112,
                "username": "hasan2",
                "firstName": "hasan2",
                "lastName": "kselek2",
                "email": "testotomasyonu@gmail.com",
                "password": "Test123",
                "phone": "123123123123",
                "userStatus": 1
            },
            {
                "id": 11113,
                "username": "hasan3",
                "firstName": "hasan3",
                "lastName": "kselek3",
                "email": "testotomasyonu@gmail.com",
                "password": "Test123",
                "phone": "123123123123",
                "userStatus": 1
            }, {
                "id": 11114,
                "username": "hasan4",
                "firstName": "hasan4",
                "lastName": "kselek4",
                "email": "testotomasyonu@gmail.com",
                "password": "Test123",
                "phone": "123123123123",
                "userStatus": 1
            },
            {
                "id": 11115,
                "username": "hasan5",
                "firstName": "hasan5",
                "lastName": "kselek5",
                "email": "testotomasyonu@gmail.com",
                "password": "Test123",
                "phone": "123123123123",
                "userStatus": 1
            }
        ]

        return payload

    @classmethod
    def user_create_with_array(cls):
        payload = [
            {
                "id": 11111,
                "username": "hasan1",
                "firstName": "hasan1",
                "lastName": "kselek1",
                "email": "testotomasyonu@gmail.com",
                "password": "Test123",
                "phone": "123123123123",
                "userStatus": 1
            },
            {
                "id": 1112,
                "username": "hasan2",
                "firstName": "hasan2",
                "lastName": "kselek2",
                "email": "testotomasyonu@gmail.com",
                "password": "Test123",
                "phone": "123123123123",
                "userStatus": 1
            },
            {
                "id": 1113,
                "username": "hasan3",
                "firstName": "hasan3",
                "lastName": "kselek3",
                "email": "testotomasyonu@gmail.com",
                "password": "Test123",
                "phone": "123123123123",
                "userStatus": 1
            }, {
                "id": 1114,
                "username": "hasan4",
                "firstName": "hasan4",
                "lastName": "kselek4",
                "email": "testotomasyonu@gmail.com",
                "password": "Test123",
                "phone": "123123123123",
                "userStatus": 1
            },
            {
                "id": 1115,
                "username": "hasan5",
                "firstName": "hasan5",
                "lastName": "kselek5",
                "email": "testotomasyonu@gmail.com",
                "password": "Test123",
                "phone": "123123123123",
                "userStatus": 1
            }, {
                "id": 1116,
                "username": "hasan6",
                "firstName": "hasan6",
                "lastName": "kselek6",
                "email": "testotomasyonu@gmail.com",
                "password": "Test123",
                "phone": "123123123123",
                "userStatus": 1
            }, {
                "id": 1117,
                "username": "hasan7",
                "firstName": "hasan7",
                "lastName": "kselek7",
                "email": "testotomasyonu@gmail.com",
                "password": "Test123",
                "phone": "123123123123",
                "userStatus": 1
            },
            {
                "id": 1118,
                "username": "hasan8",
                "firstName": "hasan8",
                "lastName": "kselek8",
                "email": "testotomasyonu@gmail.com",
                "password": "Test123",
                "phone": "123123123123",
                "userStatus": 1
            }, {
                "id": 1119,
                "username": "hasan9",
                "firstName": "hasan9",
                "lastName": "kselek9",
                "email": "testotomasyonu@gmail.com",
                "password": "Test123",
                "phone": "123123123123",
                "userStatus": 1
            }, {
                "id": 11110,
                "username": "hasan10",
                "firstName": "hasan10",
                "lastName": "kselek10",
                "email": "testotomasyonu@gmail.com",
                "password": "Test123",
                "phone": "123123123123",
                "userStatus": 1
            }
        ]

        return payload