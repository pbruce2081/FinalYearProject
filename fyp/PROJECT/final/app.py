import tkinter as tk
from bosAlgorithm import BattleOfTheSexes
from prisonersDilemma import PrisonersDilemma
from polymatrixGame import PolymatrixGame
from subprocess import Popen, PIPE

class App(tk.Frame):
    def __init__(self, window):
        self.window = window

    def create_buttons(self):
        closeButton = tk.Button(
            root,
            text="Exit",
            font=("Times New Roman", 18),
            bg="#D87DB5",
            fg="Black",
            activebackground="#D87DB5",
            command=root.destroy)
        closeButton.grid(row=1, column=0, padx=1, pady=1)

        bosButton = tk.Button(
            root,
            text="Battle of the Sexes",
            font=("Times New Roman", 18),
            bg="#D87DB5",
            fg="Black",
            activebackground="#D87DB5",
            command=App.open_bosPage)
        bosButton.grid(row=1, column=1, padx=1, pady=1)

        pdButton = tk.Button(
            root,
            text="Prisoner's Dilemma",
            font=("Times New Roman", 18),
            bg="#D87DB5",
            fg="Black",
            activeforeground="#D87DB5",
            command=App.open_pdpage)
        pdButton.grid(row=1, column=2, padx=1, pady=1)

        pmButton = tk.Button(
            root,
            text="Polymatrix Games",
            font=("Times New Roman", 18),
            bg="#D87DB5",
            fg="Black",
            activebackground="#D87DB5",
            command=App.open_pmpage)
        pmButton.grid(row=1, column=3, padx=1, pady=1)

        aboutButton = tk.Button(
            root,
            text="About the Project",
            font=("Times New Roman", 18),
            bg="#D87DB5",
            fg="Black",
            activeforeground="#D87DB5",
            command=App.open_aboutPage)
        aboutButton.grid(row=1, column=4, padx=1, pady=1)

        root.pack_propagate(False)

        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure(2, weight=1)
        root.grid_columnconfigure(3, weight=1)
        root.grid_columnconfigure(4, weight=1)

    def homepage(self):
        self.htitle = tk.Label(
            root,
            text="Algorithms for Solving Industrial Strike Action",
            fg="white",
            bg="#BB458D",
            font=("Times New Roman", 35),
            width=150,
            height=2)
        self.htitle.grid(row=0, column=0, columnspan=5, sticky="new")
        self.welcomeMsg = tk.Label(
            root,
            text="Welcome to my Final Year Project",
            bg="lightgray")
        self.welcomeMsg.config(font=("Times New Roman", 45))
        self.welcomeMsg.grid(row=2, column=0, columnspan=5, pady=(50,10))
        self.welcomeTxt = tk.Label(
            root,
            text="Please select from the above for a solution to the industrial strike action\ncurrently happening in the UK.",
            bg="lightgray")
        self.welcomeTxt.config(font=("Times New Roman", 25))
        self.welcomeTxt.grid(row=3, column=0, columnspan=5, pady=(0,50))

    def open_bosPage():
        bosWindow = tk.Toplevel(root)
        bosWindow.title("Battle of the Sexes")
        bosWindow.geometry("875x800")
        bosWindow.configure(bg="lightgray")
        btitle = tk.Label(
            bosWindow,
            text="Battle of the Sexes",
            fg="white",
            bg="#BB458D",
            font=("Times New Roman", 35),
            width=150,
            height=2)
        btitle.grid(row=0, column=0, columnspan=5, sticky="new")

        closeButton = tk.Button(
            bosWindow,
            text="Exit",
            font=("Times New Roman", 18),
            bg="#D87DB5",
            fg="Black",
            activebackground="#D87DB5",
            command=bosWindow.destroy)
        closeButton.grid(row=1, column=0, padx=1, pady=1,sticky="nw")
        
        bosDesc = tk.Label(
            bosWindow,
            text="A man and a woman want to get together for an evening of entertainment, but they have no means of communication. \nThey can either go to the ballet or the fight. The man would prefer to go to the fight, \nwhereas the woman would prefer to go to the ballet; however, both would prefer to be together rather than alone.",
            bg="lightgray")
        bosDesc.config(font=("Times New Roman", 18))
        bosDesc.grid(row=2, column=0, columnspan=5, pady=(50,10))

        inputLabelP1 = tk.Label(
            bosWindow,
            text="Enter Player 1's payoff matrix separated by spaces:",
            bg="lightgray",
            font=("Times New Roman", 18))
        inputLabelP1.grid(row=3, column=0, pady=(50,10))
        p1Entry = tk.Entry(
            bosWindow, 
            width=20)
        p1Entry.grid(row=3, column=1, pady=(50,10))

        def submit_p1():
            p1Choice = p1Entry.get()
            print(p1Choice)
            BattleOfTheSexes.set_p1_bos(p1Choice)

        submitP1Button = tk.Button(
            bosWindow,
            text="Submit",
            font=("Times New Roman", 18),
            command=submit_p1)
        submitP1Button.grid(row=3, column=2, pady=(50,10))

        inputLabelP2 = tk.Label(
            bosWindow,
            text="Enter Player 2's payoff matrix separated by spaces:",
            bg="lightgray",
            font=("Times New Roman", 18))
        inputLabelP2.grid(row=4, column=0, pady=(50,10))
        p2Entry = tk.Entry(
            bosWindow, 
            width=20)
        p2Entry.grid(row=4, column=1, pady=(50,10))
        
        def submit_p2():
            p2Choice = p2Entry.get()
            print(p2Choice)
            BattleOfTheSexes.set_p2_bos(p2Choice)

        submitP2Button = tk.Button(
            bosWindow,
            text="Submit",
            font=("Times New Roman", 18),
            command=submit_p2)
        submitP2Button.grid(row=4, column=2, pady=(50,10))

        def display_results():
            p1 = BattleOfTheSexes.set_p1_bos(p1Entry.get())
            p2 = BattleOfTheSexes.set_p2_bos(p2Entry.get())
            game = BattleOfTheSexes.create_bos_game(p1, p2)
            gameResults = tk.Label(
                bosWindow,
                text=game,
                bg="lightgray",
                font=("Times New Roman", 12))
            gameResults.grid(row=5, column=1, pady=(50,10))
            sigma_p1 = BattleOfTheSexes.calc_p1_sigma(p1)
            sigma_p2 = BattleOfTheSexes.calc_p2_sigma(p2)
            utilities = BattleOfTheSexes.calc_utils(sigma_p1, sigma_p2, game)
            utilitiesResults = tk.Label(
                bosWindow,
                text=f"Utilities: {utilities}",
                bg="lightgray",
                font=("Times New Roman", 12))
            utilitiesResults.grid(row=5, column=2, pady=(50,10))
            best_resp = BattleOfTheSexes.best_response(p1, p2, sigma_p1, sigma_p2)
            bestRespResults = tk.Label(
                bosWindow,
                text=f"Best Response: {best_resp}",
                bg="lightgray",
                font=("Times New Roman", 12))
            bestRespResults.grid(row=5, column=3, pady=(50,10))
        
        resultsButton = tk.Button(
            bosWindow,
            text="Press for Results",
            bg="lightgray",
            font=("Times New Roman", 18),
            command=display_results)
        resultsButton.grid(row=5, column=0, pady=(50,10))

        bosWindow.grid_columnconfigure(0, weight=1)
        bosWindow.grid_columnconfigure(1, weight=1)
        bosWindow.grid_columnconfigure(2, weight=1)
        bosWindow.grid_columnconfigure(3, weight=1)
        bosWindow.grid_columnconfigure(4, weight=1)
        bosWindow.grid_columnconfigure(5, weight=1)

    def open_pdpage():
        pdWindow = tk.Toplevel(root)
        pdWindow.title("Prisoner's Dilemma")
        pdWindow.geometry("875x800")
        pdWindow.configure(bg="lightgray")
        pdtitle = tk.Label(
            pdWindow,
            text="Prisoner's Dilemma",
            fg="white",
            bg="#BB458D",
            font=("Times New Roman", 35),
            width=150,
            height=2)
        pdtitle.grid(row=0, column=0, columnspan=5, sticky="new")

        closeButton = tk.Button(
            pdWindow,
            text="Exit",
            font=("Times New Roman", 18),
            bg="#D87DB5",
            fg="Black",
            activebackground="#D87DB5",
            command=pdWindow.destroy)
        closeButton.grid(row=1, column=0, padx=1, pady=1,sticky="nw")

        inputLabelP1 = tk.Label(
            pdWindow,
            text="Enter Player 1's payoff matrix separated by spaces:",
            bg="lightgray",
            font=("Times New Roman", 18))
        inputLabelP1.grid(row=2, column=0, sticky="w", pady=(50,10))
        p1Entry = tk.Entry(
            pdWindow,
            font=("Times New Roman", 18), 
            width=20)
        p1Entry.grid(row=2, column=1, pady=(50,10))

        def submit_p1():
            p1Choice = p1Entry.get()
            print(p1Choice)
            PrisonersDilemma.set_p1_pd(p1Choice)

        submitP1Button = tk.Button(
            pdWindow,
            text="Submit",
            font=("Times New Roman", 18),
            command=submit_p1)
        submitP1Button.grid(row=2, column=2, pady=(50,10))

        inputLabelP2 = tk.Label(
            pdWindow,
            text="Enter Player 2's payoff matrix separated by spaces:",
            bg="lightgray",
            font=("Times New Roman", 18))
        inputLabelP2.grid(row=3, column=0, sticky="w", pady=(50,10))
        p2Entry = tk.Entry(
            pdWindow,
            font=("Times New Roman", 18), 
            width=20)
        p2Entry.grid(row=3, column=1, pady=(50,10))
        
        def submit_p2():
            p2Choice = p2Entry.get()
            print(p2Choice)
            PrisonersDilemma.set_p2_pd(p2Choice)

        submitP2Button = tk.Button(
            pdWindow,
            text="Submit",
            font=("Times New Roman", 18),
            command=submit_p2)
        submitP2Button.grid(row=3, column=2, pady=(50,10))

        def display_results():
            p1 = PrisonersDilemma.set_p1_pd(p1Entry.get())
            p2 = PrisonersDilemma.set_p2_pd(p2Entry.get())
            game = PrisonersDilemma.create_pd_game(p1, p2)
            gameResults = tk.Label(
                pdWindow,
                text=game,
                bg="lightgray",
                font=("Times New Roman", 12))
            gameResults.grid(row=5, column=1, pady=(50,10))
            sigma_p1 = PrisonersDilemma.calc_p1_sigma(p1)
            sigma_p2 = PrisonersDilemma.calc_p2_sigma(p2)
            utilities = PrisonersDilemma.calc_utils(sigma_p1, sigma_p2, game)
            utilitiesResults = tk.Label(
                pdWindow,
                text=f"Utilities: {utilities}",
                bg="lightgray",
                font=("Times New Roman", 12))
            utilitiesResults.grid(row=5, column=2, pady=(50,10))
            best_resp = PrisonersDilemma.best_response(p1, p2, sigma_p1, sigma_p2)
            bestRespResults = tk.Label(
                pdWindow,
                text=f"Best Response: {best_resp}",
                bg="lightgray",
                font=("Times New Roman", 12))
            bestRespResults.grid(row=5, column=3, pady=(50,10))
        
        resultsButton = tk.Button(
            pdWindow,
            text="Press for Results",
            bg="lightgray",
            font=("Times New Roman", 18),
            command=display_results)
        resultsButton.grid(row=4, column=0, pady=(50,10))

        pdWindow.grid_columnconfigure(0, weight=1)
        pdWindow.grid_columnconfigure(1, weight=1)
        pdWindow.grid_columnconfigure(2, weight=1)
        pdWindow.grid_columnconfigure(3, weight=1)
        pdWindow.grid_columnconfigure(4, weight=1)
        pdWindow.grid_columnconfigure(5, weight=1)

    def open_pmpage():
        pmWindow = tk.Toplevel(root)
        pmWindow.title("Polymatrix Games")
        pmWindow.geometry("875x800")
        pmWindow.configure(bg="lightgray")
        pmTitle = tk.Label(
            pmWindow,
            text="Polymatrix Games",
            fg="white",
            bg="#BB458D",
            font=("Times New Roman", 35),
            width=150,
            height=2)
        pmTitle.grid(row=0, column=0, columnspan=5, sticky="new")
        
        closeButton = tk.Button(
            pmWindow,
            text="Exit",
            font=("Times New Roman", 18),
            bg="#D87DB5",
            fg="Black",
            activebackground="#D87DB5",
            command=pmWindow.destroy)
        closeButton.grid(row=1, column=0, padx=1, pady=1,sticky="nw")

        pmDesc = tk.Label(
            pmWindow,
            text="Polymatrix games are games played by multiple players, represented by a graph.\nEach node represents a player and each edge represents a game being played.\nOne player can play multiple games with multiple players.",
            bg="lightgray")
        pmDesc.config(font=("Times New Roman", 18))
        pmDesc.grid(row=2, column=0, columnspan=5, pady=(50,10))

        inputPlayersLabel = tk.Label(
            pmWindow,
            text="Enter the number of players:",
            bg="lightgray",
            font=("Times New Roman", 18))
        inputPlayersLabel.grid(row=3, column=0, pady=(50,10))
        numPlayers = tk.Entry(
            pmWindow,
            font=("Times New Roman", 18),
            width=20)
        numPlayers.grid(row=3, column=1, pady=(50,10))

        def submit_num_players():
            numPlayersChoice = numPlayers.get()
            print(numPlayersChoice)
            PolymatrixGame(numPlayersChoice)
        
        submitNumPlayers = tk.Button(
            pmWindow,
            text="Submit",
            font=("Times New Roman", 18),
            command=submit_num_players)
        submitNumPlayers.grid(row=3, column=2, pady=(50,10))

        def display_results():
            num_players = numPlayers.get()
            payoffs = PolymatrixGame.generate_payoffs(num_players)
            payoffsLabel = tk.Label(
                pmWindow,
                text=f"Payoffs: {payoffs}",
                bg="lightgray",
                font=("Times New Roman", 12))
            payoffsLabel.grid(row=4, column=1, pady=(50,10))
            strategies = PolymatrixGame.generate_strategies(num_players)
            strategiesLabel = tk.Label(
                pmWindow,
                text=f"Strategies: {strategies}",
                bg="lightgray",
                font=("Times New Roman", 12))
            strategiesLabel.grid(row=4, column=2, pady=(50,10))
            bestResponse = PolymatrixGame.calc_best_response(num_players, payoffs)
            bestResponseLabel = tk.Label (
                pmWindow,
                text=f"Best Response: {bestResponse}",
                bg="lightgray",
                font=("Times New Roman", 12))
            bestResponseLabel.grid(row=4, column=3, pady=(50,10))
            nashEquilibria = PolymatrixGame.get_nash_equilibria(strategies, num_players, payoffs)
            nashEquilLabel = tk.Label(
                pmWindow,
                text=f"Nash Equilibrium: {nashEquilibria}",
                bg="lightgray",
                font=("Times New Roman", 12))
            nashEquilLabel.grid(row=4, column=4, pady=(50,10))
            drawGraph = PolymatrixGame.draw_graph(num_players, strategies, payoffs)
            drawGraphLabel = tk.Label(
                pmWindow,
                text=f"Graph: {drawGraph}",
                bg="lightgray",
                font=("Times New Roman", 12))
            drawGraphLabel.grid(row=4, column=5, pady=(50,10))

        resultsButton = tk.Button(
            pmWindow,
            text="Press for Results",
            bg="lightgray",
            font=("Times New Roman", 18),
            command=display_results)
        resultsButton.grid(row=4, column=0, pady=(50,10))

        pmWindow.grid_columnconfigure(0, weight=1)
        pmWindow.grid_columnconfigure(1, weight=1)
        pmWindow.grid_columnconfigure(2, weight=1)
        pmWindow.grid_columnconfigure(3, weight=1)
        pmWindow.grid_columnconfigure(4, weight=1)
        pmWindow.grid_columnconfigure(5, weight=1)

    def open_aboutPage():
        aboutWindow = tk.Toplevel(root)
        aboutWindow.title("About the Project")
        aboutWindow.geometry("875x800")
        aboutWindow.configure(bg="lightgray")
        aboutTitle = tk.Label(
            aboutWindow,
            text="About the Project",
            fg="white",
            bg="#BB458D",
            font=("Times New Roman", 35),
            width=150,
            height=2)
        aboutTitle.grid(row=0, column=0, columnspan=5, sticky="new")

        closeButton = tk.Button(
            aboutWindow,
            text="Exit",
            font=("Times New Roman", 18),
            bg="#D87DB5",
            fg="Black",
            activebackground="#D87DB5",
            command=aboutWindow.destroy)
        closeButton.grid(row=1, column=0, padx=1, pady=1,sticky="nw")

        aboutTxtIntro = tk.Label(
            aboutWindow,
            text="This project was created to produce a solution to the industrial strike action currently happening in the UK.",
            bg="lightgray")
        aboutTxtIntro.config(font=("Times New Roman", 18))
        aboutTxtIntro.grid(row=2, column=0, columnspan=5, pady=(50,10))

        aboutTxtAims = tk.Label(
            aboutWindow,
            text="Aims: To design and implement an effective solution to the industrial strike action using various areas of Game Theory.",
            bg="lightgray")
        aboutTxtAims.config(font=("Times New Roman", 18))
        aboutTxtAims.grid(row=3, column=0, columnspan=5, pady=(50,10))

        aboutTxtBackground = tk.Label(
            aboutWindow,
            text="Background: In recent years, there have been many disputes over the pay of workers in different sectors, which has led to ongoing industrial strike actions affecting millions.\nVarious unions, such as those for railway workers and teachers, have been promised pay rises from the government\nsince before the pandemic that have failed to be implemented despite the increasing cost of living and declining work conditions,\nwith hours becoming longer and staff members being laid-off.",
            bg="lightgray")
        aboutTxtBackground.config(font=("Times New Roman", 18))
        aboutTxtBackground.grid(row=4, column=0, columnspan=5, pady=(50,10))

        aboutWindow.grid_columnconfigure(0, weight=1)
        aboutWindow.grid_columnconfigure(1, weight=1)
        aboutWindow.grid_columnconfigure(2, weight=1)
        aboutWindow.grid_columnconfigure(3, weight=1)
        aboutWindow.grid_columnconfigure(4, weight=1)
        aboutWindow.grid_columnconfigure(5, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Algorithms for Solving Industrial Strike Action")
    root.geometry("875x800")
    root.configure(bg="lightgray")
    app = App(root)
    app.homepage()
    app.create_buttons()
    root.mainloop()