from tkinter import messagebox
import customtkinter as ctk
import ATM_Manager


class ATM_Menu:
    # Initialize the CustomTkinter app
    def __init__(self, user, credit_card):
        self.ATM = ATM_Manager.ATM_Manager()
        self.app = ctk.CTk()
        self.user = user
        self.credit_card = credit_card

    def create_menu(self):
        # Set window size and title
        self.app.geometry("500x500")
        self.app.title("ATM Menu")
        name_label = ctk.CTkLabel(master=self.app, text=f"Hello {self.user.get("name")}", font=("Arial", 24))
        name_label.pack(pady=10)
        balance_label = ctk.CTkLabel(master=self.app, text=f"Your balance: {self.user.get("balance")}$",
                                     font=("Arial", 20))
        balance_label.pack(pady=5)
        frame_label = ctk.CTkLabel(master=self.app,
                                   text=f"Frame used: {self.credit_card.get("used")}/{self.credit_card.get("frame")}$",
                                   font=("Arial", 20))
        frame_label.pack(pady=5)
        title_label = ctk.CTkLabel(master=self.app, text="Choose Action", font=("Arial", 24))
        title_label.pack(pady=20)

        # Set theme and appearance mode
        ctk.set_appearance_mode("System")

        # Create a frame to hold the grid of buttons
        frame = ctk.CTkFrame(master=self.app)
        frame.pack(pady=50)

        # Create the buttons and place them in a grid
        send_money_button = ctk.CTkButton(master=frame, text="Send Money", command=lambda: self.send_money())
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

    def send_money(self):
        retry_id = True
        while retry_id:
            id_dialog = ctk.CTkInputDialog(title="Send Money", text="Enter Receiver's ID:", )
            receiver_account_id = id_dialog.get_input()
            if self.ATM.validate_account(receiver_account_id):
                amount_dialog = ctk.CTkInputDialog(title="Send Money", text="Enter Amount", )
                amount = amount_dialog.get_input()
                try_to_get = self.try_to_get_money(amount)
                while try_to_get == True:
                    amount_dialog = ctk.CTkInputDialog(title="Send Money", text="Enter Amount", )
                    amount = amount_dialog.get_input()
                    try_to_get = self.try_to_get_money(amount)
                if try_to_get == False:
                    break
                if self.try_to_enter_code():
                    if self.ATM.send_money(self.user, self.credit_card, receiver_account_id, int(amount)):
                        messagebox.showinfo("Success", "Money Sent!")
                        break
                    else:
                        messagebox.showerror("Error", "Unexpected Error happened\nplease contact the bank")
                else:
                    messagebox.showerror("Error", "Your credit card has been blocked due to too many attempts\n "
                                                  "please contact the bank to unblock it")
                retry_id = False
            else:
                retry_id = messagebox.askretrycancel("Error", "Wrong ID")

    def try_to_get_money(self, amount):  # checks if the amount entered can actually be sent,
        # if yes, the function will return "Amount valid"
        try:
            amount = int(amount)
            res = "Amount valid"
            if self.user.get("balance") < amount:
                res = messagebox.askretrycancel("Error", "Insufficient funds")
            elif self.credit_card.get("frame") < self.credit_card.get("used") + amount:
                res = messagebox.askretrycancel("Error", "Frame limit reached")
            elif amount <= 0:
                res = messagebox.askretrycancel("Error", "You should enter positive amount")
        except:
            res = messagebox.askretrycancel("Error", "You should enter positive amount")
        return res

    def try_to_enter_code(self):
        tries = 3
        correct_code = self.credit_card.get("secretCode")
        while tries > 0:
            code_dialog = ctk.CTkInputDialog(title="Secret code",
                                             text=f"Enter your secret code\nattempts left: {tries}")
            code_input = code_dialog.get_input()
            if int(code_input) == correct_code:
                break
            else:
                tries -= 1
        if tries == 0:
            return False
        return True

# if __name__ == "__main__":
#     menu = ATM_Menu({"name": "abc", "balance": 100}, {})
#     menu.create_menu()
