# Hirst-Painting-Simulator
This program is simulating Hirst's "Spots" painting.
This is the project created on my 18th day of program course.

## What does it do?
- First of all, the .png used in this file is a painting made for the video game "Nier" (owned by Square-Enix (a.k.a not mine)).
  - This image was used as the tones of color were something that talk to me. However any imagine would have made the trick.
- The program is using the "colorgram" module to extract a set amount of color (12 in this code) from the image I selected.
- The program will then draw spots, to mimic a piece of art from Hirst called "Spots", using the colors extracted earlier.
  - Note that the program needs a moment to extract the colors. I wanted this process to be randomized everytime and not have a set of color pre-extracted
- The colors for the spots are chosen randomly among the extracted ones, hence adding randomness to the final output.
  - Each itteration will be different.

![image](https://github.com/Rokobolo/Hirst-Painting-Simulator/assets/139471568/215d5462-bdbf-49c9-897e-e34fbe96b4ef)

## What is the goal?
- The goal was to play with the "Turtle" module.
- The idea here is that I had to dig the [documentation](https://docs.python.org/3/library/turtle.html#turtle.dot) and learn from it to create this project.
  - Making sure I am capable of tackling a challenge with only the proper doc handled.
- Classes where not used in this project as it was very much not necessary, thought it could have been done.

## How to use?
- Would you wish to try the program on your own, but with another picture and set of color you'd only need to edit one line:
  - _Line 40_ needs two arguments to work. The name of the file and the amount of color you want to extract.
  - Currently set on "nier.png" and "12", you'd only need to edit these to match your image name and the amount of desired color to try it out with another image.

 ![image](https://github.com/Rokobolo/Hirst-Painting-Simulator/assets/139471568/47dad177-9797-4855-a26c-d53fa88a5582)

