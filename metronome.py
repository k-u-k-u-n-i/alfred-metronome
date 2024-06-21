#!/Users/john/.venv/bin/python

import time
import pygame
import os
import sys
import signal
import psutil

# Initialize pygame mixer
pygame.mixer.init()

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Path to sound files
SOUND_FILE_ONE = os.path.join(script_dir, "metronome-click-1.mp3")
SOUND_FILE_OTHER = os.path.join(script_dir, "metronome-click.mp3")

# Load sound files
sound_one = pygame.mixer.Sound(SOUND_FILE_ONE)
sound_other = pygame.mixer.Sound(SOUND_FILE_OTHER)

def play_metronome(bpm):
    # Calculate interval in seconds (60 seconds divided by BPM)
    interval = 60.0 / bpm
    beat_count = 0

    while True:
        start_time = time.time()

        if beat_count == 0:
            sound_one.play()
        else:
            sound_other.play()

        beat_count = (beat_count + 1) % 4

        # Ensure the timing is precise by subtracting the elapsed time
        elapsed_time = time.time() - start_time
        time.sleep(max(0, interval - elapsed_time))

def kill_metronome_procs():
    current_pid = os.getpid()
    script_name = os.path.basename(__file__)
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        if os.path.exists("/tmp/metronome.pid"):
            os.remove("/tmp/metronome.pid")
        try:
            cmdline = proc.info['cmdline']
            if cmdline and len(cmdline) > 1 and script_name in cmdline[1]:
                if proc.info['pid'] != current_pid:
                    os.kill(proc.info['pid'], signal.SIGKILL)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        bpm = int(sys.argv[1])
        if os.path.exists("/tmp/metronome.pid"):
            with open("/tmp/metronome.pid", "r") as f:
                pid = int(f.read())
            os.kill(pid, signal.SIGKILL)
            os.remove("/tmp/metronome.pid")
        with open("/tmp/metronome.pid", "w") as f:
            f.write(str(os.getpid()))
        play_metronome(bpm)
    elif len(sys.argv) > 1 and sys.argv[1] == "stop":
        if os.path.exists("/tmp/metronome.pid"):
            with open("/tmp/metronome.pid", "r") as f:
                pid = int(f.read())
            os.kill(pid, signal.SIGKILL)
            os.remove("/tmp/metronome.pid")
    elif len(sys.argv) > 1 and sys.argv[1] == "fix":
       kill_metronome_procs()
  
