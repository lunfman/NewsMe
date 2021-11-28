import math

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
        len_checker = 0
        for keys, values in kwargs.items():
            if isinstance(values, list):
                if len_checker == 0:
                    len_checker = len(values)
                    order_list.append({keys: values})
                    order_keys.append(keys)
                else:
                    if len(values) != len_checker:
                        raise Exception('Lists length has to be equal')
                    else:
                        order_list.append({keys: values})
                        order_keys.append(keys)
            else:
                raise Exception('All values have to be a list !')

        sorted_list = []
        for num in range(len_checker):
            print(num)
            for key in order_keys:
                print(key)
                key_index = order_keys.index(key)
                current_value = order_list[key_index][key][num]
                sorted_list.append(CreateHtml.key_checker(key, current_value))

        return sorted_list

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