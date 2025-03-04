import requests
import urllib3
import time
import os

# Отключение предупреждений SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_KEY = '1986ad8c0a5b3df4d7028d5f3c06e936c3b7bd3b78bb54ef099066777f405c0d5'
BASE_URL = 'https://192.168.2.1:3443/api/v1'

headers = {
    'X-Auth': API_KEY,
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

def get_all_groups():
    url = f'{BASE_URL}/target_groups'
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        return response.json().get('groups', [])
    else:
        print(f'Ошибка при получении групп: {response.status_code}')
        return []

def get_scans_by_group_id(group_id):
    scans_url = f"{BASE_URL}/scans?q=group_id:{group_id}"
    response = requests.get(scans_url, headers=headers, verify=False)
    if response.status_code == 200:
        return response.json().get('scans', [])
    else:
        print(f'Ошибка при получении сканов для группы {group_id}: {response.status_code}')
        return []

def export_scans(scans, export_dir):
    create_export_url = f'{BASE_URL}/exports'
    for scan in scans:
        scan_id = scan['scan_id']
        target_id = scan['target_id']
        print(f"Запрос на экспорт для скана {scan_id} и цели {target_id}")

        payload = {
            "export_id": "21111111-1111-1111-1111-111111111111",
            "source": {
                "list_type": "scans",
                "id_list": [scan_id]
            }
        }

        response = requests.post(create_export_url, json=payload, headers=headers, verify=False)
        if response.status_code == 201:
            data = response.json()
            report_id = data['report_id']
            print(f"Запрос на экспорт для скана {scan_id} успешно создан. Report ID: {report_id}")

            status_url = f'{BASE_URL}/exports/{report_id}'

            while True:
                status_response = requests.get(status_url, headers=headers, verify=False)
                if status_response.status_code == 200:
                    status_data = status_response.json()
                    print(f"Текущий статус экспорта для скана {scan_id}: {status_data['status']}")
                    if status_data['status'] == 'completed':
                        download_path = status_data['download'][0]
                        download_link = f"https://192.168.2.1:3443{download_path}"  # Удаление дублирования /api/v1
                        print(f"Экспорт для скана {scan_id} завершен. Ссылка на скачивание: {download_link}")

                        download_response = requests.get(download_link, headers=headers, verify=False)
                        if download_response.status_code == 200:
                            filename = f'{export_dir}/exported_report_{scan_id}.xml'
                            with open(filename, 'wb') as file:
                                file.write(download_response.content)
                            print(f"Отчет для скана {scan_id} успешно загружен и сохранен как '{filename}'.")
                        else:
                            print(f"Ошибка при загрузке отчета для скана {scan_id}: {download_response.status_code}")
                        break
                    elif status_data['status'] == 'failed':
                        print(f"Экспорт для скана {scan_id} не удался.")
                        break
                else:
                    print(f"Ошибка при получении статуса экспорта для скана {scan_id}: {status_response.status_code}")
                    break
                time.sleep(1)  # Ожидание перед следующей проверкой
        else:
            print(f"Ошибка при выполнении запроса на создание экспорта для скана {scan_id}: {response.status_code}")
            print("Текст ответа:", response.text)

def main():
    groups = get_all_groups()
    for group in groups:
        group_name = group['name']
        group_id = group['group_id']
        print(f'Найдена группа "{group_name}" с ID: {group_id}')
        export_dir = f"export_{group_name.replace(' ', '_')}"
        if not os.path.exists(export_dir):
            os.makedirs(export_dir)
        scans = get_scans_by_group_id(group_id)
        print(f"Найдено сканов для группы {group_name}: {len(scans)}")
        for scan in scans:
            print(f"ID скана: {scan['scan_id']}, ID цели: {scan['target_id']}")
        export_scans(scans, export_dir)

if __name__ == "__main__":
    main()

