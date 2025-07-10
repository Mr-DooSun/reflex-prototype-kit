import reflex as rx
from src.states.router_state import RouterState

def nav_link(label: str, href: str) -> rx.Component:
    return rx.link(
        rx.text(
            label,
            color=rx.cond(RouterState.current_path == href, "black", "gray"),
            font_weight=rx.cond(RouterState.current_path == href, "bold", "normal"),
            border_bottom=rx.cond(RouterState.current_path == href, "2px solid black", "none"),
            padding_y="0.5rem",
        ),
        href=href,
        padding_x="1rem",
    )


def navbar() -> rx.Component:
    return rx.hstack(
        nav_link("Home", "/"),
        nav_link("Settings", "/settings"),
        rx.spacer(),
        rx.color_mode.button(),
        width="100%",
        height="60px",
        padding_x="2rem",
        border_bottom="1px solid #e0e0e0",
        position="sticky",
        top="0",
        bg={"light": "white", "dark": "gray.900"},
        color={"light": "black", "dark": "white"},
        z_index="1000",
        align_items="center",
    )