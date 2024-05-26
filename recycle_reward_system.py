class RecyclableItem:
    reward_rates = {
        'A': 0.10,
        'B': 0.05,
        'C': 0.15
    }
    
    def __init__(self, item_type):
        self.item_type = item_type
    
    def get_reward(self):
        return self.reward_rates.get(self.item_type.upper(), 0)

class RewardSystem:
    def __init__(self):
        self.items = []
        self.total_rewards = 0
    
    def add_item(self, item_type):
        item = RecyclableItem(item_type)
        reward = item.get_reward()
        if reward > 0:
            self.items.append(item)
            self.total_rewards += reward
            print(f"Added item of type {item_type.upper()} with reward {reward:.2f} INR")
        else:
            print(f"Invalid item type: {item_type}")
    
    def display_total_rewards(self):
        print(f"Total rewards earned: {self.total_rewards:.2f} INR")

    def display_items(self):
        item_count = {'A': 0, 'B': 0, 'C': 0}
        for item in self.items:
            item_count[item.item_type.upper()] += 1
        print(f"Items collected: {item_count}")

    def reset_session(self):
        self.items = []
        self.total_rewards = 0
        print("System has been reset for a new user session.")

def main():
    system = RewardSystem()
    print("Welcome to the Automated Collection and Reward System for Recyclable Items!")
    try:
        while True:
            print("\nMenu:   Rewards: {:.2f} INR".format(system.total_rewards))
            print("1. Add recyclable item")
            print("2. Display collected items")
            print("3. Reset system for new user session")
            print("4. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                item_type = input("Enter the item type (A, B, C): ")
                system.add_item(item_type)
            elif choice == '2':
                system.display_items()
            elif choice == '3':
                system.reset_session()
            elif choice == '4':
                print("Thank you for using the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nExiting the system...")

if __name__ == "__main__":
    main()