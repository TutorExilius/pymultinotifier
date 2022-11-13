"""The main module. The flet app will be started here."""

import flet
from flet import Page, Text

from app_globals import PRODUCT_NAME, PRODUCT_VERSION


def main(page: Page) -> None:
    page.title = f"{PRODUCT_NAME} v{PRODUCT_VERSION}"
    page.horizontal_alignment = "center"
    page.update()

    page.add(Text("Hello World"))


flet.app(target=main, route_url_strategy="path", view=flet.FLET_APP)
