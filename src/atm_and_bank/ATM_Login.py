import customtkinter as ctk
import Run_ATM


class ATM_Login:
    # Initialize the CustomTkinter app
    def __init__(self):
        self.ATM = Run_ATM.Run_ATM()
        self.app = ctk.CTk()

    def create_login(self):
        # Set window size
        self.app.geometry("500x550")
        self.app.title("ATM Login")
        title = ctk.CTkLabel(master=self.app, text="ATM Login", font=("Arial", 20, "bold"))
        title.pack(pady=20)
        ctk.set_appearance_mode("System")
        # Add widgets for id
        id_label = ctk.CTkLabel(master=self.app, text="Your ID Number:")
        id_label.pack(pady=10)
        self.id_entry = ctk.CTkEntry(master=self.app, width=150)
        self.id_entry.pack(pady=5)
        # Add widgets for Credit Card Number
        credit_card_label = ctk.CTkLabel(master=self.app, text="Credit Card Number:")
        credit_card_label.pack(pady=10)
        self.credit_card_entry = ctk.CTkEntry(master=self.app, width=150)
        self.credit_card_entry.pack(pady=5)

        # Add widgets for Expiry Date (Month/Year)
        expiry_label = ctk.CTkLabel(master=self.app, text="Expiry (MM/YYYY):")
        expiry_label.pack(pady=10)

        expiry_frame = ctk.CTkFrame(master=self.app)
        expiry_frame.pack(pady=5)

        self.month_entry = ctk.CTkEntry(master=expiry_frame, width=50, placeholder_text="MM")
        self.month_entry.grid(row=0, column=0, padx=5)

        self.year_entry = ctk.CTkEntry(master=expiry_frame, width=50, placeholder_text="YYYY")
        self.year_entry.grid(row=0, column=1, padx=5)

        # Add widgets for CCV
        ccv_label = ctk.CTkLabel(master=self.app, text="CCV:")
        ccv_label.pack(pady=10)
        self.ccv_entry = ctk.CTkEntry(master=self.app, width=50)
        self.ccv_entry.pack(pady=5)
        # Add a login button
        login_button = ctk.CTkButton(master=self.app, text="Login", command=self.login)
        login_button.pack(pady=20)

        # def validate():
        #     if not validators.length(id_entry.get(), min=8, max=8):
        #         return "wrong ID number"
        #     if not validators.length(credit_card_entry.get(), min=16, max=16):
        #         return "wrong credit card number"
        #     if not validators.between(int(month_entry.get()), min=1, max=12) or not validators.between(int(year_entry.get()),
        #                                                                                                min=1000, max=9999):
        #         return "wrong year number"
        #     if not validators.between(int(month_entry.get()))
        # Run the application

        self.app.mainloop()

    def login(self):
        if self.ATM.login(self.id_entry.get(), self.credit_card_entry.get(), self.ccv_entry.get(),
                          self.month_entry.get(), self.year_entry.get()):
            print("successfully logged in")
        else:
            wrong_input_label = ctk.CTkLabel(master=self.app, text="Wrong information provided", text_color="red")
            wrong_input_label.pack()


if __name__ == "__main__":
    atm = ATM_Login()
    atm.create_login()
