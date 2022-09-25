import random

class Director: #just director this class 
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card (List[Die]): A list of card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.player_start_points = 300
        self.current_card = random.randint(1, 13)
        self.next_card = random.randint(1, 13)
        self.score = 0
        self.total_score = 0

    
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.card:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        user_choice = input("Higher or Lower? [h/l] ")
        self.card = user_choice == "h" 
        
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        self.score = 0
        
        if not self.is_playing:
            return 

        for i in self.card:
            card = self.dice[i]
            card.draw()
            self.score += self.values 
        self.total_score += self.score

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""
        for i in self.card:
            card = self.card[i]
            values += f"{card.value} "

        print(f"You rolled: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.card = (self.score > 0)





   