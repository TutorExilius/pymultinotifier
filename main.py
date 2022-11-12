import flet
from flet import Page, Text

from app_globals import PRODUCT_NAME, PRODUCT_VERSION


def main(page: Page):
    page.title = f"{PRODUCT_NAME} v{PRODUCT_VERSION}"
    page.horizontal_alignment = "center"
    page.update()

    page.add(Text(value="Hello World"))


flet.app(target=main, view=flet.FLET_APP)
