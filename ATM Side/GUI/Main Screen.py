import customtkinter as ctk
from customtkinter import CTkLabel
import Mongo
from datetime import datetime

# Initialize the CustomTkinter app
app = ctk.CTk()

# Set window size
app.geometry("500x550")
app.title("ATM Login")
title = CTkLabel(master=app, text="ATM Login", font=("Arial", 20, "bold"))
title.pack(pady=20)
ctk.set_appearance_mode("System")
# Add widgets for id
id_label = ctk.CTkLabel(master=app, text="Your ID Number:")
id_label.pack(pady=10)
id_entry = ctk.CTkEntry(master=app, width=150)
id_entry.pack(pady=5)
# Add widgets for Credit Card Number
credit_card_label = ctk.CTkLabel(master=app, text="Credit Card Number:")
credit_card_label.pack(pady=10)
credit_card_entry = ctk.CTkEntry(master=app, width=150)
credit_card_entry.pack(pady=5)

# Add widgets for Expiry Date (Month/Year)
expiry_label = ctk.CTkLabel(master=app, text="Expiry (MM/YYYY):")
expiry_label.pack(pady=10)

expiry_frame = ctk.CTkFrame(master=app)
expiry_frame.pack(pady=5)

month_entry = ctk.CTkEntry(master=expiry_frame, width=50, placeholder_text="MM")
month_entry.grid(row=0, column=0, padx=5)

year_entry = ctk.CTkEntry(master=expiry_frame, width=50, placeholder_text="YYYY")
year_entry.grid(row=0, column=1, padx=5)

# Add widgets for CCV
ccv_label = ctk.CTkLabel(master=app, text="CCV:")
ccv_label.pack(pady=10)
ccv_entry = ctk.CTkEntry(master=app, width=50)
ccv_entry.pack(pady=5)

# Add a login button
login_button = ctk.CTkButton(master=app, text="Login", command=lambda: Login())
login_button.pack(pady=20)


def Login():
    mongo = Mongo.Mongo()
    date_str = f"{month_entry.get()}/{year_entry.get()}"
    date_format = '%m/%Y'
    result = mongo.search_card(id_entry.get(), credit_card_entry.get(), ccv_entry.get(),
                               datetime.strptime(date_str, date_format))
    if result == {}:
        pass
    else:
        print(result)

    # Run the application
app.mainloop()
