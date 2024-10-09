#Import necessary modules
import os
import wave
import time
import threading
import tkinter as tk
import pyaudio

class VoiceRecoder:
    def __init__(self):
        #Initialize the GUI window
        self.root = tk.Tk()
        self.root.resizable(False, False) #Make the window not resizable
        
        #Create a 'Record' button with large font
        self.button = tk.Button(text = "Record", font =("Arial", 120, "bold"),
                                command = self.click_handler)
        self.button.pack() #Add the button to the GUI
        
        #Label for displaying recording time
        self.label = tk.Label(text = "00:00:00")
        self.label.pack() # Add the label to the GUI
        
        self.recording = False #Flag to check if recording is active
        self.root.mainloop() #Start the GUI event loop

    #Handler for button clicks
    def click_handler(self):
        if self.recording:
            self.recording = False
            self.button.config(fg = "black") #Change button text color to black
        else:
            self.recording = True
            self.button.config(fg = "red") #Change button text color to red
            threading.Thread(target = self.record).start() #Start recording in a new thread

    #Function to handle audio recording
    def record(self):
        audio = pyaudio.PyAudio() #Create a PyAudio object
        #Open a stream for audio input
        stream = audio.open(format = pyaudio.paInt16, channels=1, rate=44100,
                            input=True, frames_per_buffer=1024)
        
        frames = [] #List to hold audio frames

        start = time.time() #Record start time

        while self.recording:
            data = stream.read(1024) #Read audio data
            frames.append(data) #Append data to the frames list

            #Calculate elapsed time
            passed = time.time() - start
            secs = passed % 60
            mins = passed // 60
            hours = mins // 60
            #Update label with elapsed time
            self.label.config(text = f"{int(hours):02d}:{int(mins):02d}:{int(secs):02d}")

        #Stop and close the stream
        stream.stop_stream()
        stream.close()
        audio.terminate() #Terminate the PyAudio object

        #Determine a unique filename for the recording
        exists = True
        i = 1
        while exists:
            if os.path.exists(f"recording{i}.wav"):
                i += 1
            else:
                exists = False

        #Save the recorded audio
        sound_file = wave.open(f"recording{i}.wav", "wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)
        sound_file.writeframes(b"".join(frames)) #Write the audio frames to file
        sound_file.close() #Close the file


#Create instance of the voiceRecoder class
VoiceRecoder()