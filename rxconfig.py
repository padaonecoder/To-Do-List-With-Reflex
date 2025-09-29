import reflex as rx

config = rx.Config(
    app_name="to_do_list",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)