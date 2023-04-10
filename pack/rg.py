import pyaudio
import numpy as np
import hashlib
import cv2 as cv




def random_gen():
    # Define the audio parameters
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 2

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open the microphone stream
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    # Start recording
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    # Stop recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Concatenate the frames into a single byte string
    audio_bytes = b''.join(frames)

    # Compute the SHA-256 hash of the byte string
    hash_object = hashlib.sha256(audio_bytes)

    # Convert the hash to a 256-bit number
    hash_number = int.from_bytes(hash_object.digest(), byteorder='big')


    return hash_number

def random_gen_cam():
    cam_port = 0
    cam = cv.VideoCapture(cam_port)
  
    # reading the input using the camera
    result, image = cam.read()
  
    # If image will detected without any error, 
    # show result
    if result:
        random_numbers = np.random.randint(np.mean(image),np.sum(image),(1,20))
  
        img_bytes =random_numbers.tobytes()

        # Compute the SHA-256 hash of the byte string
        hash_object = hashlib.sha256(img_bytes)

        # Convert the hash to a 256-bit number
        hash_number = int.from_bytes(hash_object.digest(), byteorder='big')

        # Print the hash number
        return hash_number
  
    # If captured image is corrupted, moving to else part
    else:
        return "No image detected. Please! try again"
x=random_gen_cam()
print(x)





