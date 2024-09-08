from flet import *

BG = "#041955"
FWG = "#97b4ff"
FG = "#3450a1"
PINK = "#eb06ff"


def main(page: Page):

    first_page_contents = Container(
        content=Column(
            controls=[
                Row(
                    alignment="spaceBetween",
                    controls=[
                        # Container(
                        #     on_click=lambda e: shrink(e), content=Icon(icons.MENU)
                        # ),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED),
                            ],
                        ),
                    ],
                ),
                Container(height=20),
                Text(value="What's up, Olivia!"),
                Text(value="CATEGORIES"),
                Container(
                    padding=padding.only(
                        top=10,
                        bottom=20,
                    ),
                    # content=categories_card,
                ),
                Container(height=20),
                Text("TODAY'S TASKS"),
                Stack(
                    controls=[
                        # tasks,
                        FloatingActionButton(
                            bottom=2,
                            right=20,
                            icon=icons.ADD,
                            on_click=lambda _: page.go("/create_task"),
                        ),
                    ]
                ),
            ],
        ),
    )
    page_2 = Row(
        alignment="end",
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor=FG,
                border_radius=35,
                animate=animation.Animation(600, AnimationCurve.DECELERATE),
                animate_scale=animation.Animation(400, curve="decelerate"),
                padding=padding.only(top=50, left=20, right=20, bottom=5),
                content=Column(controls=[first_page_contents]),
            )
        ],
    )
    container = Container(
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=35,
        content=Stack(
            controls=[
                # page_1,
                page_2,
            ]
        ),
    )
    # pages = {
    #     "/": View(
    #         "/",
    #         [container],
    #     ),
    #     "/create_task": View(
    #         "/create_task",
    #         [create_task_view],
    #     ),
    # }
    page.add(container)


app(target=main, view=AppView.FLET_APP)
