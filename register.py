
from flet import *
from controls import inputText
from view import ChangeRoute, RegisterUser

def _view_():
    return View(
        "/register",
        bgcolor='#fafafa',
        horizontal_alignment=CrossAxisAlignment.CENTER,
        vertical_alignment=MainAxisAlignment.CENTER,
        controls=[
            Column(
                controls=[
                        Container(
                        width=350,
                        height=600,
                        border_radius=8,
                        bgcolor="#ffffff",
                        border=border.all(3,"#dbdbdb"),
                        alignment=alignment.center,
                        content=Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                Divider(height=20, color="transparent"),
                                Text(
                                    "Register Form",
                                    size=26,
                                    weight="w600",
                                    color="Black"
                                ),
                                Text(
                                    "Fill out the form below to create an account.",
                                    size=12,
                                    weight="w400",
                                    color="Black"
                                ),
                                Divider(height=40, color="transparent"),
                                Column(
                                    spacing=5,
                                    controls=[
                                        inputText.InputetextField("First Name", False),
                                        inputText.InputetextField("Last Name", False),
                                        inputText.InputetextField("Email", False),
                                        inputText.InputetextField("Password", True),
                                    ],
                                ),
                                Row(
                                    width=300,
                                    alignment=MainAxisAlignment.END,
                                    controls=[
                                        Text(
                                            "Forgot Password",
                                            color="black",
                                            weight="bold",
                                            size=10,
                                        ),
                                    ],
                                ),
                                Divider(height=5, color="transparent"),

                                inputText.SignInOption( "Sign uP", 
                                                       lambda e: RegisterUser(e)
                                                       ),
                                Divider(height=60, color="transparent"),
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    spacing=4,
                                    controls=[
                                        Text(
                                            "Have an account",
                                            color="black",
                                            size=10,
                                            weight='bold',
                                        ),
                                        Container(
                                            on_click= lambda e: ChangeRoute(e, "/login"),
                                            content=Text(
                                                "Log In",
                                                color="blue900",
                                                size=10,
                                                weight="bold",
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        ],
    )