import tkinter as tk
from tkinter import filedialog
import pygame
import os

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Sfopity")
        self.master.geometry("800x100")
        self.master.configure(bg="pink")

        self.playlist= []

        self.currentTrack =tk.StringVar()
        self.currentTrack.set("Nothing yet")  

        pygame.init()
        pygame.mixer.init()

    def createWidgs(self):
        playButton =tk.Button(self.master, text="Play", command=self.playMusic)
        playButton.pack(side=tk.LEFT, padx=10)

        pauseButton =tk.Button(self.master, text="Pause", command=self.pauseMusic)
        pauseButton.pack(side=tk.LEFT, padx=10)

        stopButton =tk.Button(self.master, text="Stop", command=self.stopMusic)
        stopButton.pack(side=tk.LEFT, padx=10)

        prevButton =tk.Button(self.master, text="prev", command=self.prevTrack)
        prevButton.pack(side=tk.LEFT, padx=10)

        nextButton =tk.Button(self.master, text="next", command=self.nextTrack)
        nextButton.pack(side=tk.LEFT, padx=10)

        addFilesButton = tk.Button(self.master, text="Add Files", command=self.addFiles)
        addFilesButton.pack(side=tk.LEFT, padx=10)

        volumeLabel=tk.Label(self.master, text="Volume:")
        volumeLabel.pack(side=tk.LEFT, padx=10)

        volumeSlider=tk.Scale(self.master, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume, bg="pink")
        volumeSlider.set(30)
        volumeSlider.pack(side=tk.LEFT, padx=10)

        trackLabel=tk.Label(self.master, textvariable=self.currentTrack, bg="black", fg="pink")
        trackLabel.pack(pady=10, side='left')

    def playMusic(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[0])
            pygame.mixer.music.play(0)
            self.updateCurrentTrackLabel()
                
    def pauseMusic(self):
        pygame.mixer.music.pause()

    def stopMusic(self):
        pygame.mixer.music.stop()
        
    def nextTrack(self):
        if self.playlist:
            self.playlist.append(self.playlist.pop(0))
            self.playMusic()
            self.updateCurrentTrackLabel()

    def prevTrack(self):
        if self.playlist:
            self.playlist.insert(0, self.playlist.pop())
            self.playMusic()
            self.updateCurrentTrackLabel()

    def set_volume(self, vol):
        volume=int(vol)/100
        pygame.mixer.music.set_volume(volume)

    def addFiles(self):
        files = filedialog.askopenfilenames(title="Select Audio Files", filetypes=[("Audio Files", "*.mp3;*.wav")])
        self.playlist.extend(files)

    def updateCurrentTrackLabel(self):
        if self.playlist:
            currentTrack = os.path.basename(self.playlist[0])
            self.currentTrack.set(currentTrack)
          

def main():
    root=tk.Tk()
    app= MusicPlayer(root)
    app.createWidgs()
    root.mainloop()
    root.configure(bg="Pink")

if __name__ == "__main__":
    main()
