from nicegui import ui


def create_right_drawer() -> ui.right_drawer:
    with ui.right_drawer(fixed=False).style('background-color: #ebf1fa').props('bordered') as drawer:
        ui.label('Default right drawer content')
    drawer.hide()
    return drawer