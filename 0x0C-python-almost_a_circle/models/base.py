#!/usr/bin/python3
"""module for base"""
import json
import os


class Base:
    """class with a private instance"""
    __nb_objects = 0

    def __init__(self, id=None):
        """function for id"""
        self.id = id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to change python to json"""
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """to save json to a file"""
        name = cls.__name__ + '.json'
        with open(name, 'w', encoding='utf-8') as file:
            if list_objs is None:
                file.write('[]')
            else:
                list_dc = []
                for p in list_objs:
                    sq_rt = p.to_dictionary()
                    list_dc.append(sq_rt)
                file.write(Base.to_json_string(list_dc))

    @staticmethod
    def from_json_string(json_string):
        """to change json to python"""
        json_list = []
        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json must have a json string")
            json_list = json.loads(json_string)
        return json_list

    @classmethod
    def create(cls, **dictionary):
        """ that returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(2, 3)
        if cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """that returns a list of instances:"""
        name = cls.__name__ + '.json'
        list_dict = []
        list_ins = []
        if os.path.exists(name):
            with open(name, 'r', encoding='utf-8') as file:
                rfile = file.read()
                list_dict = cls.from_json_string(rfile)
                for dictionary in list_dict:
                    list_ins.append(cls.create(**dictionary))
        return list_ins
