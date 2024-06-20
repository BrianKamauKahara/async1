import yaml
from pydantic_core import to_jsonable_python



with open('my_books.yaml','r') as file:
    my_books = yaml.safe_load(file)
    print(yaml.dump(my_books['my_books'][0]))
    # print(yaml.dumps(to_jsonable_python(my_books['my_books'])))
    """ Traceback (most recent call last):
            File "C:\Users\user\Desktop\ProjectsOlearning\async\async1\myyaml.py", line 9, in <module>
                print(yaml.dumps(to_jsonable_python(my_books['my_books'])))
                    ^^^^^^^^^^
        AttributeError: module 'yaml' has no attribute 'dumps'. Did you mean: 'dump'? """