from jinja2 import Template

out = open('1.html', 'w', encoding='utf-8')

file = open('1.jinja', 'r', encoding='utf-8')
html = file.read()
file.close()

temp = Template(html)
temp.globals['enumerate'] = enumerate
result = temp.render(name='color', string='синий зелёный красный', numbers=[1, 2])

out.write(result)
out.close()
