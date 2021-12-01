import math
import os
from re import template

class CreateHtml:

    def __init__ (self, path = f'{os.path.dirname(os.path.realpath(__file__))}/template.html'):
        # html is going to store extracted html
        self.html = ''
        # path for the template
        self.template_path = path
        # store template after read
        self.template = ''
        # stores html blocks
        self.html_list = []


    """
    method create_simple_html
    - accepts **kwargs like h1 = , p = ,a = , b =, i =, and etc
    - you can pass as many params as you wish as strings

    1. Example
    CreateHtml.create_simple_htm(h1 = 'title', p='Text)
    return -----> [<h1>title</h1>,<p>Text</p>]
    The list of converted values will be returned 

    method create_html_mail_from_list
    - accepts **kwargs like h1 = , p = ,a = , b =, i =, and etc
    - values has to be equal lists -> h1 = ['Header1, 'Header2], p = ['Text 1', 'Text2']
    - if you want to pass single values or without lists use create_simple_html method
    - this method can be used to create a bunch of logical html blocks

    1. Example
    CreateHtml.create_html_mail_from_list(h1 = [Header1, Header2], p = [Text1, Text2], b = [B1, B2]
    return --> a list [[Header1,Text1,B1],[Header2,Text2,B2]] all values converted to html as well
    """

    def create_simple_html(self,**kwargs):
        # this function can create a simple html block by providing html tags and values
        # after completing function saves result to self.html_list as a new list
        array = []
        for key, value in kwargs.items():
            if isinstance(value, str):
                # adding html element to an empty array
                # CreateHtml.key_checker creates html elements from key and value
                array.append(CreateHtml.key_checker(key, value))
            # else:
            #     raise Exception('Values have to be a strings')
        
        # checking if an array is empty
        if len(array) == 0:
            return
        # return -> save empty array to html_list
        return self.html_list.append(array)

    def create_html_mail_from_list(self, **kwargs):
        #TODO this functions looks complex do refactor after!
        # this function can create multiple blocks of html
        # h1 = ['heading 1', 'heading 2'] p = ['par 1', 'par 2']
        # the lists length has to be equal or the function will not return a proper result

        # why do we need order_list and order_keys?
        # order_keys stores all keys needed to create blocks
        # order_list stores key:[values]
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
                    # if it was first run len_checker = len of the list
                    len_checker = len(values)
                    # save values
                    order_list.append({keys: values})
                    order_keys.append(keys)
                else:
                    if len(values) != len_checker:
                        raise Exception('Lists length has to be equal')
                    # if lists have the same length continue 
                    else:
                        # save values to order list
                        order_list.append({keys: values})
                        # save keys to order_keys
                        order_keys.append(keys)
            # else:
            #     raise Exception('All values have to be a list !')

        # for loop in range of len_checker why?
        # this information helps to understand have many tags was provided
        # len_checker -> how many blocks program needs to create?
        for num in range(len_checker):
            #print(num)
            # saveing html block to the array why?
            # self.html_list stores blocks as a list so every  block is a list with html elements
            array = []
            # running a loop to get a key order and add new html elements to the array
            for key in order_keys:
                #print(key)
                # getting index of the key why?
                # the order list looks this way -> [{h1:[]},{p:[]},{b:[]}]
                # key_list -> [h1,p,b]
                # to get the first headding we need to get dict {h1:[]}, 
                # after use a key, and the num to get value
                key_index = order_keys.index(key)
                current_value = order_list[key_index][key][num]
                # adding html element to the array
                array.append(CreateHtml.key_checker(key, current_value))
            # saveing html block to the html_list
            self.html_list.append(array)
        return

    def create_html(self):
        # this functions creates html from self.html_list blocks
        for line in self.html_list:
            for value in line:
                self.html += f'{value}\n'
        return self

    def use_template(self):
        with open(self.template_path) as html_template:
            template_content = html_template.read()
        self.template = template_content
        return self

    def replace_templates_content(self):
        # NB! Use this method after create_html
        # method replaces templates content with created_html
        self.template = self.template.replace('[CONTENT]', self.html)
        return self

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
