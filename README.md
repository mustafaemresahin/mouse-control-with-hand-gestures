# Hand Gesture Recognition for Cursor Control

This project uses OpenCV, MediaPipe, and PyAutoGUI to enable hand gesture recognition for controlling the mouse cursor and performing various mouse actions like clicking and scrolling. The system utilizes a webcam to detect and track hand movements, translating these into cursor movements and clicks on the user's screen.

## Installation

Before running this project, ensure you have the following prerequisites installed on your system:

### Prerequisites

- Python 3.7 or later
- OpenCV
- MediaPipe
- PyAutoGUI

You can install the required packages using pip:

```bash
pip install opencv-python mediapipe pyautogui
```

## Usage

To start the hand gesture recognition, run the main script from your command line:

```bash
python hand_gesture_recognition.py
```


### How It Works

- **Cursor Movement**: Use your left hand's index finger to control the mouse cursor. Movement of this finger will directly translate to cursor movement on the screen.

- **Scrolling**: Squeeze your left hand's index finger and thumb together, then move them up or down to scroll up or down respectively.

- **Left Click**: Squeeze the index finger and thumb of your right hand together to perform a left click.

- **Right Click**: Squeeze the middle finger and thumb of your right hand together to perform a right click.

### Controls

- Close the application by pressing the `ESC` key while the webcam window is active.

## Acknowledgments

- This project utilizes the [MediaPipe](https://google.github.io/mediapipe/) framework for hand tracking.
- Thanks to the contributors of the OpenCV and PyAutoGUI libraries for providing essential tools for image processing and GUI automation.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.

