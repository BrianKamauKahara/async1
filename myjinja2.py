import jinja2
import yaml

env = jinja2.Environment()
template = env.from_string("""
My favorite fruits are:
{% for fruit in fruits -%}
 {{ fruit }}
{% endfor %}
""")
print(template.render(fruits=["apples", "oranges","Guavas"]))

env2 = jinja2.Environment()
template2 = env2.from_string("""
{% for book in my_books -%}
 Author: {{ book['author'] }}
{% endfor %}
""")

with open("my_books.yaml",'r') as file:
    data = yaml.safe_load(file)
    print(template2.render(my_books=data['my_books']))
