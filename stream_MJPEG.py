import cv2
from mjpeg_streamer import MjpegServer, Stream

# Initialize your OpenCV video capture device
cap = cv2.VideoCapture(4)
#cap = cv2.VideoCapture('/dev/video0')    #Use this if you are streaming via HDMI Output to USB converter

# Create a stream object
stream = Stream("my_camera", size=(640, 480), quality=50, fps=30)

# Specify the IP address of your server machine (replace with actual server IP)
server_ip = "192.168.168.187"  # Example IP address

# Initialize the MJPEG server with the server IP and port
server = MjpegServer(server_ip, 8080)

# Add the stream to the server
server.add_stream(stream)

# Start the MJPEG server
server.start()

print(f"Streaming MJPEG at http://{server_ip}:8080/my_camera")

# Capture frames and stream them
while True:
    _, frame = cap.read()
    cv2.imshow(stream.name, frame)
    if cv2.waitKey(1) == ord("q"):
        break

    # Update the frame in the stream
    stream.set_frame(frame)

# Clean up
server.stop()
cap.release()
cv2.destroyAllWindows()
