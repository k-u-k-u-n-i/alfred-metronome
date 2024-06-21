# Metronome Workflow for Alfred 5.5

This is a simple python script to start and stop a metronome at whatever BPM speed you want.  

## Requirements
* Install Python 3.x
* Install pip
* Install pygame module `pip install pygame`
* Install psutil module `pip install psutil`
* Update script hashbang to point to your version of python
* Add an Alfred Workflow

## Install
- Clone this repo to wherever you want it to reside
- Open Alfred options > Workflows > + > Blank Workflow
  - Name: Metronome
  - Description: Play Metronome at X BPM
  - Category: Tools
  - Icon:  Drag and drop the metronome-icon.png file to the box
  - Create
- Inputs > Keyword > Drag to window
  - Keyword: met (or metro or metronome)
  - Check box for with space
  - Argument Required
  - Title: Metronome
  - Subtext: Enter BPM value, "stop", or "fix"
  - Drag and drop the metronome-icon.png file to the box
  - Save
  - Click the little tab at the right of the Keyword box and select: Actions > Run Script
    - Language dropdown: External Script
    - running instances: Concurrently  (super important step!!! Won't work without it)
    - Script file:  Type file location of metronome.py
    - Save
- Test:  `met 60` then `met stop`

## Usage
- `met <bpm-value>` = Play metronome at specific BPM - Example: `met 60`
- `met stop`        = Stop metronome playing
- `met fix`         = In case something goes wrong (metronome still playing or won't play), search for any instances of the script running, kill them all, and delete the temp file in /tmp

## Notes
* Only supports 4/4 time at the moment (you can set the 1 click file to be the same as the other click file if you don't want a 1 click)
* You'll need to update the script's hashbang to point to your python environment. 
* MP3 files to play for the clicks need to be in the same folder as the script
* You need to install pip and pygame module
* If you ever have an issue or crash and metronome is still playing, you can run:  `ps aux | grep metronome.py`   to get the process ID
* Then:  `kill -9 <proc_id>`    to stop the process
* TODO: Add additional time signature options
* TODO: Add subdivision time options and sounds 

