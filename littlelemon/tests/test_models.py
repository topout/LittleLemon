from django.test import TestCase
from restaurant.models import menu

class MenuTestCase(TestCase):

    def test_menu_item(self):
        item = menu.objects.create(title='IceCream', price=80, inventory = 100)
        self.assertEqual(str(item), 'IceCream : 80')

    # display menu in admin
    