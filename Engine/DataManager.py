data = {}

def get_data(key):
    return data.get(key, None)

def set_data(key, value):
    data[key] = value
