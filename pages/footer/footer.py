from nicegui import ui

def create_footer() -> ui.element:
    with ui.footer().style('background-color: #3874c8') as footer:
        ui.label('FOOTER')

    return footer
