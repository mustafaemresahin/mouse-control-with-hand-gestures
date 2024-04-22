# Hand Gesture Recognition for Cursor Control

This project uses `OpenCV`, `MediaPipe`, and `PyAutoGUI` to enable hand gesture recognition for controlling the mouse cursor and performing various mouse actions like clicking and scrolling. The system utilizes a webcam to detect and track hand movements, translating these into cursor movements and clicks on the user's screen.

## Installation

Before running this project, ensure you have `Python` and `pip` installed on your system. Follow these steps to install the required dependencies:

### Setting Up a Virtual Environment (Optional but Recommended)

It's recommended to use a virtual environment for Python projects to keep dependencies organized and separate from other projects. Here's how to set up and use a virtual environment:

Install `virtualenv` if you haven't installed it yet

```bash
pip install virtualenv
```

Create a virtual environment
```bash
virtualenv venv
```

Activate the virtual environment
- On Windows
    ```bash
    .\venv\Scripts\activate
    ```
- On macOS and Linux
    ```bash
    source venv/bin/activate
    ```

### Installing Dependencies

Once the virtual environment is activated, install all required dependencies by running:

```bash
pip install -r requirements.txt
```

This command installs all the packages listed in the `requirements.txt` file, ensuring you have the correct versions needed to run the project.

### Deactivating the Virtual Environment

When you're done working on the project, you can `deactivate` the virtual environment by running:

```bash
deactivate
```

## Usage

To start the hand gesture recognition, run the main script from your command line:

```bash
python gesture_mouse_control.py
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
- Thanks to the contributors of the `OpenCV` and `PyAutoGUI` libraries for providing essential tools for image processing and GUI automation.
