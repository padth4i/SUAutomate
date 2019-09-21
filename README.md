# Status Update Automation

Telegram bot to send automated status updates.

## Usage
1. Clone the scripts onto your machine.

2. Change your email id and password on `emailbot.py`.

3. Run the following commands one after the other.

```
crontab -l > mycron
echo "00 22 * * * python3 path/to/reminderbot.py" >> mycron
echo "45 22 * * * python3 path/to/emailbot.py" >> mycron
crontab mycron
rm mycron
```

The Telegram bot reminds you to send daily updates which are then automatically sent to the status update thread. On sending updates, you will be given points based on how regularly you send updates, how detailed you write them and how early you push them. At the end of each week, the members will be awarded titles like `Early Bird` and `Hard Worker`. At the end of the month, the member with the highest number of points will win some awesome swag 😄.
