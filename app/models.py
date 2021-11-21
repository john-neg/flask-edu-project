import requests


# class ApeksData:
#     # getting ID of first active user (need to make general API data request)
#     payload = {'table': 'state_staff',
#                'filter[active]': '1'}
#     active_staff_id = requests.get(ApeksAPI.URL + '/api/call/system-database/get?token='
#                                    + ApeksAPI.TOKEN, params=payload).json()['data'][0]['id']
#
#     # getting data about organisation structure
#     payload = {'staff_id': active_staff_id,
#                'month': date.today().strftime('%m'),
#                'year': date.today().strftime('%Y')}
#     data = requests.get(ApeksAPI.URL + '/api/call/schedule-schedule/staff?token='
#                         + ApeksAPI.TOKEN, params=payload)
#     # getting data about recent staff
#     staff = data.json()['data']['staff']
#     # getting data about divisions
#     departments = data.json()['data']['departments']
#     # getting data about disciplines
#     payload = {'table': 'plan_disciplines',
#                'filter[level]': '3'}
#     plan_disciplines = requests.get(ApeksAPI.URL + '/api/call/system-database/get?token='
#                                     + ApeksAPI.TOKEN, params=payload).json()['data']
