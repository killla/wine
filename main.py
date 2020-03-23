'''
from http.server import HTTPServer, SimpleHTTPRequestHandler


server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
'''


from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

import datetime, pandas, collections

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

years_from_build_story = datetime.date.today().year - 1920

excel_data_df = pandas.read_excel('wine3.xlsx', sheet_name='Лист1')

wines = excel_data_df.to_dict(orient='record')

categories = list(collections.Counter(excel_data_df['Категория'].tolist()))


rendered_page = template.render(
    years_from_build_story=years_from_build_story,
    wines=wines,
    categories=categories,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()