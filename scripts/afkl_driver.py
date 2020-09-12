import urllib
import urllib.request
import json
import ssl
import scripts.users
import base64

auth_url = 'https://api-ute2-ext.airfranceklm.com/cargo/tracking/oauth'
track_url = 'https://api-ute2-ext.airfranceklm.com/cargo/tracking/v2/public/shipments'

def get_access():
    user = scripts.users.get_afkl_user()
    user_base64 = base64.b64encode(
        ('%s:%s' % (user['username'], user['password'])).encode('ascii')
    ).decode('utf-8')
    auth_req = urllib.request.Request(
        auth_url,
        headers={
            'content-type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic %s' % (user_base64)
        },
        # data = bytes(json.dumps({
        #     'grant_type': 'client_credentials'
        # }).encode('utf8'))
        data = urllib.parse.urlencode({
            'grant_type': 'client_credentials'
        }).encode('utf8')
    )
    print(auth_req.__dict__)

    auth_res = urllib.request.urlopen(auth_req, context=ssl._create_unverified_context())
    auth_data = json.loads(auth_res.read())
    return auth_data['accessToken']

def track_shipment(track_request_data):
    # access_token = get_access()
    access_token = 'n726vt8mmha7mge4utshm9bu'
    # print(access_token)

    req_awb = '/%s' % (track_request_data)
    req_filters = '?expand=shipment-characteristics'
    track_req = urllib.request.Request(
        track_url + req_awb + req_filters,
        headers={
            'content-type': 'application/json',
            'Authorization': 'Bearer %s' % (access_token)
        }
    )
    print(track_req.__dict__)

    track_res = urllib.request.urlopen(track_req, context=ssl._create_unverified_context())
    track_data = json.loads(track_res.read())
    return track_data