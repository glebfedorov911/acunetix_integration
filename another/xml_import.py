import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import os
import re

# Функция для извлечения даты сканирования из XML файла
def extract_scan_date(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    start_time_text = root.findtext('.//StartTime')
    start_time = datetime.fromisoformat(start_time_text)
    scan_date = start_time.strftime('%Y-%m-%d')
    return scan_date

# Функция для извлечения URL из XML файла
def extract_url(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    start_url = root.findtext('.//StartURL')
    return start_url

# Функция для проверки, является ли строка IP-адресом
def is_ip_address(string):
    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return ip_pattern.match(string) is not None

# Функция для поиска продукта по URL
def find_product(url, headers):
    if is_ip_address(url):
        print(f"Ищем продукт по IP-адресу: {url}")  # Логирование
        response = requests.get(f'http://10.130.132.251:8080/api/v2/products/?name_exact={url}', headers=headers)
        if response.status_code == 200:
            product_data = response.json()
            if product_data['results']:
                return product_data['results'][0]
    else:
        parts = url.split('.')
        while len(parts) > 1:
            domain = '.'.join(parts)
            print(f"Ищем продукт по домену: {domain}")  # Логирование
            response = requests.get(f'http://10.130.132.251:8080/api/v2/products/?name_exact={domain}', headers=headers)
            if response.status_code == 200:
                product_data = response.json()
                if product_data['results']:
                    print(f"Найден продукт: {product_data['results'][0]['name']}")  # Логирование
                    return product_data['results'][0]
            parts.pop(0)  # Удаляем первый префикс и проверяем снова
    
    return None

# Параметры
api_token = 'fff7cb849295eab657a6cbdb5a439c39137f2707'
headers = {'Authorization': f'Token {api_token}'}
directory = '.'  # текущая директория

# Получение списка XML файлов в директории
xml_files = [f for f in os.listdir(directory) if f.endswith('.xml')]

# Обработка каждого XML файла
for idx, xml_file in enumerate(xml_files, start=1):
    try:
        # Извлечение данных из XML
        scan_date = extract_scan_date(xml_file)
        product_url = extract_url(xml_file)

        # Поиск продукта по доменному имени или IP-адресу
        product_data = find_product(product_url, headers)

        if not product_data:
            raise ValueError(f'Product with URL {product_url} not found')

        product_name = product_data['name']
        product_type_id = product_data['prod_type']

        # Поиск типа продукта
        response = requests.get(f'http://10.130.132.251:8080/api/v2/product_types/?id={product_type_id}', headers=headers)
        product_type_data = response.json()

        if not product_type_data['results']:
            raise ValueError(f'Product type with ID {product_type_id} not found')

        product_type_name = product_type_data['results'][0]['name']

        # Формирование значения для engagement_name
        engagement_name = f'indepo_scan_{scan_date}'

        # Формирование и выполнение запроса на импорт сканирования
        import_url = 'http://10.130.132.251:8080/api/v2/import-scan/'
        files = {'file': (xml_file, open(xml_file, 'rb'), 'text/xml')}
        data = {
            'product_type_name': product_type_name,
            'active': 'true',
            'verified': 'false',
            'close_old_findings': 'false',
            'deduplication_on_engagement': 'true',
            'push_to_jira': 'false',
            'minimum_severity': 'Info',
            'close_old_findings_product_scope': 'false',
            'apply_tags_to_endpoints': 'true',
            'scan_date': scan_date,
            'create_finding_groups_for_all_findings': 'true',
            'group_by': 'component_name',
            'apply_tags_to_findings': 'true',
            'product_name': product_name,
            'auto_create_context': 'true',
            'scan_type': 'Indepo Scan',
            'engagement_name': engagement_name
        }

        response = requests.post(import_url, headers=headers, files=files, data=data)

        if response.status_code == 201:
            print(f'Scan {xml_file} imported successfully ({idx}/{len(xml_files)})')
        else:
            print(f'Failed to import scan {xml_file}: {response.status_code}, {response.text} ({idx}/{len(xml_files)})')

    except Exception as e:
        print(f'Error processing file {xml_file}: {e} ({idx}/{len(xml_files)})')
