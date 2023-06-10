from django.test import TestCase
from restaurant.models import menu
from django.core.serializers import serialize
import json

class MenuViewTest(TestCase):
    def setUp(self):
        menu.objects.create(title='IceCream', price=80, inventory = 50)
        menu.objects.create(title='Pizza', price=200, inventory = 70)
        menu.objects.create(title='Burger', price=100.59, inventory = 100)
    
    def test_get_all(self):
        queryset = menu.objects.all()
        serialized_data = serialize('json', queryset)
        print(queryset)
        
        # print('serialized_data: ', serialized_data)
        expected_data = [
            {"model": "restaurant.menu", "pk": 2, "fields": {"title": "IceCream", "price": "80.00", "inventory": 50}}, 
            {"model": "restaurant.menu", "pk": 3, "fields": {"title": "Pizza", "price": "200.00", "inventory": 70}}, 
            {"model": "restaurant.menu", "pk": 4, "fields": {"title": "Burger", "price": "100.59", "inventory": 100}}
        ]
        expected_data = json.dumps(expected_data)

        self.assertEqual(serialized_data, expected_data)

        # the following code did not work
        # for expected, actual in zip(expected_data, serialized_data):
        #     print('expected: ', expected['model'][0])
        #     print('actual: ', actual['model'])
        #     print('expected: ', expected['fields']['name'])
        #     print('actual: ', actual['fields']['name'])
        #     self.assertEqual(expected['model'], actual['model'])
        #     self.assertEqual(expected['fields']['name'], actual['fields']['name'])
        #     self.assertEqual(expected['fields']['price'], actual['fields']['price'])
        #     self.assertEqual(expected['fields']['inventory'], actual['fields']['inventory'])

