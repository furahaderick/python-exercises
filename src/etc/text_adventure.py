# Text-based Adventure Game


# Location Class
class Location:
    """
    Represents a location on the game's map.

    Attributes:
    name(str): The location's name.
    description(str): The location's description.
    exits(dict): Exits that go out of the location.
    location_items(list): Items in the location.
    locked(bool): The open/closed state of the location.
    """

    def __init__(self, name, description, exits, location_items, locked):
        self.name = name
        self.description = description
        self.exits = exits
        self.location_items = location_items
        self.locked = locked


# Item Class
class Item:
    """
    Represents a game item.

    Attributes:
    name(str): The item's name.
    description(str): The item's description
    usable(bool): The item's usable state
    item_location(str): Where the item is found.
    """

    def __init__(self, name, description, usable, item_location):
        self.name = name
        self.description = description
        self.usable = usable
        self.item_location = item_location


class NPC:
    """
    Represents a non-player character

    Attributes:
    name(str): The NPC's name
    dialogue(str): The NPC's hint or dialogue
    npc_location(str): Where the NPC is found
    """

    def __init__(self, name, dialogue, npc_location):
        self.name = name
        self.dialogue = dialogue
        self.npc_location = npc_location


# Initial Game State
current_location = "village_ruins"
inventory = []

# Game Setup
locations = {
    "village_ruins": Location(
        "Village Ruins",
        "\n".join(
            [
                "You awaken amidst crumbling stone and tangled roots.",
                "The sky is gray, the air unnaturally still.",
                "A weathered statue of a robed figure stares blankly toward the horizon.",
                "An old man sits by a fire, murmuring to himself.",
                "Paths lead north and east, though the eastern road is blocked by rubble.",
            ]
        ),
        {"south": "whispering_forest"},
        [],
        False,
    ),
    "whispering_forest": Location(
        "Whispering Forest",
        "You are in a dark forest with whispering trees.",
        {
            "north": "village_ruins",
            "east": "forgotten_library",
            "south": "abandoned_chapel",
        },
        [],
        False,
    ),
    "forgotten_library": Location(
        "Forgotten Library",
        "You are in a dusty library filled with ancient books.",
        {"west": "whispering_forest"},
        [],
        True,
    ),
    "abandoned_chapel": Location(
        "Abandoned Chapel",
        "You are in a chapel with broken stained glass windows.",
        {"north": "whispering_forest", "south": "cavern_of_echoes"},
        [],
        False,
    ),
    "cavern_of_echoes": Location(
        "Cavern of Echoes",
        "You are in a dark cavern where your voice echoes.",
        {"north": "abandoned_chapel", "east": "frozen_passage"},
        [],
        False,
    ),
    "frozen_passage": Location(
        "Frozen Passage",
        "You are in a passage filled with ice and snow.",
        {"west": "cavern_of_echoes", "south": "tower_of_heartstone"},
        [],
        True,
    ),
    "tower_of_heartstone": Location(
        "Tower of Heartstone",
        "You are in a tower with a large heart-shaped stone at its center.",
        {"north": "frozen_passage"},
        [],
        False,
    ),
}

# Items Setup
items = {
    "rusted_sword": Item(
        "Rusted Sword",
        "An old, rusted sword that looks like it hasn't been used in years.",
        True,
        "village_ruins",
    ),
    "heartstone_fragment": Item(
        "Heartstone Fragment",
        "A fragment of the heartstone, glowing faintly.",
        True,
        "tower_of_heartstone",
    ),
}

# NPCs Setup
npcs = {
    "the_hermit": NPC(
        "The_Hermit",
        "The realm forgets, but the stone remembers.",
        "village_ruins",
    ),
}

# Main Game Loop
while True:

    # Get location
    location = locations[current_location]

    # TODO: Get items here
    items_in_sight = {
        key: obj for key, obj in items.items() if obj.item_location == current_location
    }
    # TODO: Get NPCs here

    # TODO: Print description (location, NPCs)
    print(f"\n{location.name}\n{location.description}")
    print()

    # Print exits
    exit_locations = location.exits
    print("Exits: ")
    for direction, destionation in exit_locations.items():
        print(f"- {direction}, to the {destionation}")
    print()

    # Print items
    print("Visible items: ")
    if len(items_in_sight) > 0:
        for key in items_in_sight:
            print(f"- {key}")
    else:
        print("- None")
    print()

    try:
        command = input("> ").strip().lower()
    except KeyboardInterrupt:
        print("\nSee you next time, adventurer.")
        break

    # go [direction] command
    if command.startswith("go "):
        direction = command.split(" ")[1]

        if direction in location.exits:
            if not locations[location.exits[direction]].locked:
                current_location = location.exits[direction]
            else:
                print(f"The {locations[location.exits[direction]].name} is locked!")
        else:
            print("I don't know where that is!")

    # command inventory
    elif command == "inventory":
        if len(inventory) > 0:
            print("You have these in inventory:")
            for item in inventory:
                print(f"- the {item}")
        else:
            print("You have nothing in your inventory.")

    # talk to [npc] command
    elif command.startswith("talk to "):
        npc = command.split(" ")[2]

        if npc in npcs:
            if npcs[npc].npc_location == current_location:
                print(f"{npcs[npc].name} says, '{npcs[npc].dialogue}'")
            else:
                print(f"{npcs[npc].name} is not here.")
        else:
            print(f"I don't know who {npc} is!")

    # take [item] command
    elif command.startswith("take "):
        item = command.split(" ")[1]

        # Check if [item exists] [items is in current location] [item is not already on the player]
        if item in items:
            if items[item].item_location == current_location:
                if item not in inventory:
                    inventory.append(item)
                    print(f"Now you have the {items[item].name}")
                else:
                    print(f"You already have the {items[item].name}")
            else:
                print(f"{items[item].name} is not here.")
        else:
            print("I don't know what that is!")

    # drop [item] command
    elif command.startswith("drop "):
        item = command.split(" ")[1]

        # Check if [item exists] [item is on the player]
        if item in items:
            if item in inventory:
                inventory.remove(item)
                items[item].item_location = current_location
                print(f"You dropped the {items[item].name}")
            else:
                print(f"You don't have the {items[item].name}")

        else:
            print("I don't know what that is!")

    elif command == "quit":
        print("Thanks for playing! See you next time.")
        break
    else:
        print("I don't understand that.")
