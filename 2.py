from jinja2 import Template

out = open('2.html', 'w', encoding='utf-8')

file = open('2.jinja', 'r', encoding='utf-8')
html = file.read()
file.close()

temp = Template(html)
d = {
     "title" : ["Мастер и Маргарита","Белая гвардия", "Война и мир", "Анна Каренина", "Игрок"],
     "author": ["Булгаков М.А.", "Булгаков М.А.", "Толстой Л.Н.", "Толстой Л.Н.","Достоевский Ф.М."],
     "price": [581.50, 600.00, 899.99, 450.10, 234.55]
}
temp.globals['list'] = list
temp.globals['len'] = len
result = temp.render(dict=d, n=5)

out.write(result)
out.close()

