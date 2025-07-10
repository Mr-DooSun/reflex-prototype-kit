import reflex as rx

from src.pages import home
from src.pages import setting

def create_app() -> rx.App:
    app = rx.App()
    app.add_page(home.home)
    app.add_page(setting.settings)

    return app


app = create_app()
