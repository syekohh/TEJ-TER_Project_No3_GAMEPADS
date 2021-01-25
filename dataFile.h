// define pin constants
#define downArrow 10
#define upArrow 11
#define mouseLeftClick 12

// define unique values to be sent to the serial for each different button press
#define upVal "99"
#define downVal "97"
#define leftClickVal "95"

// define the "x" and "y" axis analog pins
/*
* please note that these pins are inverted in the joystick due
* to the orientation in which the joystick is meant to be held
* and used by the user - Makes more sense to be held this way.
*/
#define yInput A0
#define xInput A1