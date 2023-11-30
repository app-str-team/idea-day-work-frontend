
from flet import *
from view import ChangeRoute

class ModernNavbar(UserControl):
    def __init__(self):
        
        super().__init__()

    def ContainedIcon(self, icon_name, text):
        return Container(
            width=190,
            height=45,
            border_radius=10,
            on_click= None,
            on_hover= None,
            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_size=18,
                        selected=False,
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=9),
                            },
                            overlay_color={"":"transparent"},
                        ),
                    ),
                    Text(
                        value=text,
                        size=11,
                        opacity=1,
                        animate_opacity=200,
                    ),
                ],
            ),
        )

    def build(self):
        return Container(
            alignment=alignment.center,
            padding=10,
            clip_behavior=ClipBehavior.HARD_EDGE,
            content=Column(
                expand=True,
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.START,
                spacing=5,
                controls=[
                    # self.ContainedIcon(icons.HOME_FILLED, "Home"),
                    # self.ContainedIcon(icons.DASHBOARD_ROUNDED, "Dashboard",),
                    Container(
                                on_click= lambda e: None,
                                    # ChangeRoute(e,"/home"),
                                content=Text(
                                    "HOME",
                                    color="orange900",
                                    size=10,
                                    weight="bold",
                                ),
                            ),
                    Container(
                         on_click= lambda e: ChangeRoute(e, "/postComments"),
                                content=Text(
                                    "DASHBOARD",
                                    color="orange900",
                                    size=10,
                                    weight="bold",
                                ),
                    ),
                               

                    Divider(color="whitw", height=7),
                    # self.ContainedIcon(icons.LOGOUT_ROUNDED, "Logout"),
                    Container(
                        on_click= lambda e: ChangeRoute(e, "/login"),
                        content=Text(
                                    "LOGOUT",
                                    color="orange900",
                                    size=10,
                                    weight="bold",
                        ),
                    ),
                ],
            ),
        )