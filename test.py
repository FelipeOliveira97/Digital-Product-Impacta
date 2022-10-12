# -*- coding: utf-8 -*-
from app import app
import unittest
import random

class Test(unittest.TestCase):
    def setUp(self):
        # cria uma instância do unittest, precisa do nome "setUp"
        self.app = app.test_client()

        x = random.randint(1,10)
        
        # envia uma requisicao GET para a URL
        self.result = self.app.get('/status/x')

    def test_requisicao(self):
        # compara o status da requisicao (precisa ser igual a 200)
        self.assertEqual(self.result.status_code, 200)
