# MJPEG Streamer with RealSense D435i Camera

This project sets up an MJPEG stream from a RealSense D435i camera using OpenCV and serves it over HTTP using a Python-based MJPEG server.

## Prerequisites

Before you start, ensure you have the following installed on your system:

- Python 3.x
- pip (Python package installer)

## Installation

Follow these steps to install the required dependencies:

1. Install pip:

    ```sh
    sudo apt install python3-pip
    ```

2. Install OpenCV for Python:

    ```sh
    pip install opencv-python
    ```

3. Install the MJPEG Streamer library:

    ```sh
    pip install mjpeg-streamer
    ```

## Usage

1. Clone the repository:

    ```sh
    git clone https://github.com/limyi/mjpeg-streamer-realsense.git
    cd mjpeg-streamer-realsense
    ```

2. Run the script:

    ```sh
    python stream_MPEG.py
    ```

3. Access the MJPEG stream from a web browser using the following URL (replace with your server's IP address):

    ```
    http://192.168.1.221:8080/stream
    ```

## Troubleshooting

- Ensure that your camera is properly connected and recognized by the system. You can verify this using `ls /dev/video*`.
- Adjust the `VideoCapture` index if the camera is not detected. The default is `4` in the script.
- Make sure the specified `server_ip` matches your machine's IP address.
- Ensure the required ports are open and not blocked by a firewall.
- **Note:** Ensure that you are on the same network when you want to stream with another computer.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

