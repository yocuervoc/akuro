import datetime
import re
def date_calculator(json):

    json_parts = json.split('\"')
    str_date = json_parts[3].split('-')
    date = datetime.datetime(int(str_date[0]), int(str_date[1]), int(str_date[2]))
    
    return (date + datetime.timedelta(days=20))
    