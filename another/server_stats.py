import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def read_servers_from_file(file_path):
    servers = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():
                    server_url, api_key = line.strip().split('-')
                    servers.append((server_url, api_key))
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {str(e)}")
    return servers

def check_server_availability(api_url):
    try:
        response = requests.get(api_url, verify=False)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(f"Произошла ошибка при проверке доступности сервера {api_url}: {str(e)}")
        return False

def check_api_key(api_url, api_key):
    test_url = f"{api_url}/api/v1/target_groups"
    headers = {
        "X-Auth": api_key,
        "Accept": "application/json"
    }
    try:
        response = requests.get(test_url, headers=headers, verify=False)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(f"Произошла ошибка при проверке API ключа на сервере {api_url}: {str(e)}")
        return False

def get_target_groups(api_url, api_key):
    groups_url = f"{api_url}/api/v1/target_groups"
    headers = {
        "X-Auth": api_key,
        "Accept": "application/json"
    }
    try:
        response = requests.get(groups_url, headers=headers, verify=False)
        if response.status_code == 200:
            data = response.json()
            return data.get('groups', [])
        else:
            print(f"Не удалось получить группы целей с сервера {api_url}. Код состояния: {response.status_code}")
            return []
    except Exception as e:
        print(f"Произошла ошибка при получении групп целей с сервера {api_url}: {str(e)}")
        return []

def main():
    servers = read_servers_from_file('servers.txt')
    
    total_servers = len(servers)
    available_servers = 0

    for server_url, api_key in servers:
        if check_server_availability(server_url):
            print(f"Сервер {server_url} доступен.")
            if check_api_key(server_url, api_key):
                available_servers += 1
                groups = get_target_groups(server_url, api_key)
                total_groups = len(groups)
                total_targets = sum(group['target_count'] for group in groups)
                print(f"Сервер {server_url} доступен. API ключ корректен. Групп: {total_groups}, целей: {total_targets}")
            else:
                print(f"Сервер {server_url} доступен. API ключ некорректен.")
        else:
            print(f"Сервер {server_url} недоступен.")

    print(f"Статистика: доступно {available_servers} серверов из {total_servers}.")

if __name__ == "__main__":
    main()

