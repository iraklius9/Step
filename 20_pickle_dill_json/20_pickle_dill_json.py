import json
import pickle
import dill


def save_object(obj):
    try:
        with open('object.json', 'w') as file:
            json.dump(obj, file)
    except:
        print('ვერ შეინახა json-ში')
        try:
            with open('object.pickle', 'wb') as file:
                pickle.dump(obj, file)
        except:
            print('ობიექტის სერიალიზაცია ვერ მოხერხდა')


def load_object(file_name):
    try:
        with open(file_name, 'r') as file:
            obj = json.load(file)
            print(obj)
    except:
        print('ვერ გაიტანა json-იდან')
        try:
            with open(file_name, 'rb') as file:
                obj = pickle.load(file)
                print(obj)
        except:
            print('ობიექტის დესერიალიზაცია ვერ მოხერხდა')


def save_object_dill(obj):
    try:
        with open('object.dill', 'wb') as file:
            dill.dump(obj, file)
    except:
        print('ობიექტის სერიალიზაცია dill-ით ვერ მოხერხდა')


def load_object_dill(file_name):
    try:
        with open(file_name, 'rb') as file:
            obj = dill.load(file)
            print(obj)
    except:
        print('ობიექტის დესერიალიზაცია dill-ით ვერ მოხერხდა')


json_obj = {
    'name': 'გიორგი',
    'age': 25,
    'city': 'თბილისი'
}

save_object(json_obj)
load_object('object.json')

complex_obj = {
    'name': 'გიორგი',
    'age': 25,
    'city': 'თბილისი',
    'hobbies': {'reading', 'traveling'},
    'birthdate': lambda: "01-01-1999"
}

print('\n')
save_object(complex_obj)
load_object('object.pickle')


class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, city={self.city})"


custom_obj = Person(name='გიორგი', age=25, city='თბილისი')

print('\n')
save_object_dill(custom_obj)
load_object_dill('object.dill')
