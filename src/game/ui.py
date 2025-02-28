from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.table import Table
from rich.align import Align
from rich.theme import Theme

class GameUI:
    # -------------------------------------------------------------
    # constructor
    def __init__(self):
        # theme to be used through game, if wanted add different themes for everyone
        self.theme = Theme({
            "info": "cyan",
            "warning": "green",
            "error": "bold red",
            "title": "bold magenta",
            "prompt": "bold green",
            "heading": "bold blue"
        })
        self.console = Console(theme=self.theme)
        self.layout = Layout()
        self.setup_layout()
        self.player = None

    def set_player(self, player):
        self.player = player


    
    # -------------------------------------------------------------
    # basic ui boxes
    def setup_layout(self):
        self.layout.split_row(
            Layout(name="left_panel", ratio=1),
            Layout(name="right_panel", ratio=2)
        )
        self.layout["right_panel"].split_column(
            Layout(name="game_area", ratio=2),
            Layout(name="input_area", ratio=1)
        )

    # -------------------------------------------------------------
    # left side stats panel, this must be fleshed out more
    def create_stats_panel(self):
        if not self.player.current_character:
            return Panel(Align.center("No character select"), title="Stats")
        
        stats = self.player.get_stats()

        # player health, talk with team how this is actually calculated based off base stats
        health_section = Table(show_header=False, box=None)
        health_section.add_row(
            "[bright_red]♥[/bright_red]" * stats['life']
        )
        health_panel = Panel(
            Align.center(health_section, vertical="middle"),
            title="[bright_red]Health[/bright_red]",
            border_style="red",
            padding=(0, 1)
        )

        meter_section = Table(show_header=False, box=None)
        meter_section.add_row(
            "[bright_green]███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ [/bright_green]" 
        )
        meter_panel = Panel(
            Align.center(meter_section, vertical="middle"),
            title="[green]Meter[/green]",
            padding=(0,1)
        )     

         # stats section, talk to team for rerendering now that stats go to 100
        stats_table = Table(show_header=False, box=None)
        stats_table.add_column("Stat", style="bright_cyan")
        stats_table.add_column("Value", style="bright_green", justify="right")
        
        # Add each stat to the table (excluding life and patrick_points)
        for stat, value in stats.items():
            if stat not in ['life', 'patrick_points']:
                stats_table.add_row(
                    stat.capitalize(),
                    "★" * value + "☆" * (10 - value)  # Shows both filled and empty stars
                )
        
        stats_panel = Panel(
            stats_table,
            title="[bright_cyan]Character Stats[/bright_cyan]",
            border_style="cyan",
            padding=(0, 1)
        )

        # 3. Create a vertical layout combining all sections
        layout = Table.grid(padding=0)
        layout.add_row(health_panel)
        layout.add_row(meter_panel)
        layout.add_row(stats_panel)
        
        
        # Wrap everything in a main panel
        return Panel(
            layout,
            title=f"[white]{self.player.current_character.name.name}[/white]",
            border_style="white",
            # padding=(10, 1)
        )
    
    # -------------------------------------------------------------
    # update display with updated stats and text (game_text and input_text)
    def update_display(self, game_text="", input_text=""):
        # Update left panel
        self.layout["left_panel"].update(self.create_stats_panel())
        
        # Update game area
        self.layout["game_area"].update(Panel(
            game_text,
            title="Tempe Quest",
            border_style="white"
        ))
        
        # Update input area
        self.layout["input_area"].update(Panel(
            input_text,
            title="Actions",
            border_style="red"
        ))

    # -------------------------------------------------------------
    def display_title_screen(self):
        title = """
        ▄▄▄█████▓▓█████  ███▄ ▄███▓ ██▓███  ▓█████      █████   █    ██ ▓█████   ██████ ▄▄▄█████▓
        ▓  ██▒ ▓▒▓█   ▀ ▓██▒▀█▀ ██▒▓██░  ██▒▓█   ▀    ▒██▓  ██▒ ██  ▓██▒▓█   ▀ ▒██    ▒ ▓  ██▒ ▓▒
        ▒ ▓██░ ▒░▒███   ▓██    ▓██░▓██░ ██▓▒▒███      ▒██▒  ██░▓██  ▒██░▒███   ░ ▓██▄   ▒ ▓██░ ▒░
        ░ ▓██▓ ░ ▒▓█  ▄ ▒██    ▒██ ▒██▄█▓▒ ▒▒▓█  ▄    ░██  █▀ ░▓▓█  ░██░▒▓█  ▄   ▒   ██▒░ ▓██▓ ░ 
          ▒██▒ ░ ░▒████▒▒██▒   ░██▒▒██▒ ░  ░░▒████▒   ░▒███▒█▄ ▒▒█████▓ ░▒████▒▒██████▒▒  ▒██▒ ░ 
          ▒ ░░   ░░ ▒░ ░░ ▒░   ░  ░▒▓▒░ ░  ░░░ ▒░ ░   ░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░  ▒ ░░   
            ░     ░ ░  ░░  ░      ░░▒ ░      ░ ░  ░    ░ ▒░  ░ ░░▒░ ░ ░  ░ ░  ░░ ░▒  ░ ░    ░    
          ░         ░   ░      ░   ░░          ░         ░   ░  ░░░ ░ ░    ░   ░  ░  ░    ░      
                    ░  ░       ░                ░  ░      ░       ░        ░  ░      ░           
        """
        self.console.print(Panel(title, style="title"))
        self.console.print("\nWelcome to Tempe Quest!", style="heading")
        self.console.print("A text adventure through the depths of Tempe", style="info")

        self.console.print("\nPress Enter to start...", style="prompt")
        input()


    