#!/usr/bin/python3
"""module for base"""
import json
import os
import csv
import os
import turtle


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """function to save a csv file
        args:
            list_obj:list of objects"""
        filename = cls.__name__ + '.csv'
        with open(filename, 'w', newline='') as file:
            if list_objs is None or list_objs == []:
                file.write('[]')
            else:
                if cls.__name__ = 'Rectangle':
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                csvw = csv.DictWriter(file, fieldnames=fieldnames)
                for line in list_objs:
                    csvw.writerow(line.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """function to load csv file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                listdicts = csv.DictReader(file, fieldnames=fieldnames)
                listdicts = [dict([i, int(j)] for i, j in k.items())
                             for k in listdicts]
                return [cls.create(**k) for k in listdicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """rec and square using turtle
        args:
            list_rectangle:list rect objects
            list_square:sq list objects
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rec in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rec.x, rec.y)
            turt.down()
            for _ in range(2):
                turt.forward(rec.width)
                turt.left(90)
                turt.forward(rec.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for _ in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
