import math
# If using list to create multiple values with one header list must be equal or create every time as a separate object
# If two first list equal and the last not it will return good value DDDDDD


class CreateHtml:

    """
    method create_simple_html
    - accepts **kwargs like h1 = , p = ,a = , b =, i =, and etc
    - you can pass as many params as you wish as strings

    1. Example
    CreateHtml.create_simple_htm(h1 = 'title', p='Text)
    return -----> [<h1>title</h1>,<p>Text</p>]
    The lis of converted values will be returned

    method create_html_mail_from_list
    - accepts **kwargs like h1 = , p = ,a = , b =, i =, and etc
    - values has to be equal lists -> h1 = ['Header1, 'Header2], p = ['Text 1', 'Text2']
    - if you want to pass single values or without lists use create_simple_html method
    - this method can be used to create a bunch of logical html blocks

    1. Example
    CreateHtml.create_html_mail_from_list(h1 = [Header1, Header2], p = [Text1, Text2], b = [B1, B2]
    return --> a list [Header1,Text1,B1,Header2,Text2,B2] all values converted to html as well
    """

    @staticmethod
    def create_simple_html(**kwargs):
        html_list = []
        for key, value in kwargs.items():
            if isinstance(value, str):
                html_list.append(CreateHtml.key_checker(key, value))
            else:
                raise Exception('Values have to be a strings')
        return html_list

    @staticmethod
    def create_html_mail_from_list(**kwargs):
        order_list = []
        order_keys = []
        # Checking for list class of instances
        for keys, values in kwargs.items():
            if isinstance(values, list):
                order_list.append({keys: values})
                order_keys.append(keys)
            else:
                raise Exception('All values have to be a list !')

        html_converted_values = []
        # Creating html converted values
        for key in range(len(order_keys)):
            print(key)
            key_ = order_keys[key]
            current_list = order_list[key][order_keys[key]]
            for value in current_list:
                html_converted_values.append(CreateHtml.key_checker(key_, value))

        # Sorting values of list by checking how many keys we have and values
        sort_list = []
        # In Case of not equal list going to round up
        if len(order_keys) == 0:
            step = 1
        else:
            step = math.ceil((len(html_converted_values) / len(order_keys)))
        start = 0
        for starting_number in range(step):
            for order in range(start, len(html_converted_values), step):
                sort_list.append(html_converted_values[order])
            start += 1
        return sort_list

    @staticmethod
    def key_checker(key, value):
        text = ''
        if key == 'h1':
            text += f'<h1>{value}</h1>'
        elif key == 'b':
            text += f'<b>{value}</b>'
        elif key == 'p':
            text += f'<p>{value}</p>'
        elif key == 'i':
            text += f'<i>{value}</i>'
        elif key == 'a':
            text += f'<a href={value} >Visit Article Page</a>'
        return text
