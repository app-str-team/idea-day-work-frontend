import flet
from flet import *
from controls import IdeaDayCategory
from controls import IdeaDayTeam
#from controls import getDataFromFirebase
import requests
import json


class IdeaDayApp(UserControl):
    def build(self):
        listCUSTOMERDELIGHT = []
        listTECHBIZCATEGORY = []
        listPRODUCTINNOVATION = []
        listPROCESSINNOVATION = []
        ideaSingle = []
        str_ideaList = requests.get('http://127.0.0.1:5000/idealist')
        indextechbiz = 0
        indexvisionary_champs = 0
        indexefficiency_champs = 0
        indexcustomer_delight = 0
        for ideaItem in str_ideaList.json():
            if(ideaItem["category"] == "techbiz"): #techbiz_category
                ideaSingle = []
                ideaSingle.append(ideaItem["ImageUrl"] + str(ideaItem["ID"]))
                ideaSingle.append(ideaItem["TeamName"])
                #ideaSingle.append(str(ideaItem["ID"]))
                ideaSingle.append(indextechbiz)
                ideaSingle.append(ideaItem["TeamMember"])
                ideaSingle.append(ideaItem["Summary"])
                ideaSingle.append(ideaItem["category"])
                listTECHBIZCATEGORY.append(ideaSingle) #str(ideaItem["Id"]))
                indextechbiz = indextechbiz + 1
            if (ideaItem["category"] == "visionary_champs"): #Product Innovation
                ideaSingle = []
                ideaSingle.append(ideaItem["ImageUrl"] + str(ideaItem["ID"]))
                ideaSingle.append(ideaItem["TeamName"])
                #ideaSingle.append(str(ideaItem["ID"]))
                ideaSingle.append(indexvisionary_champs)
                ideaSingle.append(ideaItem["TeamMember"])
                ideaSingle.append(ideaItem["Summary"])
                ideaSingle.append(ideaItem["category"])
                listPRODUCTINNOVATION.append(ideaSingle) #str(ideaItem["Id"]))
                indexvisionary_champs = indexvisionary_champs + 1
            if (ideaItem["category"] == "efficiency_champs"): #process_innovation
                ideaSingle = []
                ideaSingle.append(ideaItem["ImageUrl"] + str(ideaItem["ID"]))
                ideaSingle.append(ideaItem["TeamName"])
                #ideaSingle.append(str(ideaItem["ID"]))
                ideaSingle.append(indexefficiency_champs)
                ideaSingle.append(ideaItem["TeamMember"])
                ideaSingle.append(ideaItem["Summary"])
                ideaSingle.append(ideaItem["category"])
                listPROCESSINNOVATION.append(ideaSingle) #str(ideaItem["Id"]))
                indexefficiency_champs = indexefficiency_champs + 1
            if (ideaItem["category"] == "customer_delight"): #customer_delight
                ideaSingle = []
                ideaSingle.append(ideaItem["ImageUrl"] + str(ideaItem["Id"]))
                ideaSingle.append(ideaItem["TeamName"])
                #ideaSingle.append(str(ideaItem["Id"]))
                ideaSingle.append(indexcustomer_delight)
                ideaSingle.append(ideaItem["TeamMember"])
                ideaSingle.append(ideaItem["Summery"])
                ideaSingle.append(ideaItem["category"])
                listCUSTOMERDELIGHT.append(ideaSingle) #str(ideaItem["Id"]))
                indexcustomer_delight = indexcustomer_delight + 1




        #taskPRODUCTINNOVATION = self.IdeaDayTeam("PRODUCTINNOVATION")
        taskTECHBIZCATEGORY = IdeaDayCategory.IdeaDayCategory("TECHBIZ CATEGORY",listTECHBIZCATEGORY)
        taskPRODUCTINNOVATION = IdeaDayCategory.IdeaDayCategory("PRODUCT INNOVATION",listPRODUCTINNOVATION)
        taskPROCESSINNOVATION = IdeaDayCategory.IdeaDayCategory("PROCESS INNOVATION",listPROCESSINNOVATION)
        taskCUSTOMERDELIGHT = IdeaDayCategory.IdeaDayCategory("CUSTOMER DELIGHT",listCUSTOMERDELIGHT)

        #response = requests.get("https://api.open-notify.org/this-api-doesnt-exist")

        self.tasks = Column(
            controls= [taskPRODUCTINNOVATION , taskPROCESSINNOVATION , taskTECHBIZCATEGORY , taskCUSTOMERDELIGHT],
        )

        def on_backarrow_clicked(e):
            step = e.page.controls[0].controls[0].controls[0]
            step.controls[0].visible = True
            step.controls[1].visible = True
            step.controls[2].visible = False

            step.update()

        self.selected_Idea = Column() #IdeaDayTeam.IdeaDayTeam("")
        # self.selected_Idea = Column( controls=[
        #         Container(
        #         content=IconButton(
        #             icon= icons.ARROW_BACK,
        #             icon_color="BLUE_50",
        #             icon_size=20,
        #             tooltip="Back Home",
        #             on_click=on_backarrow_clicked
        #         ),
        #         bgcolor=colors.YELLOW,
        #         padding=5,
        #     )],
        #     visible=False
        # )

        self.tasks.controls[0].visible = True

        self.filter = Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[Tab(text="PRODUCT INNOVATION"), Tab(text="PROCESS INNOVATION"), Tab(text="TECHBIZ CATEGORY"), Tab(text="CUSTOMER DELIGHT")],
        )

        # application's root control (i.e. "view") containing all other controls
        return Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment= CrossAxisAlignment.CENTER,
            width=400,
            auto_scroll=True,
            controls=[
                Column(
                    spacing=25,
                    controls=[
                        self.filter,
                        self.tasks,
                        self.selected_Idea
                    ],
                ),
            ],
        )

    def add_clicked(self, e):
        self.update()

    def task_status_change(self, task):
        self.update()

    def task_delete(self, task):
        self.update()

    def update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        for task in self.tasks.controls:
            task.visible = False
            if(status == task.task_name) :
                task.visible = True
        super().update()

    def tabs_changed(self, e):
        self.update()