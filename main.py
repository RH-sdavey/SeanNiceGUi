import asyncio
from nicegui import ui

with ui.button(icon='menu'):
    with ui.menu():
        ui.menu_item('Option 1')
        ui.menu_item('Option 2')
        with ui.menu_item('Option 3', auto_close=False):
            with ui.item_section().props('side'):
                ui.icon('keyboard_arrow_right')
            with ui.menu().props('anchor="top end" self="top start" auto-close'):
                ui.menu_item('Sub-option 1')
                ui.menu_item('Sub-option 2')
                ui.menu_item('Sub-option 3')

async def compute():
    n = ui.notification(timeout=None)
    for i in range(10):
        n.message = f'Computing {i/10:.0%}'
        n.spinner = True
        await asyncio.sleep(0.2)
    n.message = 'Done!'
    n.spinner = False
    await asyncio.sleep(1)
    n.dismiss()

ui.button('Compute', on_click=compute)

with ui.dialog() as dialog, ui.card():
    ui.label('Are you sure?')
    with ui.row():
        ui.button('Yes', on_click=lambda: dialog.submit('Yes'))
        ui.button('No', on_click=lambda: dialog.submit('No'))

async def show():
    result = await dialog
    ui.notify(f'You chose {result}')

ui.button('Await a dialog', on_click=show)


with ui.card().tight():
    ui.image('https://picsum.photos/id/684/640/360')
with ui.card_section():
    ui.label('Lorem ipsum dolor sit amet, consectetur adipiscing elit, ...')

with ui.row():
    ui.label('Hello NiceGUI!')
    ui.button('BUTTON', on_click=lambda: ui.notify('button was pressed'))
    ui.chat_message('Hello NiceGUI!',
                    name='Robot',
                    stamp='now',
                    avatar='https://robohash.org/ui')

    with ui.chat_message():
        ui.label('Guess where I am!')
        ui.image('https://picsum.photos/id/249/640/360').classes('w-64')

        ui.mermaid('''
        graph LR;
            A --> B;
            A --> C;
            B --> C;
            C --> D;
            D --> A;
        ''')

    table = ui.table(
        columns=[{'name': 'name', 'label': 'Name', 'field': 'name'}],
        rows=[{'name': 'Alice'}, {'name': 'Bob'}, {'name': 'Carol'}],
    )

    with table.add_slot('top-left'):
        def toggle() -> None:
            table.toggle_fullscreen()
            button.props('icon=fullscreen_exit' if table.is_fullscreen else 'icon=fullscreen')
        button = ui.button('Toggle fullscreen', icon='fullscreen', on_click=toggle).props('flat')
    ui.highchart({
        'title': False,
        'chart': {'type': 'solidgauge'},
        'yAxis': {
            'min': 0,
            'max': 1,
        },
        'series': [
            {'data': [0.42]},
        ],
    }, extras=['solid-gauge']).classes('h-64')


    from random import random

    echart = ui.echart({
        'xAxis': {'type': 'value'},
        'yAxis': {'type': 'category', 'data': ['A', 'B'], 'inverse': True},
        'legend': {'textStyle': {'color': 'gray'}},
        'series': [
            {'type': 'bar', 'name': 'Alpha', 'data': [0.1, 0.2]},
            {'type': 'bar', 'name': 'Beta', 'data': [0.3, 0.4]},
        ],
    })

    def update():
        echart.options['series'][0]['data'][0] = random()
        echart.update()

    ui.button('Update', on_click=update)


    schema = {
        'type': 'object',
        'properties': {
            'id': {
                'type': 'integer',
            },
            'name': {
                'type': 'string',
            },
            'price': {
                'type': 'number',
                'exclusiveMinimum': 0,
            },
        },
        'required': ['id', 'name', 'price'],
    }
    data = {
        'id': '4e2',
        'name': 22,
        'price': 15,
    }
    ui.json_editor({'content': {'json': data}}, schema=schema)

with ui.stepper().props('vertical').classes('w-full') as stepper:
    with ui.step('Preheat'):
        ui.label('Preheat the oven to 350 degrees')
        with ui.stepper_navigation():
            ui.button('Next', on_click=stepper.next)
    with ui.step('Ingredients'):
        ui.label('Mix the ingredients')
        with ui.stepper_navigation():
            ui.button('Next', on_click=stepper.next)
            ui.button('Back', on_click=stepper.previous).props('flat')
    with ui.step('Bake'):
        ui.label('Bake for 20 minutes')
        with ui.stepper_navigation():
            ui.button('Done', on_click=lambda: ui.notify('Yay!', type='positive'))
            ui.button('Back', on_click=stepper.previous).props('flat')

with ui.timeline(side='left').classes('w-128'):
    ui.timeline_entry('Rodja and Falko start working on NiceGUI.',
                      title='Initial commit',
                      subtitle='May 07, 2021')
    ui.timeline_entry('The first PyPI package is released.',
                      title='Release of 0.1',
                      subtitle='May 14, 2021')
    ui.timeline_entry('Large parts are rewritten to remove JustPy '
                      'and to upgrade to Vue 3 and Quasar 2.',
                      title='Release of 1.0',
                      subtitle='December 15, 2022',
                      icon='rocket')

with ui.carousel(animated=True, arrows=True, navigation=True).props('height=180px'):
    with ui.carousel_slide().classes('p-0'):
        ui.image('https://picsum.photos/id/30/270/180').classes('w-[270px]')
    with ui.carousel_slide().classes('p-0'):
        ui.image('https://picsum.photos/id/31/270/180').classes('w-[270px]')
    with ui.carousel_slide().classes('p-0'):
        ui.image('https://picsum.photos/id/32/270/180').classes('w-[270px]')

ui.run()