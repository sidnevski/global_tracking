import json

users = {
    "qr": [{
        "userHostKey":"TESTHOST",
        "clientId":"ORQRUSER1",
        "clientSecret":"0901ce169c7c960a488e4e1c58d50ca1056eaf01288fef8b718223bf92b58883"
    }],
    'afkl': [{
        'username': 'ubne6w8ytcrneh3fa7msmnw2',
        'password': 'ky3sytdTHX'
    }]
}

def get_qr_user():
    return users['qr'][0]

def get_afkl_user():
    return users['afkl'][0]