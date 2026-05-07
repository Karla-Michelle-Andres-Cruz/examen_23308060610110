import flet as ft
from examen_23308060610110.src.controllers.userController import AuthController
from examen_23308060610110.src.controllers.tareaController import TareaController 
from examen_23308060610110.src.view.loginView import LoginView
from examen_23308060610110.src.view.registroView import RegistroView
from examen_23308060610110.src.view.dashboard import DashboardView

def start(page: ft.Page):
    auth_ctrl = AuthController()
    tarea_ctrl = TareaController()

    def route_change(e):
        print(f" route_change llamado: {page.route}")
        page.controls.clear()
        if page.route == "/":
            page.controls.append(LoginView(page, auth_ctrl))
        elif page.route == "/registro":
            page.controls.append(RegistroView(page, auth_ctrl))
        elif page.route == "/dashboard":
            page.controls.append(DashboardView(page, auth_ctrl, tarea_ctrl))
        page.update()

    page.on_route_change = route_change
    route_change(None)

def main():
    ft.app(target=start)