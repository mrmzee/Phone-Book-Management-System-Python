# Phone Book Management System

#### Video Demo: [https://youtu.be/LMo8FGahBnI](https://youtu.be/LMo8FGahBnI)

#### Description:
The Phone Book Management System is a simple Python-based application for managing contact information. This project allows users to add new contacts, search for contacts by phone number, and store contact details in a JSON file. The contact details include the following fields:
- First Name
- Last Name
- Phone Number
- Age
- Country

### Features
- **Add Contact**: Users can add a new contact with the necessary details.
- **Find Contact**: Users can search for a contact by their phone number and view their details.
- **JSON Storage**: Contacts are stored in a JSON file for persistent storage.

### Project Structure
- `project.py`: Contains the main logic for managing contacts, including adding and finding contacts.
- `test_project.py`: Contains test cases for the functions in `project.py` using the `pytest` framework.
- `requirements.txt`: Lists the required packages, including `pytest` for running tests.

### How to Run
1. Install the required packages:
   ```sh
   pip install -r requirements.txt


2. Run the application:
   ```sh
   python project.py


3. Run the tests:
   ```sh
   pytest test_project.py

### Example Usage
Upon running the program, users will be presented with a menu to add a contact, find a contact by phone number, or exit the application:

    ```sh
      1. Add contact
      2. Find contact by phone number
      3. Exit


To add a contact, users need to follow the prompts to enter the contact's first name, last name, phone number, age, and country. The information will be stored, and a confirmation message will be displayed. To find a contact, users need to enter the phone number, and if the contact exists, their details will be displayed in a readable format:

    ```sh
      Contact found:
      Name: John Doe
      Last Name: Doe
      Phone: 1234567890
      Age: 30
      Country: USA

If the contact is not found, an appropriate message will be displayed.

Acknowledgements
This project was developed as part of the CS50 course. I would like to express my gratitude to the CS50 team for providing such a high-quality educational experience. Their resources and guidance have been invaluable in the development of this project.

Call for Contributions
I invite fellow developers to contribute to the further development of this project. There are many potential enhancements that can be made, such as:

Adding a graphical user interface (GUI) for easier interaction.
Implementing additional search and filter options.
Enhancing data validation and error handling.
Adding the ability to delete or update contacts.
If you are interested in contributing, please feel free to fork the repository and submit a pull request with your improvements. Your contributions are greatly appreciated and will help make this project more robust and user-friendly.







