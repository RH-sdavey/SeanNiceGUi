from nicegui import ui
from typing import Callable

option_endpoints = {
    'Users': '/entra/users',
    'Groups': '/entra/groups',
    'Applications': '/entra/applications',
}

def create_left_drawer(on_select: Callable[[str, str], None]) -> ui.element:
    with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #d7e3f4') as drawer:
        with ui.expansion('Entra ID', icon='list').classes('w-full'):
            for option, endpoint in option_endpoints.items():
                ui.button(option, on_click=lambda opt=option, end=endpoint: on_select(opt, end)).classes('w-full')
    drawer.hide()
    return drawer
