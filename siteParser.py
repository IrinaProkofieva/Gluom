import requests
from bs4 import BeautifulSoup

with open('products.txt', 'w', encoding='UTF-8') as output_file:
    for page in range(0, 89):
        url = 'https://calorizator.ru/product/all/?page=%d' % (page)  # url страницы
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.find('table', {'class': 'views-table'})
        for row in table.tbody.find_all('tr'):
            product = row.find('td', {'class': 'views-field-title'}).a.text
            protein = row.find('td', {'class': 'views-field-field-protein-value'}).text
            fat = row.find('td', {'class': 'views-field-field-fat-value'}).text
            carbohydrate = row.find('td', {'class': 'views-field-field-carbohydrate-value'}).text
            kcal = row.find('td', {'class': 'views-field-field-kcal-value'}).text
            output_file.write("{},{},{},{},{}\n".format(product.strip(),
                                                   protein.strip(), fat.strip(), carbohydrate.strip(), kcal.strip()))
