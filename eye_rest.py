import time
from plyer import notification
from tkinter import Tk, messagebox

def time1():
    print("Timer")
    print("For eye care, you should not look at the screen continuously for more than 20 minutes.")
    
    name = input("Enter your name: ")
    
    print("Your 20-minute timer will start shortly...")
    for i in range(5, 0, -1):
        print(f"Starting in {i} seconds...")
        time.sleep(1)
    
    for i in range(20, 0, -1):
        print(f"{i} minutes left")
        time.sleep(60)  # Wait for 1 minute

def second_20():
    print("20-second timer started.")
    for i in range(20, 0, -1):
        print(f"{i} seconds left")
        time.sleep(1)  # Wait for 1 second
    for i in range(1):
        notification.notify(
                title="Eye Care Reminder",
                message="You can work now",
                timeout=5
            )

def show_message():
    # Initialize the Tkinter root window (hidden)
    root = Tk()
    root.withdraw()
    
    # Show the notification
    for i in range(1):
        notification.notify(
            title="Eye Care Reminder",
            message="It's time to take a 20-second break.",
            timeout=5
        )
    
    # Display a message box
    response = messagebox.askquestion("Reminder", "Please take a 20-second break. Click 'Yes' to start the 20-second timer.")
    return response

def main():
    time1()
    response = show_message()
    if response == "yes":
        second_20()
    else:
        print("Thank you for using the eye care reminder.")

if __name__ == "__main__":
    main()
