from nicegui import ui

def create_header(left_drawer: ui.element) -> ui.element:
    with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between') as header:
        ui.button(on_click=left_drawer.toggle, icon='menu').props('flat color=white')

    return header

