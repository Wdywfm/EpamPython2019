from collections import deque


def is_string(json):
    string = ''
    if json[0] != '"':
        return string, json
    else:
        json.popleft()
    for c in json:
        if c == '"' and string[len(string)-1] != '\\':
            for i in range(len(string)+1):
                json.popleft()
            return string, json
        else:
            string += str(c)


def is_number(json):
    number = ''
    for n in json:
        if n not in "0123456789.-":
            if '.' in number:
                for i in range(len(number)):
                    json.popleft()
                return float(number), json
            elif number:
                for i in range(len(number)):
                    json.popleft()
                return int(number), json
            else:
                return None, json
        else:
            number += str(n)


def is_bool(json):
    info = ''
    if json[0] != 't' or json[0] != 'f':
        return None, json
    for c in json:
        if len(info) == 4:
            if info == 'true':
                for i in range(4):
                    json.popleft()
                return True, json
            elif info == 'fals':
                for i in range(4):
                    json.popleft()
                return False, json
            else:
                return None, json
        else:
            info += str(c)


def is_none(json):
    info = ''
    if json[0] != 'n':
        return None, json
    for c in json:
        if len(info) == 4:
            if info == 'null':
                for i in range(4):
                    json.popleft()
                return True, json
            else:
                return None, json
        else:
            info += str(c)


def get_tokens(json: str) -> list:
    tokens = []
    json2 = deque(json)
    while json2:
        print(len(json2))
        string, json2 = is_string(json2)
        if string:
            tokens.append(string)
            continue
        number, json2 = is_number(json2)
        if number:
            tokens.append(number)
            continue
        if json2[0] in 'nft':
            boolean, json2 = is_bool(json2)
            if boolean is not None:
                tokens.append(boolean)
                continue
            nothing, json2 = is_none(json2)
            if nothing:
                tokens.append(None)
                continue
        if json2[0] in "{}[]:,":
            tokens.append(json2[0])
            json2.popleft()
        elif json2[0] in " \n":
            json2.popleft()
    return tokens


def get_list(tokens):
    out_list = []
    while tokens[0] != ']':
        if tokens[0] == '[':
            tokens.popleft()
            arg, tokens = get_list(tokens)
            out_list.append(arg)
        elif tokens[0] == '{':
            tokens.popleft()
            arg, tokens = get_dict(tokens)
            out_list.append(arg)
        elif tokens[0] == ',':
            tokens.popleft()
        else:
            out_list.append(tokens[0])
            tokens.popleft()
    else:
        tokens.popleft()
        return out_list, tokens


def get_dict(tokens):
    out_dict = {}
    while tokens[0] != '}':
        if tokens[2] == '[':
            key = tokens[0]
            for i in range(3):
                tokens.popleft()
            out_dict[key], tokens = get_list(tokens)
        elif tokens[2] == '{':
            key = tokens[0]
            for i in range(3):
                tokens.popleft()
            out_dict[key], tokens = get_dict(tokens)
        elif tokens[0] in ':,':
            tokens.popleft()
        else:
            out_dict[tokens[0]] = tokens[2]
            for i in range(3):
                tokens.popleft()
    else:
        tokens.popleft()
        return out_dict, tokens


def get_info(tokens: list):
    tokens = deque(tokens)
    while tokens:
        print(len(tokens))
        if tokens[0] == '[':
            tokens.popleft()
            my_list, toks = get_list(tokens)
            if toks:
                return my_list, toks
            else:
                return my_list
        elif tokens[0] == '{':
            tokens.popleft()
            return get_dict(tokens)
        elif tokens[0] == ',':
            tokens.popleft()


def transform_to_json(smth) -> str:
    string = ''
    if type(smth) == list:
        string = '['
        for i, s in enumerate(smth):
            string += transform_to_json(s)
            if i == len(smth)-1:
                string += ']'
            else:
                string += ', '
        return string
    elif type(smth) == dict:
        string += '{'
        for i, (key, value) in enumerate(smth.items()):
            string += f'"{key}": {transform_to_json(value)}'
            if i == len(smth)-1:
                string += '}'
            else:
                string += ', '
        return string

    elif type(smth) == int or type(smth) == float:
        return str(smth)
    elif smth is None:
        return 'null'
    elif smth is True:
        return 'true'
    elif smth is False:
        return 'false'
    elif type(smth) == str:
        return f'"{smth}"'
