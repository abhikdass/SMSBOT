# Telegram Bot for OTP and File Management

This project is a Telegram bot designed to assist users with OTP handling and file management functionalities. The bot can fetch OTP for various services, display information based on country and service, and split large files into smaller ones, making it versatile for everyday automation needs.

## Features

- **OTP Handling**: Fetch OTP for a range of supported services across different countries.
- **Country Selection**: Interactive country selection for OTP with inline keyboard.
- **File Splitting**: Split large text files into smaller parts by specifying lines per file.
- **Service Information Display**: View a list of supported services for OTP retrieval.

## Technologies Used

- **Python**: Core programming language for the bot's logic.
- **Pyrogram**: Telegram bot framework for handling messages and interactions.
- **Pykeyboard**: Library for managing inline keyboards in Telegram messages.
- **Requests**: HTTP requests library to interact with external APIs.

## Prerequisites

- Python 3.7 or above
- A Telegram Bot API token from [BotFather](https://core.telegram.org/bots#botfather)
- API credentials (API ID, API Hash) from [my.telegram.org](https://my.telegram.org)
- 5Sim API key for OTP handling (if using the 5Sim platform)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
2. **Install Dependencies**

    Install the required packages using pip:

    ```bash
    pip install -r requirements.txt
    Set Environment Variables

Create a .env file or set environment variables directly in your shell for sensitive information:

    API_ID=your_api_id
    API_HASH=your_api_hash
    BOT_TOKEN=your_bot_token
    AUTH_TOKEN=your_auth_token
Run the Bot

Start the bot using the following command:

    python bot.py

## USAGE
**OTP Handling**
Get OTP for Service: Use the /otp sitename command to fetch an OTP for a specified service and choose a country from the options displayed.
File Splitting
Split a File: Reply to a file with the /split <lines_per_file> command to split it into smaller parts.

**Example Commands**

/list — List supported OTP services.

/otp <sitename> — Get OTP for a specific site.

/split <lines_per_file> — Split a file into smaller files with specified lines per file.
License
This project is licensed under the MIT License.

Contributing
Feel free to open issues or submit pull requests to improve the project. All contributions are welcome!
