from json import dumps


def obj2json(obj):
    date_list = []
    value_list = []
    for record in obj:
        date_list.append(record['Date'])
        value_list.append(float(record['Value']))

    return dumps({'date': date_list, 'value': value_list, 'status': False})


def errorRep(erro):
    return dumps({'status': True, 'value': erro})