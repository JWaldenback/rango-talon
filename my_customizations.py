from talon import Module, actions, Context

ctx = Context()
ctx.matches = r"""
tag: browser
"""

@ctx.action_class("user")
class UserActions:
    #Defining mouse scroll actions here enables for the usage of the exact same voice commands in knausj_talons mouse.py but Rango has precedence when a browser is in focus
    #"""
    def mouse_scroll_up(amount: float = 0.9):
        actions.user.rango_command_without_target("scrollUpPage", amount)

    def mouse_scroll_down(amount: float = 0.9):
        actions.user.rango_command_without_target("scrollDownPage", amount)
    #"""