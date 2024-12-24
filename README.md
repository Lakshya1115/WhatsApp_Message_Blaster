# WhatsApp_Message_Blaster
Enter the number, select the file and blast whatsapp messages

# WhatsApp Message Blaster 🚀📱

Welcome to the **WhatsApp Message Blaster**! This funky tool lets you blast customized messages to multiple WhatsApp numbers using an easy-to-use GUI. 🎉

## 🌟 Features
- **Bulk Messaging**: Send messages to all numbers listed in an Excel sheet.
- **Simple UI**: Clean and intuitive interface built with Tkinter.
- **Excel Integration**: Supports `.xlsx` files with phone numbers.
- **Validation**: Ensures numbers are formatted correctly with the country code.
- **Automated Messaging**: Sends messages automatically using WhatsApp Web.

## 📦 Prerequisites
Before you dive in, make sure you have the following installed:

1. Python 3.8+
2. Required libraries:
   ```bash
   pip install tkinter pandas pywhatkit openpyxl
   ```
3. WhatsApp Web logged in on your browser.

## 🛠️ How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/whatsapp-message-blaster.git
   ```
2. Navigate to the project directory:
   ```bash
   cd whatsapp-message-blaster
   ```
3. Run the script:
   ```bash
   python whatsapp_blast_ui.py
   ```

4. Follow these steps in the app:
   - **Step 1**: Enter your message in the text box.
   - **Step 2**: Select your Excel file with phone numbers.
   - **Step 3**: Click on "Blast Messages" and watch the magic happen! ✨

## 📁 Excel File Format
Ensure your Excel file has a column named `Phone` containing phone numbers with the country code (e.g., `+1234567890`).

| Phone          |
|----------------|
| +1234567890    |
| +9876543210    |
| +1122334455    |

## 🚨 Notes
- Use this tool responsibly. Spamming is not cool! 😎
- Add slight delays between messages to avoid getting flagged by WhatsApp.
- Double-check that all phone numbers are formatted correctly with the `+` and country code.

## 🤔 FAQ
### **Q: Can I customize the delay between messages?**
Yes! Modify the `time.sleep(5)` line in the code to change the delay.

### **Q: What happens if I miss the country code in my numbers?**
The tool will display an error and stop the process.

### **Q: Is this tool free to use?**
Absolutely! It's open-source and free for all.

## 🏗️ Contributing
We welcome contributions! Feel free to fork this repository, create a feature branch, and submit a pull request. 💡

## 📜 License
This project is licensed under the MIT License. Feel free to use and modify it as per your needs.

---

Happy Blasting! 🎉📲

