# src/components/layout.py
import reflex as rx
from src.components.navbar import navbar
from src.components.sidebar import sidebar

def layout(content: rx.Component) -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.hstack(
            sidebar(),
            content,
            align="start",
            spacing="0",
        ),
    )
