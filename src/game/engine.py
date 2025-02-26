from rich.live import Live
from rich.prompt import Prompt
from rich.table import Table


from src.game.ui import GameUI
from src.scenes.managers.scene_manager import SceneManager
from src.scenes.managers.dialogue_manager import DialogueManager
from src.characters.char_types import CharacterType
from src.characters.player import Player

class GameEngine:
    def __init__(self):
        self.ui = GameUI()
        self.player = Player()
        self.ui.set_player(self.player)
        self.game_running = False


    # -------------------------------------------------------------
    def character_selection(self) -> bool:
        characters = list(CharacterType)
        
        # Create character selection table
        table = Table(show_header=True)
        table.add_column("Character", style="cyan")
        table.add_column("Passion", justify="center")
        table.add_column("Intelligence", justify="center")
        table.add_column("Charisma", justify="center")
        table.add_column("Strength", justify="center")
        table.add_column("Life", justify="center")

        for char_type in CharacterType:
            char = self.player.characters[char_type]
            stats = char.stats
            table.add_row(
                char_type.name.capitalize(),
                "★" * stats["passion"],
                "★" * stats["intelligence"],
                "★" * stats["charisma"],
                "★" * stats["strength"],
                "★" * stats["life"]
            )

        selected_preview = None

        with Live(self.ui.layout, refresh_per_second=4, screen=True):
            self.ui.update_display(
                game_text=f"\nChoose your character:\n\n{table}",
                input_text="Use number keys (1-4) to select:\n1. Evan\n2. SeanP\n3. SeanH\n4. Ryan\nPress Enter twice to confirm selection"
            )
            
            while True:
                choice = Prompt.ask("\nEnter your choice")
                
                if choice in ['1', '2', '3', '4']:
                    character_map = {
                        '1': 'EVAN',
                        '2': 'SEANP',
                        '3': 'SEANH',
                        '4': 'RYAN'
                    }
                    # Preview the character by temporarily selecting it
                    selected_preview = character_map[choice]
                    self.player.select_character(selected_preview)
                    self.ui.update_display(
                        game_text=f"Selected {selected_preview.capitalize()}\nPress Enter to confirm or choose another number",
                        input_text="Use number keys (1-4) to select:\n1. Evan\n2. SeanP\n3. SeanH\n4. Ryan\n\nPress Enter to confirm selection"
                    )
                    
                elif choice == "" and selected_preview:
                    return True
                else:
                    self.ui.console.print("Invalid choice. Please enter a number between 1 and 4.", style="error")
        pass

    # -------------------------------------------------------------
    # start game
    def start(self):
        self.ui.display_title_screen()
        if self.character_selection():
            self.game_running = True
            self.main_game_loop()
        else:
            with Live(self.ui.layout, refresh_per_second=4, screen=True):
                self.ui.update_display(
                    game_text="Character selection failed!", 
                    input_text="Please restart the game"
                )


    # -------------------------------------------------------------
    # game loop
    def main_game_loop(self):
        self.scene_manager = SceneManager()
        self.dialogue_manager = DialogueManager()
        
        with Live(self.ui.layout, refresh_per_second=4, screen=True):
            while self.game_running:
                current_scene = self.scene_manager.get_current_scene()
                
                # Handle initial dialogue if scene has one
                if current_scene.initial_dialogue:
                    dialogue_state = self.dialogue_manager.start_dialogue(current_scene.initial_dialogue)
                    while dialogue_state:
                        # Display dialogue text
                        dialogue_text = dialogue_state.get_text(self.player.current_character.name)
                        choices_text = "\n".join(
                            f"{i+1}. {choice.text}" 
                            for i, choice in enumerate(dialogue_state.choices)
                        )
                        
                        self.ui.update_display(
                            game_text=f"{dialogue_state.speaker}: {dialogue_text}",
                            input_text=choices_text
                        )
                        
                        # Get player choice
                        choice = Prompt.ask("\nSelect an option", choices=[
                            str(i+1) for i in range(len(dialogue_state.choices))
                        ])
                        
                        # Process choice
                        dialogue_state, next_scene = self.dialogue_manager.make_choice(
                            int(choice) - 1,
                            self.player.current_character.name
                        )
                        
                        # Handle scene transition if needed
                        if next_scene:
                            self.scene_manager.transition_to_scene(next_scene)
                            break
                
                # Display regular scene options when not in dialogue
                available_actions = current_scene.get_available_actions(
                    self.player.current_character.name,
                    self.player.get_stats()
                )
                
                actions_text = "\n".join(
                    f"{i+1}. {action.description}" 
                    for i, action in enumerate(available_actions)
                )
                
                self.ui.update_display(
                    game_text=current_scene.description,
                    input_text=actions_text
                )
                
                # Get player choice
                choice = Prompt.ask("\nSelect an option", choices=[
                    str(i+1) for i in range(len(available_actions))
                ])
                
                # Process scene transition
                selected_action = available_actions[int(choice) - 1]
                self.scene_manager.transition_to_scene(selected_action.next_scene)

