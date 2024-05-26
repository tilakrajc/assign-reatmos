# assign-reatmos
a basic Python project that simulates the core functionalities of an automated collection and reward system for recyclable items. The project should accept various types of recyclable items, calculate rewards based on the item type, and maintain a simple user interface for interactions.

This is an assignment repository and created solely for these purposes.

# Automated Collection and Reward System for Recyclable Items

## Overview

This project simulates an automated collection and reward system for recyclable items. The system accepts different types of recyclable items, calculates rewards based on the item type, and maintains a simple command-line interface for user interactions. The system supports adding items, viewing total rewards, viewing collected items, and resetting the system for a new user session.

## Requirements

- Python 3.x

## Instructions

### Running the Project

1. Ensure you have Python 3.x installed on your system.
2. Download or clone the project files to your local machine.
3. Open a terminal and navigate to the directory containing the project file.
4. Run the script using the command:
   ```sh
   python recycle_reward_system.py

## Using the CLI
Add recyclable item: Allows you to add an item of type A, B, or C.
Display total rewards: Shows the total rewards accumulated for the current session.
Display collected items: Shows a count of each type of item collected.
Reset system for new user session: Resets the system, clearing all collected items and rewards.
Exit: Exits the application.
## Design Decisions
### Class Structure
1. RecyclableItem Class: Represents a recyclable item and contains the logic for determining the reward based on the item type.

2. reward_rates: A dictionary mapping item types to their respective reward rates.
__init__(self, item_type): Initializes the item with a specified type.
get_reward(self): Returns the reward for the item's type.
3. RewardSystem Class: Manages the collection of items and the calculation of total rewards.

__init__(self): Initializes an empty list of items and sets total rewards to zero.
add_item(self, item_type): Adds a recyclable item to the system and updates the total rewards.
display_total_rewards(self): Prints the total rewards accumulated.
display_items(self): Prints the count of each type of item collected.
reset_session(self): Resets the system for a new user session, clearing all collected items and rewards.
## Command-Line Interface (CLI)
1. The CLI provides an interactive menu for the user to add items, view rewards, view collected items, reset the system, and exit the application.
2. User input is handled using the input() function.
3. The menu is displayed in a loop, allowing the user to perform multiple actions before exiting.