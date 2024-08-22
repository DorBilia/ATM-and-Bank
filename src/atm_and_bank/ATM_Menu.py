import customtkinter as ctk


class ATM_Menu:
    # Initialize the CustomTkinter app
    def __init__(self, user, credit_card):
        self.app = ctk.CTk()
        self.user = user
        self.credit_card = credit_card

    def create_menu(self):
        # Set window size and title
        self.app.geometry("500x500")
        self.app.title("ATM Menu")
        name_label = ctk.CTkLabel(master=self.app, text=f"Hello {self.user.get("name")}", font=("Arial", 24))
        name_label.pack(pady=10)
        balance_label = ctk.CTkLabel(master=self.app, text=f"Your balance: {self.user.get("balance")}$",font=("Arial", 20))
        balance_label.pack(pady=5)
        title_label = ctk.CTkLabel(master=self.app, text="Choose Action", font=("Arial", 24))
        title_label.pack(pady=20)

        # Set theme and appearance mode
        ctk.set_appearance_mode("System")

        # Create a frame to hold the grid of buttons
        frame = ctk.CTkFrame(master=self.app)
        frame.pack(pady=50)

        # Create the buttons and place them in a grid
        send_money_button = ctk.CTkButton(master=frame, text="Send Money", command=lambda: print("Send Money pressed"))
        send_money_button.grid(row=0, column=0, padx=20, pady=20)

        change_code_button = ctk.CTkButton(master=frame, text="Change Secret Code",
                                           command=lambda: print("Change Secret Code pressed"))
        change_code_button.grid(row=0, column=1, padx=20, pady=20)

        deposit_cash_button = ctk.CTkButton(master=frame, text="Deposit Cash",
                                            command=lambda: print("Deposit Cash pressed"))
        deposit_cash_button.grid(row=1, column=0, padx=20, pady=20)

        get_cash_button = ctk.CTkButton(master=frame, text="Get Cash", command=lambda: print("Get Cash pressed"))
        get_cash_button.grid(row=1, column=1, padx=20, pady=20)

        # Create a disconnection button
        exit_button = ctk.CTkButton(master=self.app, text="Exit", command=self.app.destroy, fg_color="red",
                                    hover_color="darkred")
        exit_button.pack()
        # Run the application
        self.app.mainloop()


if __name__ == "__main__":
    menu = ATM_Menu({"name": "abc", "balance": 100}, 122)
    menu.create_menu()
