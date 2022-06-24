#!/usr/bin/env python3
import tcod

from engine import Engine
from entity import Entity
from input_handlers import EventHandler

def main() -> None:
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet("font10x10.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    event_handler = EventHandler()

    player = Entity(player_x, player_y, "@", (255, 255, 255))
    npc = Entity(player_x - 5, player_y, "@", (255, 255, 0))

    entities = {player, npc}

    engine = Engine(entities=entities, event_handler=event_handler, player=player)

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Battle Alchemist",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)

            
if __name__ == "__main__":
    main()