---
hide:
  - navigation
---

# Note-generating metronome with Python

Metronome's and random note generators are useful for many reasons, but separately, they are quite limited.
In this article we'll use Python to combine these two functions to create a custom metronome that generates notes for your practice sessions or curiosity.

If you want to practice finding note positions on your guitar, or keyboard, with a little pressure from a metronome, There are plenty of resources on and offline that can help with these activities. However, they are usually separated - A metronome, and a random note generator. In this article we'll use Python to combine both of those into one program you can use.


## Prerequisites
You should have Python and a text editor of your choice installed - This article assumes you are using VSCode, but the core ideas remain the same for any other editor.

Some experience with Python is beneficial, but it isn't necessary.

## Setting up
Open up your text editor, create a new `notes.py` file and open it.
We'll now import the necessary modules. At the bottom of your editor window should be a terminal - Press `` ctrl+shift+` `` if it isn't there already.
Type the following lines into the terminal:
```
pip install simpleaudio
pip install numpy
```
- `simpleaudio` is the package we'll use to play our sounds, and `numpy` is the package we'll use to generate audible notes.

Now let's import these packages onto our Python file by typing in the following lines at the top of our `notes.py` file:
```
import simpleaudio
import numpy
import random
import time
```
- We import the extra random and time modules to choose random notes from a list and time our metronome.

## Generating note frequencies
Using a bottom up approach, let's start by creating our note dictionary.
For this, we'll create a Python dictionary called `notes`. At every index in the dictionary is a list that contains a note and it's frequency. 
Type the following in your Python file:
```
# Note frequencies
notes = {
    1: ["A" ,0],
    2: ["A#",0],
    3: ["B" ,0],
    4: ["C" ,0],
    5: ["C#",0],
    6: ["D" ,0],
    7: ["D#",0],
    8: ["E" ,0],
    9: ["F" ,0],
    10:["F#",0],
    11:["G" ,0],
    12:["G#",0],
}

# Generate note frequencies
for i,note in enumerate(notes.keys()):
    notes[note] = round(440 * 2 ** (i / 12), 1)
    print(notes[i])
```
- We initialize our dictionary with the 12 notes, but with 0 as the frequency values. This is so that we can then generate the note frequencies using a loop.
- Using 440 Hz as the base frequency, this loop calculates the frequency of each note based on the mathematical interval between them. We then update each note's frequency in our dictionary, printing it to our terminal as we go along.  

If you run the code using `` ctrl + f5 `` or press the green run button on the top right of your window, 
you should have the correct notes and frequencies displayed like this on the terminal:
```
['A', 440.0]
['A#', 466.2]
['B', 493.9]
['C', 523.3]
['C#', 554.4]
['D', 587.3]
['D#', 622.3]
['E', 659.3]
['F', 698.5]
['F#', 740.0]
['G', 784.0]
['G#', 830.6]
```
You can remove the `print(notes[i])` line if the correct notes and frequencies are being printed.

## Playing the notes
Now, let's create the note playing function.
For this we'll use `numpy` and `simpleaudio`. Type the following function into your Python file:
```
def play_note(note, octave=4):
    if octave >= 8:
        octave = 8
    frequency = note[1] * 2 ** (((octave*12)-48) / 12) 
    fs = 44100  # 44100 samples per second
    seconds = 1 # Note duration - integer

    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = numpy.linspace(0, seconds, seconds * fs, False)

    # Generate a sine wave from the frequency
    note = numpy.sin(frequency * t * 2 * numpy.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / numpy.max(numpy.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(numpy.int16)

    # Start playback
    play_obj = simpleaudio.play_buffer(audio, 1, 2, fs)

# Remove this after testing is done
play_note(notes[1], octave = 4)
time.sleep(1)
```
- Here, we create a function that takes two arguments: The list (containing the note name and frequency), as well as an octave number - which is used when calculating the note's new frequency, giving us freedom to play notes across octaves.  
- We then use various `numpy` functions to ultimately generate an audible note from the frequency we supply. `simpleaudio` then plays this generated note for one full second. 

If you run the program now, you should hear an A middle tone being played on your speakers.

## Metronome
One thing to keep in mind with Python, is that your code doesn't directly access your hardware, but does so through a lot of layers. So our metronome might not be fully accurate and will drift after some time. The usual approach to creating a metronome is to use Python's built-in `time.sleep()` method. However, since this method varies significantly depending on what other tasks your computer processor could be running at that moment, we'll use a slightly different approach so our metronome can have relatively more accuracy.    

Now, let's build our metronome - You will need to download these two metronome sound files and place them in the same folder as your `notes.py` file: 

* [metronome.wav](../assets/note-generator-article/metronome.wav)
* [metronomeup.wav](../assets/note-generator-article/metronomeup.wav)

The only difference between the two is that one will be played when stressing the beginning of a new beat.

Add this code onto your Python file:

```python
def metronome(bpm):
    print(float(bpm), "bpm")
    delay = 60/bpm
    count = 0
    beat = 0
    
    mode = 4
    multiple = 8

    while True:
        wait(delay)
        
        # increment count after every wait and beat after ever 4 counts 
        count += 1
        if count > mode:
            count = 1
            beat += 1
        
        # set metronome audio according to beat count
        wave_obj = simpleaudio.WaveObject.from_wave_file('metronome.wav')
        if count == 1:
            wave_obj = simpleaudio.WaveObject.from_wave_file('metronomeup.wav')
        
        # play metronome audio
        play_obj = wave_obj.play()
        play_obj

        # Remove this after testing
        print(beat, count)
```
Let's break this code down.
- We create a metronome function that takes in a bpm number. This function begins with defining the time delay between each beat per minute, and initializing the metronome count and beat. We'll look at the `mode` and `multiple` variables in the upcoming sections.
- We then create an infinite loop which waits for the specified delay time at every iteration before executing the rest of the code inside the loop. You will notice that we use a `wait()` function - This is another function that we will code separately after this metronome function. 
- The second section in our loop increases the count by 1 after every delay, and after every 4 counts (The mode variable), resets back to 1. The beat number is also increased by 1 after every 4 counts. You can change the mode variable from 4 to other numbers, like 3 or 6, to change the metronome's rhythm.
- With our counting system in place, we use `simpleaudio` to prepare our metronome sound file. We select a different metronome sound whenever the count is on 1 to stress the start of a new beat.
- The final section in our loop plays the selected sound file. In this case, `simpleaudio` plays the sound on a separate thread from the main program thread so the main program can continue running.

Now, let's create the function that works as the delay between every tick of the metronome.
Copy this code onto your file:
```
def wait(delay):
    end_time = time.time() + delay
    while end_time > time.time():
        continue

#Remove this after testing
metronome(95)
```
- This function takes in the delay time we defined in the previous function.
- We create a variable called `end_time` which is defined by adding the number of seconds that have passed since *epoch and the delay time for our bpm.
- We then create a loop that continues to run (or in other words, wait) until the epoch time is greater than the `end_time` we've defined. Once this loop has finished, our wait function is terminated and the program continues.


*`"The epoch is the point where the time starts, and is platform dependent. For Unix, the epoch is January 1, 1970, 00:00:00 (UTC). To find out what the epoch is on a given platform, look at time.gmtime(0)."`

*`"...various real-time functions may be less than suggested by the units in which their value or argument is expressed. E.g. on most Unix systems, the clock “ticks” only 50 or 100 times a second."`

Keep in mind this method may not be fully accurate as stated in the overview of this section.
Run the code and you should hear your metronome as well as the beat counter printing on the console like this:
```
95.0 bpm
0 1
0 2
0 3
0 4
1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
...
```
Don't forget to remove the `print(beat, count)` and `metronome(95)` lines if you don't need to see the output from them.

You can use the shortcut ``ctrl+c`` on the terminal, or click on the red stop button near the top right of the screen to stop the program.

## Putting it together
Now with the metronome and note playing functions completed, let's combine them to complete this program.
Add the following function to your file:
```
def generate_notes(sound = True):
    random_note = random.choice(list(notes.values()))
    print("\n\nFind: ",random_note[0])
    if sound == True:
        play_note(random_note, octave = 3)
```
- This function chooses a random note from our notes dictionary. We combine all the values in our dictionary into a list, and then use `random.choice()` to select a random note.
- We then print a message to the console, indicating which note has been selected.
- Since we create this function to take in a `sound` variable which can be True or False. We use the variable to determine whether or not the program should play the note sound. If the note is played, we set it to play at the third octave. Higher octaves can get a bit uncomfortable to hear on certain speakers

As it is, the function we just created is not being called anywhere, so it isn't working yet. Let's go back to our metronome function and add the code to call this function.
Add the following code underneath the `# Play metronome audio` section of your metronome function:
```
# Generate notes()
if beat % 8 == 0 and count == 4:
    generate_notes()
```
Your code should look something like this:
```
        # Play metronome audio
        play_obj = wave_obj.play()
        play_obj

        # Generate notes()
        if beat % multiple == 0 and count == 1:
            generate_notes()
```
- We call the `generate_notes()` function only when the beat number is a multiple of 8 (the variable we defined earlier), and when the count is at 1. This value of 8 will give you enough time to find the notes on your instrument. Feel free to adjust this to suit your needs. Lower numbers will generate notes more frequently (Values lower than one will not work well).

You can now run the code by adding this line to your file:
```
metronome(90)
```

## Conclusion
You could use this to practice finding notes as mentioned, or use it to generate root notes for you to play on top of.
If you have more coding experience, perhaps you could extend the functionality to include scales, midi input, or anything else that is possible.

In this tutorial you have learned how to make a metronome system and a random note generator. We also looked at using simpleaudio to play external sounds or generate notes with the help of numpy. I hope this has in some way enhanced your practice sessions with your instrument.

