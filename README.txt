# Writer's Block Helper
This program provides an interface with a text editor, that allows you to type freely, and incentivizes you to write constantly without stopping, letting your ideas flow.

## Installing libraries
1. Create and set up your [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).
2. Run this line in the terminal to install the required libraries:
```
python -m pip install -r requirements.txt
```

## Functionality
Once the "Start" button is pressed in the editor, a timer will start counting down (5 seconds by default) and you will be able to start typing. Each text input will reset the timer — if no input is given within the time limit the text interface will be disabled, and the written text will be grayed out.

You can use the "Copy Text" button to copy the text inputted in the editor both before and after the timer has run out.

The "Logs" button currently has no functionality.

## Timer Setting
You can change the timer length by going into the "writing_helper.py" file, and modifying the value of "TIMER_LENGTH_SECONDS" variable in the "Constants" section. The value will be the amount of seconds that the timer will run for.
