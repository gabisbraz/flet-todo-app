from flet import *

BG = "#041955"
FWG = "#97b4ff"
FG = "#3450a1"
PINK = "#eb06ff"


def main(page: Page):
    container = Container(
        width=500, height=500, bgcolor=BG, border_radius=35, content=Stack(controls=[ ])
    )
    page.add(container)


app(target=main, view=AppView.FLET_APP)
