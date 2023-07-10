from django.urls import reverse
from simple_menu import Menu, MenuItem

Menu.add_item(
    'breakfast',
    MenuItem(
        "Eggs",
        "/",
        children=[MenuItem("Scrambled", "/"), MenuItem("Fried", "/")],
    ),
)
Menu.add_item('breakfast', MenuItem("Cereal", "/"))
Menu.add_item('breakfast', MenuItem("Waffles", "/"))

Menu.add_item(
    'navbar',
    MenuItem(
        "Profile",
        "/",
        children=[
            MenuItem("Logout", reverse('logout')),
        ],
    ),
)
