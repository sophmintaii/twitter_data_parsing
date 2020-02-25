import json


def get_decoded_json(path):
    '''
    str -> dict
    returns a decoded dictionary from the json file
    '''
    with open(path, 'r', encoding='utf-8') as f:
        decoded = json.load(f)
    return decoded


def get_list(dictionary):
    '''
    dict -> list
    returns list of dictionary keys
    '''
    return list(dictionary.keys())


def get_key(data):
    '''
    dict -> str
    returns value of key
    '''
    if isinstance(data, dict):
        keys = get_list(data)
        print('Available keys: ', str(keys))
        key = input("Enter key: ")
        while key not in keys:
            key = input("Wrong value entered, repeat: ")
        value = data[key]
    else:
        return data
    if isinstance(value, dict):
        print('Value is a dictionary.')
        return get_key(value)
    if isinstance(value, list):
        length = len(value)
        print('Value is a list.')
        input_str = 'Enter number in range 0 to ' + \
            str(length - 1) + ' to show an element under this number: '
        index = input(input_str)
        while not index.isdigit():
            index = input('Wrong value entered. Repeat: ')
        while not int(index) in list(range(length)):
            index = input('Wrong value entered. Repeat: ')
        index = int(index)
        return get_key(value[index])
    else:
        return value


if __name__ == '__main__':
    data = get_decoded_json(
        '/home/smint/Documents/sem2/labs/lab3/twitter_data_parsing/twitter_data.json')
    print(get_key(data))
