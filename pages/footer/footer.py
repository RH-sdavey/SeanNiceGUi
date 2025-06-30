from nicegui import ui

def create_footer() -> ui.element:
    with ui.footer().style('background-color: #3874c8') as footer:
        ui.label('Sean Davey - NiceGUI Entra ID Sample App').classes('text-white text-center w-full p-2')

    return footer
