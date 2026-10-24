BEGIN PROGRAM

IMPORT pygame
IMPORT Planet class

SET window width and height

INITIALIZE pygame
CREATE window
CREATE clock

CREATE list of planets:
    - sun
    - earth
    - etc.

WHILE program is running:
    CHECK for quit event

    FOR each planet:
        FOR each other planet:
            APPLY gravitational attraction

    FOR each planet:
        UPDATE its position

    CLEAR the screen
    DRAW each planet
    UPDATE the display
    LIMIT frame rate

END PROGRAM

