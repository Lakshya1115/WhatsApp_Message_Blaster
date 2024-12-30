import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import pywhatkit as kit
import time

class WhatsAppBlaster:
    def __init__(self, root):
        self.root = root
        self.root.title("WhatsApp Message Blaster")
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.root, text="Message:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.message_entry = tk.Text(self.root, height=5, width=40)
        self.message_entry.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(self.root, text="Select Excel File:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.file_path_entry = tk.Entry(self.root, width=40)
        self.file_path_entry.grid(row=1, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Browse", command=self.browse_file).grid(row=1, column=2, padx=10, pady=5)
        tk.Button(self.root, text="Blast Messages", command=self.blast_messages).grid(row=2, column=1, pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        self.file_path_entry.delete(0, tk.END)
        self.file_path_entry.insert(0, file_path)

    def blast_messages(self):
        file_path = self.file_path_entry.get()
        message = self.message_entry.get("1.0", tk.END).strip()
        default_country_code = "+91"  
        error_numbers = []

        if not file_path:
            messagebox.showerror("Error", "Please select an Excel file.")
            return

        if not message:
            messagebox.showerror("Error", "Please enter a message.")
            return

        try:
            df = pd.read_excel(file_path)
            if 'Phone' not in df.columns:
                messagebox.showerror("Error", "The Excel file must contain a column named 'Phone'.")
                return

            phone_numbers = df['Phone'].dropna().astype(str).tolist()
            for number in phone_numbers:
                number = number.strip()
                if '.' in number:
                    number = number.split('.')[0]  # Remove decimal points
                if not number.startswith("+"):
                    number = default_country_code + number

                print(f"Sending message to {number}...")
                try:
                    kit.sendwhatmsg_instantly(number, message, wait_time=15) 
                    print(f"Message sent to {number}.")
                except Exception as e:
                    print(f"Failed to send message to {number}: {e}")
                    error_numbers.append((number, str(e)))
                time.sleep(10)  # Add delay between messages

            if error_numbers:
                with open("error_numbers.txt", "w") as error_file:
                    for num, err in error_numbers:
                        error_file.write(f"{num}: {err}\n")
                messagebox.showwarning("Warning", "Some messages failed to send. Check 'error_numbers.txt' for details.")

            messagebox.showinfo("Success", "Messages have been sent successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WhatsAppBlaster(root)
    root.mainloop()
