import reflex as rx

from src.states.router_state import RouterState

from src.components.layout import layout
from src.components.chat import chat_main


@rx.page(route="/", title="Home")
def home() -> rx.Component:
    RouterState.current_path = "/"
    return layout(
        content= rx.hstack(
            chat_main(),
            align="start",
            spacing="0",
        ),
    )