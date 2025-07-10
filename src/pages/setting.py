import reflex as rx
from src.components.sidebar import sidebar
from src.states.router_state import RouterState

from src.components.layout import layout

@rx.page(route="/settings", title="Settings")
def settings() -> rx.Component:
    RouterState.current_path = "/settings"
    return layout(
        content= rx.hstack(
            align="start",
            spacing="0",
        ),
    )