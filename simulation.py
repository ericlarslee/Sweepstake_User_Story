import user_interface
from marketing_firm import MarketingFirm



class Simulation:
    def __init__(self):
        self.run_simulation()

    def run_simulation(self):
        print('Welcome to the Sim.\n')
        name = input('What would you like the name of your marketing firm to be?')
        marketing_company = MarketingFirm(name)
        will_proceed = True
        if will_proceed:
            user_option = user_interface.simulation_main_menu()
            if user_option == 1:
                pass
            elif user_option == 2:
                pass
            elif user_option == 3:
                pass
            else:
                return False
