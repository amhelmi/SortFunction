# FDE Technical Screen
Python file containing sort function and test cases for robotic package sorting. 

The function sorts packages based on the following criteria and returns a string with the correct sort string:

- A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
- A package is **heavy** when its mass is greater or equal to 20 kg
- Else it is a standard package

String returns as follows:
**STANDARD**: not bulky or heavy
- **SPECIAL**: either heavy or bulky
- **REJECTED**: both heavy
- **ERROR**: incorrect input

Limitation: Does not test for incorrect input types. Assumes input is numeric.
