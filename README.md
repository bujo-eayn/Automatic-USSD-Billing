# Automatic USSD Billing Script

This project is an automatic USSD billing script that utilizes Android's ADB (Android Debug Bridge) to automate the process of making payments via USSD codes. The script interacts with the M-Pesa service to complete transactions without manual input.

## Features

- Automatically dials a USSD code to initiate the payment process.
- Navigates through the M-Pesa menu options to reach the "Buy Goods and Services" option.
- Inputs the required till number, amount, and PIN for the transaction.
- Confirms the transaction and displays a confirmation message.

## Prerequisites

- Android device with ADB enabled.
- ADB installed on your computer.
- Basic knowledge of Python.

## Installation

1. **Install ADB**: Follow the instructions to install ADB on your operating system from the [official documentation](https://developer.android.com/studio/command-line/adb).

2. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/ussd-billing-script.git
   cd ussd-billing-script
   ```

3. **Connect your Android device**: Connect your Android device via USB and enable USB debugging.

4. **Run the Script**:
   ```sh
   python ussd_billing_script.py
   ```

## Usage

1. **Run the Script**: Execute the script using Python.
   ```sh
   python ussd_billing_script.py
   ```
2. **Enter your M-Pesa PIN**: When prompted, enter your M-Pesa PIN to authorize the transaction.

## Demonstration Video

<center>

[![Watch the video](https://github.com/bujo-eayn/Automatic-USSD-Billing/assets/68962169/c7af1353-4c11-4f85-ac8a-ecd6a0a02aae)](https://github.com/bujo-eayn/Automatic-USSD-Billing/assets/68962169/c7af1353-4c11-4f85-ac8a-ecd6a0a02aae)

</center>

## License

This project is licensed under the MIT License - see the LICENSE file for details.
