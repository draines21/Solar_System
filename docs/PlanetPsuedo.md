CLASS Planet:

    INITIALIZE with:
        position (x, y)
        velocity (vx, vy)
        mass
        radius
        color
        trail list

    METHOD attract(other):
        CALCULATE dx, dy
        CALCULATE distance
        IF distance is zero:
            RETURN
        CALCULATE gravitational force
        CALCULATE acceleration
        UPDATE velocity

    METHOD update_position():
        UPDATE x and y using velocity
        ADD current position to trail

    METHOD draw(screen):
        DRAW circle at (x, y)
        DRAW trail lines
