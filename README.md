# Gmail Email Extractor

This Python script connects to a Gmail account using the Gmail API and extracts the content of emails from the specified label (default is the Inbox). It retrieves details such as the subject, sender, date, and content of each email.

## Dependencies
- Python 3.10.7 or greater
- The pip package management tool (ensure pip is installed)
- Run the following command to install the required packages:


pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib


## Functionality
1. **Authentication:** The script authenticates the user using OAuth 2.0 to access the Gmail API.
2. **Label Selection:** It retrieves a list of Gmail labels associated with the user's account and selects the specified label (default is the Inbox).
3. **Email Extraction:** For each email in the selected label, the script fetches details such as the subject, sender, date, and content.
4. **Display:** It prints the extracted details of each email, including the subject, sender, date, and content.

## How to Run
1. Ensure Python 3.10.7 or greater is installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Execute the script using the following command:

python quickstart.py

6. Follow the authentication prompts to grant access to your Gmail account.
7. The script will then retrieve and display the details of emails from the specified label.

**Note:** Ensure that the `credentials.json` file, containing OAuth 2.0 credentials, is present in the same directory as the script. Additionally, the `token.json` file will be generated automatically to store access and refresh tokens for future use.
