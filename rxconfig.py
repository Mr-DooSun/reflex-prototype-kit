import reflex as rx

config = rx.Config(
    app_name="Test",
    app_module_import="src.app",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)