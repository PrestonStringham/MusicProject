MusicProject

This project concerns mapping digits to notes of piano keys in MIDI. For some sequence of digits, Musicify maps those digits to any key in any octave using a variety of different "extensions" as there are more digits than notes in a key. This allows one to create infinite melodies using transcendental numbers like pi. You can theoretically make a song of infinite length and varying melodies using different transcendental numbers.

Consider digits 0-9 and imagine a piano. Pick any 10 keys on the piano and assign it a number. Then, consider a sequence of numbers like, 3.1415... We can play these digits in order and produce some music. Now, computers have a file type for storing music note data called MIDI. Basically, it already has assigned keys on the piano to digits in ascending order. That is, the lowest note on the keyboard, in MIDI, is 0. Then, the next is 1 and so on.

So, we know that 0-9 are already MIDI notes... So, we are done...

But... We can be more creative than that. You see, the digits 0-9 are already in what we call a "chromatic" scale. An example of a chromatic scale is C, C#, D, D#, E, F, F#, G, G#, A, A#, B, C. The notes are right next to each other. Some more observant readers will also notice that there were 12 notes in a chromatic scale(Excluding the top C in our example). So, we couldn't even map digits to the chromatic scale anyway, but we could cover some of it as follows

0->C, 1->C#, 2-> D, ..., 9 -> A

The results of this mapping... well... It doesn't sound very pleasant. Believe me, I tried. So what about converting this to a more pleasant sounding "scale." A scale is just a sequence of notes that are more pleasing to the ear. You can be more detailed about what a scale is, talking about frequencies and distance between notes, but that is a simple way to put it. An example of a scale would be C, D, E, F, G, A, B, C. This is the most basic scale. We can also shift the starting note of that scale to another note. Say, D, E, F, G, A, B, C, D. This is called changing the "Mode" of the scale. 

I briefly mention "octaves." If you look on the piano closely, you will see the same pattern of white and black keys. For example, you should see two groups of black keys, one group of two keys (C# and D#) and one group of three black keys (F#, G#, and A#). This pattern repeats across the keys. If you go from one group of two keys (C# and D#) and go up the keyboard or down, you are now looking at a new octave. The notes are called exactly the same names, but in music notation, we denote these octaves with a number following the note. Like C0, F#3, G5, etc.


So, the purpose of this project is to allow one to create melodies using digits in ANY key and ANY mode in ANY octave. It just generalizes the entire process.

But we can go further.

What about the note lengths?

We can use ANOTHER string of digits to compute the length of the notes. 

So, I can use pi for my melody and eulers number for my note lenghts. My code just strings together the notes and their respective lenghts.

How does it REALLY work?

First, it starts by using the fact that 0-9 are ALREADY MIDI notes. It then converts it to a C Major scale(The most basic one described in the scale section of this description). Then we calculate the numbers for a mode change, but we don't actually shift the notes yet. Then, it calculates the amount of shift for the notes to be in the right key. For example, if the key is set to G Major, it moves the F number and adds one to it, making it F# which turns the scale into G Major. Then we add all of the shift numbers to each digits and then we have finally mapped the digit to the note on the keyboard. In addition, I made it so it goes to one of the higher octaves, so it can easily be heard as 0 - 9 would be mapped to some low notes like C0.

That's it! 
