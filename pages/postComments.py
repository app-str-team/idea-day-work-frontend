from threading import activeCount
from flet import *
from controls import inputTextField
from view import PostJudgeScore,homePage, goToPreviousPage

from common import usersession
from controls import IdeaDayTeam

def _view_(page : Page):
    return View(
        "/postComments",
        bgcolor='#fafafa',
        horizontal_alignment=CrossAxisAlignment.CENTER,
        vertical_alignment=MainAxisAlignment.CENTER,
        controls=[
            Column(
                controls=[
                        Container(
                        width=350,
                        height=650,
                        border_radius=8,
                        bgcolor="#ffffff",
                        border=border.all(3,"#dbdbdb"),
                        alignment=alignment.center,
                        content=Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                Divider(height=15, color="transparent"),
                                Text(
                                    "JUDGEMENT FORM",
                                    size=21,
                                    weight="w600",
                                    color="Black"
                                ),
                                Text(
                                    "Fill out the form below to give the Score and comments for Idea's",
                                    size=12,
                                    weight="w500",
                                    color="Black",
                                    text_align="center"
                                    
                                ),
                                Divider(height=11, color="transparent"),
                                Column(
                                    spacing=5,
                                    controls= [inputTextField.InputtextField(x,"Enter the Score between 1-10") for x in usersession.SESSION['active_session']['fieldsforjudgement']] +
                                              [inputTextField.MultitextField("Comment","Enter Your comment here")]
                                ),

                                # Divider(height=5, color="transparent"),

                                inputTextField.SignInOption( "POST JUDGEMENT", lambda e: PostJudgeScore(e)),
                                Divider(height=5, color="transparent"),
                                inputTextField.SignInOption( "BACK", lambda e: goToPreviousPage(e)),
                                Divider(height=5, color="transparent"),
                            ],
                        ),
                    ),
                ],
            ),
        ],
    )
