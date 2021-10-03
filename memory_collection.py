from definitions import *

from pygame import Rect
from memory import Memory

def memory_collection():
    memory_data = [
        (   (
                asset('doll.png'),
                200,
                15
            ),
            {
                'pos' : (550, 200),
                'spawn_box' : Rect(0, 200, 5, RES[1] - 200),
                'text' : [
                    "CLICK AND DRAG, LET THE WINDS RISE\n"
                    "TO CONTROL THE FLOW IS TO REMINISCE;\n"
                    "THE PETALS SHALL FLOW TO THE HIDDEN MEMORY\n"
                    "BRING IT FORTH TO SEE IT AGAIN\n\n"
                    "PS. PRESS ESC TO EXIT GAME\n"
                    "PRESS LEFT CTRL TO TOGGLE MOUSE INSIDE WINDOW",
                    "WHEN THE PETALS HAVE FINISHED FALLING\n"
                    "CLICK ON THE MEMORY TO LET IT GO",
                    "IT SNOWED THAT DAY\n"
                    "AND YOU WERE AS BEAUTIFUL AS EVER",
                ]
            }),
        (   (
                asset('queen_goose.png'),
                500,
                25
            ),
            {
                'pos' : (20, 20),
                'spawn_box' : Rect(200, RES[1], 150, -10),
                'text' : [
                    "\"KOI NO GOOSE QUEEN\"",
                    "HONK.",
                    "FOR YOU MY QUEEN,\n"
                    "ALL THE RAKES BELONG IN LAKES",
                ]
            }),
        (   (
                asset('rose.png'),
                600,
                25
            ),
            {
                'pos': (500, 400),
                'spawn_box': Rect(600, 0, 300, 15),
                'text' : [
                    "FLOWER DANCE",
                    "IT MAY NOT BE A REAL ONE,\n"
                    "IT MAY NOT BE THE PRETTIEST",
                    "BUT IT WILL NEVER WITHER\n"
                    "JUST LIKE MY LOVE FOR YOU"
                ]
            }
            ),
        (   (
                asset('seal.png'),
                800,
                25
            ),
            {
                'sprite_scale' : 1.2,
                'release_amount' : 200,
                'pos' : (50, 400),
                'spawn_box' : Rect(800, 150, 45, 90),
                'text' : [
                    "A WALK AT THE PARK",
                    "\"IS THAT A SEAL!?\"",
                    "ITSUMADEMO KIMI GA\nSHIAWASE NARA"
                ]
            }),
    ]
    for args, kwargs in memory_data:
        yield Memory(*args, **kwargs)
