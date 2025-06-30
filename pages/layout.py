from nicegui import ui

from pages.footer.footer import create_footer
from pages.left_drawer.drawer import create_left_drawer
from pages.main_content.content import create_main_content, user_details, group_details, application_details
from pages.right_drawer.drawer import create_right_drawer
from pages.header.header import create_header

from graph.client import client

@ui.page('/')
async def page_layout():

    async def update_content(option: str, endpoint: str):
        right_drawer.clear()
        right_drawer.show()

        match option:
            case 'Users':
                result = await client.graph.users.get()

                with main_container:
                    group_details.refresh(None)
                    application_details.refresh(None)

                with right_drawer:
                    ui.label(f'Users in Entra ID:').classes('text-lg font-bold')
                    ui.aggrid({
                        'columnDefs': [
                            {
                                'headerName': 'Name',
                                'field': 'name',
                                'filter': 'agTextColumnFilter',
                                'floatingFilter': True
                            },
                        ],
                        'rowData': [{
                            'id': user.id,
                            'name': user.display_name,
                            'email': user.user_principal_name
                        } for user in result.value]}
                    ).classes('max-h-full h-96').on('cellClicked', lambda event: user_details.refresh(event.args['data']['id']))

            case 'Groups':
                result = await client.graph.groups.get()
                with main_container:
                    user_details.refresh(None)
                    application_details.refresh(None)

                with right_drawer:
                    ui.aggrid({
                        'columnDefs': [
                            {
                                'headerName': 'Name',
                                'field': 'name',
                                'filter': 'agTextColumnFilter',
                                'floatingFilter': True
                            },
                        ],
                        'rowData': [{
                            'id': group.id,
                            'name': group.display_name,

                        } for group in result.value]}
                    ).classes('max-h-full h-96').on('cellClicked', lambda event: group_details.refresh(event.args['data']['id']))

            case 'Applications':
                result = await client.graph.applications.get()
                with main_container:
                    user_details.refresh(None)
                    group_details.refresh(None)

                with right_drawer:
                    ui.aggrid({
                        'columnDefs': [
                            {
                                'headerName': 'Name',
                                'field': 'name',
                                'filter': 'agTextColumnFilter',
                                'floatingFilter': True
                            },
                        ],
                        'rowData': [{
                            'id': application.id,
                            'name': application.display_name,

                        } for application in result.value]}
                    ).classes('max-h-full h-96').on('cellClicked', lambda event: application_details.refresh(event.args['data']['id']))


    main_container = await create_main_content()
    left_drawer = create_left_drawer(on_select=update_content)
    right_drawer = create_right_drawer()
    create_header(left_drawer)
    create_footer()

