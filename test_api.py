import unittest
import requests
import os
from dotenv import load_dotenv

load_dotenv()


# Получение переменных окружения
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')

# Заголовки для авторизации
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

class TestGitHubAPI(unittest.TestCase):

    def setUp(self):
        self.api_url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}'

    # def test_create_repository(self):
    #     # create
    #     create_repo_url = f'https://api.github.com/user/repos'
    #     payload = {
    #         'name': REPO_NAME,
    #         'private': False
    #     }
    #     response = requests.post(create_repo_url, json=payload, headers=HEADERS)
    #     self.assertEqual(response.status_code, 201, 'Не удалось создать репозиторий')

    def test_check_repository_exists(self):
        response = requests.get(self.api_url, headers=HEADERS)
        self.assertEqual(response.status_code, 200, 'Репозиторий не найден')

    def test_delete_repository(self):
        response = requests.delete(self.api_url, headers=HEADERS)
        self.assertEqual(response.status_code, 204, 'Не удалось удалить репозиторий')

    def tearDown(self):
        # Удаляем репозиторий, если он существует
        requests.delete(self.api_url, headers=HEADERS)

if __name__ == '__main__':
    unittest.main()
