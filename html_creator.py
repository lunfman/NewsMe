import math
import os

class CreateHtml:

    def __init__ (self, path):
        self.html = ''
        self.template_path = os.path.dirname(os.path.realpath(__file__))
        self.template = ''
        self.html_list = []


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

    def create_simple_html(self,**kwargs):
        # this function can create a simple html block by providing html tags and values
        # after completing function saves result to self.html_list
        array = []
        for key, value in kwargs.items():
            if isinstance(value, str):
                # adding html element to an empty array
                array.append(CreateHtml.key_checker(key, value))
            # else:
            #     raise Exception('Values have to be a strings')
        
        # checking i array is empty
        if len(array) == 0:
            return
        # return -> save empty array to html_list
        return self.html_list.append(array)

    def create_html_mail_from_list(self, **kwargs):
        # this function can create multiple blocks of html
        # h1 = ['heading 1', 'heading 2'] p = ['par 1', 'par 2']
        # the lists length has to be equal
        order_list = []
        order_keys = []
        
        len_checker = 0
        # running a for loop to get keys, create order list and get the len of the arrays
        for keys, values in kwargs.items():
            # Checking for list class of instances
            if isinstance(values, list):
                # if len_checker = 0 it meas we are checking for the first list
                # this allow to get len of the first list and compare with next lists
                # if not equal raise error cause this function will not retrun the right result
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
            # else:
            #     raise Exception('All values have to be a list !')

        for num in range(len_checker):
            print(num)
            # saveing html block to the array
            array = []
            for key in order_keys:
                print(key)
                key_index = order_keys.index(key)
                current_value = order_list[key_index][key][num]
                array.append(CreateHtml.key_checker(key, current_value))

            self.html_list.append(array)

    @staticmethod
    def key_checker(key, value):
        # key_checker function takes two arguments one is the key -> h1,b,i -> html tag
        # second is value for the key
        text = ''
        if key == 'h1':
            text += f'<h1>{value}</h1>'
            return text
        elif key == 'b':
            text += f'<b>{value}</b>'
            return text            
        elif key == 'p':
            text += f'<p>{value}</p>'
            return text            
        elif key == 'i':
            text += f'<i>{value}</i>'
            return text            
        elif key == 'a':
            text += f'<a href={value} >Visit Article Page</a>'
            return text
        return text            
