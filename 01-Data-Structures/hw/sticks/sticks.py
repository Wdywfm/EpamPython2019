import json_parser2


def merge_lists(first, second):
    new_list = second
    for dicti in first:
        duplicate = False
        for dicty in second:
            if dicti == dicty:
                duplicate = True
                break
            else:
                pass
        if not duplicate:
            new_list.append(dicti)
    return new_list


def find_most_expensive_wine(info):
    max_price = 0
    most_expensive_wine = []
    for i, value in enumerate(info):
        if value['price'] and value['price'] > max_price:
            most_expensive_wine = []
            most_expensive_wine.append(value['title'])
            max_price = value['price']
        elif value['price'] and value['price'] == max_price:
            most_expensive_wine.append(value['title'])
    return most_expensive_wine, max_price


def find_cheapest_wine(info):
    min_price = None
    cheapest_wine = []
    for i, value in enumerate(info):
        if not i:
            min_price = value['price']
            cheapest_wine = []
            cheapest_wine.append(value['title'])
        else:
            if not min_price:
                min_price = value['price']
                cheapest_wine = []
                cheapest_wine.append(value['title'])
            elif min_price and value['price'] and value['price'] < min_price:
                min_price = value['price']
                cheapest_wine = []
                cheapest_wine.append(value['title'])
            elif min_price and value['price'] and value['price'] == min_price:
                cheapest_wine.append(value['title'])
    return cheapest_wine, min_price


def find_highest_score(info):
    highest_score = 0
    wines = []
    for i, value in enumerate(info):
        if value['points'] and int(value['points']) > highest_score:
            wines = []
            wines.append(value['title'])
            highest_score = int(value['points'])
        elif value['points'] and int(value['points']) == highest_score:
            wines.append(value['title'])
    return wines, highest_score


def find_lowest_score(info):
    lowest_score = None
    wines = []
    for i, value in enumerate(info):
        if not i:
            lowest_score = value['points']
            wines = []
            wines.append(value['title'])
        else:
            if not lowest_score:
                lowest_score = value['points']
                wines = []
                wines.append(value['title'])
            elif lowest_score and value['points']\
                    and int(value['points']) < int(lowest_score):
                lowest_score = value['points']
                wines = []
                wines.append(value['title'])
            elif lowest_score and value['points']\
                    and int(value['points']) == int(lowest_score):
                wines.append(value['title'])
    return wines, lowest_score


def find_most_expensive_and_cheapest_country(info):
    country_dict = {}
    country_counter_dict = {}
    for i, value in enumerate(info):
        if not value['country'] in country_dict:
            if value['price']:
                country_dict[value['country']] = value['price']
                country_counter_dict[value['country']] = 1
            else:
                country_dict[value['country']] = 0
                country_counter_dict[value['country']] = 0
        else:
            if value['price']:
                country_dict[value['country']] += value['price']
                country_counter_dict[value['country']] += 1
            else:
                pass
    for key in country_dict:
        if country_counter_dict[key]:
            country_dict[key] /= country_counter_dict[key]
    max_country = 0
    max_country_dict = []
    min_country_dict = []
    for key in country_dict:
        if country_dict[key] > max_country:
            max_country_dict = []
            max_country_dict.append(key)
            max_country = country_dict[key]
        elif country_dict[key] == max_country:
            max_country_dict.append(key)
    min_country = max_country
    for key in country_dict:
        if country_dict[key] < min_country and country_dict[key]:
            min_country_dict = []
            min_country_dict.append(key)
            min_country = country_dict[key]
        elif country_dict[key] == min_country:
            min_country_dict.append(key)
    return max_country_dict, max_country, min_country_dict, min_country


def find_most_rated_and_underrated_country(info):
    country_dict = {}
    country_counter_dict = {}
    for i, value in enumerate(info):
        if not value['country'] in country_dict:
            if value['points']:
                country_dict[value['country']] = int(value['points'])
                country_counter_dict[value['country']] = 1
            else:
                country_dict[value['country']] = 0
                country_counter_dict[value['country']] = 0
        else:
            if value['points']:
                country_dict[value['country']] += int(value['points'])
                country_counter_dict[value['country']] += 1
            else:
                pass
    for key in country_dict:
        country_dict[key] /= country_counter_dict[key]
    max_country = 0
    max_country_dict = []
    min_country_dict = []
    for key in country_dict:
        if country_dict[key] > max_country:
            max_country_dict = []
            max_country_dict.append(key)
            max_country = country_dict[key]
        elif country_dict[key] == max_country:
            max_country_dict.append(key)
    min_country = max_country
    for key in country_dict:
        if country_dict[key] < min_country:
            min_country_dict = []
            min_country_dict.append(key)
            min_country = country_dict[key]
        elif country_dict[key] == min_country:
            min_country_dict.append(key)
    return max_country_dict, max_country, min_country_dict, min_country


def find_most_active_commentator(info):
    commentators_dict = {}
    for i, value in enumerate(info):
        if value['taster_name'] in commentators_dict:
            commentators_dict[value['taster_name']] += 1
        else:
            if value['taster_name']:
                commentators_dict[value['taster_name']] = 1
    max_comments = 0
    commentators = []
    for key in commentators_dict:
        if commentators_dict[key] > max_comments:
            max_comments = commentators_dict[key]
            commentators = []
            commentators.append(key)
        elif commentators_dict[key] == max_comments:
            commentators.append(key)
    return commentators, max_comments


def find_average_price(info, variety):
    summa = 0
    counter = 0
    for i, value in enumerate(info):
        if value['variety'] == variety:
            if value['price']:
                summa += value['price']
                counter += 1
    return summa/counter if counter != 0 else -1


def find_average_score(info, variety):
    summa = 0
    counter = 0
    for i, value in enumerate(info):
        if value['variety'] == variety:
            if value['points']:
                summa += int(value['points'])
                counter += 1
    return summa / counter if counter != 0 else -1


def find_min_price(info, variety):
    min_price = None
    for i, value in enumerate(info):
        if variety == value['variety']:
            if not min_price:
                min_price = value['price']
            else:
                if value['price'] and value['price'] < min_price:
                    min_price = value['price']
    return min_price


def find_max_price(info, variety):
    max_price = 0
    for i, value in enumerate(info):
        if variety == value['variety']:
            if value['price'] and value['price'] > max_price:
                max_price = value['price']
    return max_price


def find_most_common_region(info, variety):
    region_dict = {}
    for i, value in enumerate(info):
        if variety == value['variety']:
            if value['region_1']:
                if value['region_1'] in region_dict:
                    region_dict[value['region_1']] += 1
                else:
                    region_dict[value['region_1']] = 1
            elif value['region_2']:
                if value['region_2'] in region_dict:
                    region_dict[value['region_2']] += 1
                else:
                    region_dict[value['region_2']] = 1
    max_region = 0
    region = ''
    for key in region_dict:
        if region_dict[key] > max_region:
            max_region = region_dict[key]
            region = key
    return region


def find_most_common_country(info, variety):
    country_dict = {}
    for i, value in enumerate(info):
        if variety == value['variety']:
            if value['country']:
                if value['country'] in country_dict:
                    country_dict[value['country']] += 1
                else:
                    country_dict[value['country']] = 1

    max_country = 0
    country = ''
    for key in country_dict:
        if country_dict[key] > max_country:
            max_country = country_dict[key]
            country = key
    return country


wine1 = open('winedata_1.json', 'r')
rwine1 = wine1.read()
wine2 = open('winedata_2.json', 'r')
rwine2 = wine2.read()
info1 = json_parser2.get_info(json_parser2.get_tokens(rwine1))
wine1.close()
info2 = json_parser2.get_info(json_parser2.get_tokens(rwine2))
wine2.close()

# Merge lists and delete duplicates
new_info = merge_lists(info2, info1)

# Replace None for sort
for value in new_info:
    if not value['price']:
        value['price'] = 0
    if not value['variety']:
        value['variety'] = 'zzz'

# Sort by variety
new_info.sort(key=lambda x: x['variety'])
# Sort by price, collisions will be sorted by variety
new_info.sort(key=lambda x: x['price'], reverse=True)

# Return None
for value in new_info:
    if not value['price']:
        value['price'] = None
    if value['variety'] == 'zzz':
        value['variety'] = None
print('dumping in process')

# Create winedata_full.json file and write info in it
wine_full = open('winedata_full.json', 'w')
wine_full.write(json_parser2.transform_to_json(new_info))
wine_full.close()

# Find statistics
most_expensive_wine = find_most_expensive_wine(new_info)
cheapest_wine = find_cheapest_wine(new_info)
highest_score = find_highest_score(new_info)
lowest_score = find_lowest_score(new_info)
most_expensive_and_cheapest_country =\
    find_most_expensive_and_cheapest_country(new_info)
most_expensive_country = most_expensive_and_cheapest_country[0]
cheapest_country = most_expensive_and_cheapest_country[2]
most_rated_and_underrated_country =\
    find_most_rated_and_underrated_country(new_info)
most_rated_country = most_rated_and_underrated_country[0]
underrated_country = most_rated_and_underrated_country[2]
most_active_commentator = find_most_active_commentator(new_info)
wine_dict = dict.fromkeys(('Gew\\u00fcrztraminer', 'Riesling', 'Merlot',
                           'Madeira Blend', 'Tempranillo', 'Red Blend'), None)
for key in wine_dict:
    wine_dict[key] = {}
    wine_dict[key]['average_price'] = find_average_price(new_info, key)
    wine_dict[key]['max_price'] = find_max_price(new_info, key)
    wine_dict[key]['min_price'] = find_min_price(new_info, key)
    wine_dict[key]['most_common_region'] =\
        find_most_common_region(new_info, key)
    wine_dict[key]['most_common_country'] =\
        find_most_common_country(new_info, key)
    wine_dict[key]['average_score'] = find_average_score(new_info, key)
print(wine_dict)
stat_dict = {'most_expensive_wine': most_expensive_wine[0],
             'cheapest_wine': cheapest_wine[0],
             'highest_score': highest_score[0],
             'lowest_score': lowest_score[0],
             'most_expensive_country': most_expensive_country,
             'cheapest_country': cheapest_country,
             'most_rated_country': most_rated_country,
             'underrated_country': underrated_country,
             'most_active_commentator': most_active_commentator[0]}
stat = {'statistics': [{'wine': wine_dict}, stat_dict]}
json = json_parser2.transform_to_json(stat)
stats = open('stats.json', 'w')
for i, char in enumerate(json):
    stats.write(char)
    if char in '{}' and char != json[0] and i != len(json)-1 and\
            json[i+1] != ',':
        stats.write('\n')
    elif char == ',' and json[i-1] in '}]':
        stats.write('\n')
stats.close()
