import tkinter as tk
from tkinter import messagebox
from zenpy import Zenpy
import pandas as pd

def retrieve_tickets():
    email = email_entry.get()
    token = token_entry.get()
    subdomain = subdomain_entry.get()
    status = status_entry.get()

    if not email or not token or not subdomain or not status:
        messagebox.showerror("Input Error", "All fields must be filled out")
        return

    creds = {
        'email': email,
        'token': token,
        'subdomain': subdomain
    }

    try:
        print("... connecting to zendesk ...")
        zenpy_client = Zenpy(**creds)
        print("... ... successfully connected to zendesk!")

        print("... Querying Zendesk Tickets ...")
        raw_ticket_data = zenpy_client.search_export(type='ticket', status=status)
        print("... ... successfully retrieved zendesk tickets!")

        print("... converting zendesk raw object data to pandas dataframe ...")
        tickets = [ticket.to_dict() for ticket in raw_ticket_data]
        ticket_df = pd.DataFrame(tickets)
        print("... ... successfully converted python dict to pandas dataframe!")
        
        ticket_df_rowcount = ticket_df.shape[0]
        print(f"... ... which has {ticket_df_rowcount} rows of tickets!")

        # Uncomment these lines if you want to push data to BigQuery
        # print("... push data in BigQuery ...")
        # pandas_gbq.to_gbq(ticket_df, table_id, project_id=project_id)
        # print("... ... successfully imported data in BigQuery!")
        
        messagebox.showinfo("Success", f"Retrieved {ticket_df_rowcount} tickets")
    except Exception as e:
        messagebox.showerror("Error", str(e))

app = tk.Tk()
app.title("Zendesk Ticket Retriever")

tk.Label(app, text="Your Email").grid(row=0, column=0, padx=10, pady=5)
email_entry = tk.Entry(app)
email_entry.grid(row=0, column=1, padx=30, pady=5)

tk.Label(app, text="Your API Token").grid(row=1, column=0, padx=10, pady=5)
token_entry = tk.Entry(app, show="*")
token_entry.grid(row=1, column=1, padx=30, pady=5)

tk.Label(app, text="Your Subdomain").grid(row=2, column=0, padx=10, pady=5)
subdomain_entry = tk.Entry(app)
subdomain_entry.grid(row=2, column=1, padx=30, pady=5)

tk.Label(app, text="Ticket Status").grid(row=3, column=0, padx=10, pady=5)
status_entry = tk.Entry(app)
status_entry.grid(row=3, column=1, padx=30, pady=5)

submit_button = tk.Button(app, text="Start!", command=retrieve_tickets)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

app.mainloop()
