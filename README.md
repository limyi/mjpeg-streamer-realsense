# Intel RealSense D435i and MJPEG Streamer Setup

## Part 1: Installing Librealsense2

### Install dependencies

1. **Make Ubuntu up-to-date including the latest stable kernel:**

    ```bash
    sudo apt-get update && sudo apt-get upgrade && sudo apt-get dist-upgrade
    ```

2. **Install the core packages required to build librealsense binaries and the affected kernel modules:**

    ```bash
    sudo apt-get install libssl-dev libusb-1.0-0-dev libudev-dev pkg-config libgtk-3-dev
    ```

    **Note:** Certain librealsense CMAKE flags (e.g. CUDA) require version 3.8+ which is currently not made available via apt manager for Ubuntu LTS.

3. **Install build tools:**

    ```bash
    sudo apt-get install git wget cmake build-essential
    ```

### Prepare Linux Backend and the Dev. Environment

1. **Unplug any connected Intel RealSense camera and run:**

    ```bash
    sudo apt-get install libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev at
    ```

### Install librealsense2

1. **Clone/Download the latest stable version of librealsense2 in one of the following ways:**

    **Clone the librealsense2 repo:**

    ```bash
    git clone https://github.com/IntelRealSense/librealsense.git
    ```

### Building librealsense2 SDK

1. **Navigate to librealsense2 root directory and run:**

    ```bash
    mkdir build && cd build
    ```

2. **Run cmake configure step, here are some cmake configure examples:**

    The default build is set to produce the core shared object and unit-tests binaries in Debug mode.
    Use `-DCMAKE_BUILD_TYPE=Release` to build with optimizations.

    ```bash
    cmake ../
    ```

3. **Lastly run:**

    **Run Intel RealSense permissions script from librealsense2 root directory:**

    ```bash
    ./scripts/setup_udev_rules.sh
    ```

    **and reboot**

## Part 2: MJPEG Streamer with RealSense D435i Camera

This project sets up an MJPEG stream from a RealSense D435i camera using OpenCV and serves it over HTTP using a Python-based MJPEG server.

### Prerequisites

Before you start, ensure you have the following installed on your system:

- Python 3.x
- pip (Python package installer)

### Installation

Follow these steps to install the required dependencies:

1. **Install pip:**

    ```sh
    sudo apt install python3-pip
    ```

2. **Install OpenCV for Python:**

    ```sh
    pip3 install opencv-python
    ```

3. **Install the MJPEG Streamer library:**

    ```sh
    pip3 install mjpeg-streamer
    ```

### Usage

1. **Clone the repository:**

    ```sh
    git clone https://github.com/limyi/mjpeg-streamer-realsense.git
    cd mjpeg-streamer-realsense
    ```

2. **Run the script:**

    ```sh
    python3 stream_MJPEG.py
    ```

3. **Access the MJPEG stream from a web browser using the following URL (replace with your server's IP address):**

    ```
    http://192.168.1.221:8080/my_camera
    ```

### Troubleshooting

- Ensure that your camera is properly connected and recognized by the system. You can verify this using `ls /dev/video*`.
- Adjust the `VideoCapture` index if the camera is not detected. The default is `4` in the script.
- Make sure the specified `server_ip` matches your machine's IP address.
- Ensure the required ports are open and not blocked by a firewall.
- **Note:** Ensure that you are on the same network when you want to stream with another computer.
- **Note:** Ensure that you have given the necessary permissions to access the `/dev/video*` ports.

    ```sh
    sudo chmod 666 /dev/video*
    ```

## Additional Notes: Converting MJPEG Format to RTSP Format

To convert an MJPEG stream to an RTSP stream, follow these steps:

1. Download release from https://github.com/bluenviron/mediamtx/releases and extract the MediaMTX package:
   ```sh
   tar -xzf mediamtx_v0.0.0_linux_amd64.tar.gz
   cd mediamtx_v0.0.0_linux_amd64
   ```
2. Start the MediaMTX server:
    ```
    ./mediamtx
    ```
    
3. Run ffmpeg command line:
    ```
    ffmpeg -i http://192.168.1.221:8080/my_camera -c:v copy -f rtsp rtsp://localhost:8554/mystream

    ```
This will take the input from the MJPEG stream available at http://192.168.1.221:8080/my_camera and output it as an RTSP stream at rtsp://localhost:8554/mystream.

This snippet provides a step-by-step guide, including the download, extraction, server start, and stream conversion commands, all in one shot.
