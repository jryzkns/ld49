from definitions import *

from memory import Memory

def memory_collection():
    memory_data = [
        (   (   
                asset('doll.png'),
                200, 
                15
            ), 
            {
                'text' : [
                    "CLICK AND DRAG, LET THE WINDS ARISE\n"
                    "TO CONTROL THE FLOW IS TO REMINISCE;\n"
                    "THE PETALS SHALL FLOW TO THE HIDDEN MEMORY\n"
                    "BRING IT TO LIGHT.\n\n"
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
                300, 
                25
            ), 
            {
                'text' : [
                    "\"KOI NO GOOSE QUEEN\"",
                    "HONK.",
                    "FOR YOU MY QUEEN,\n"
                    "ALL THE RAKES BELONG IN LAKES",
                ]
            }),
        (   (
                asset('seal.png'), 
                500, 
                25
            ), 
            {
                'sprite_scale' : 1.2, 
                'release_amount' : 200,
                'text' : [
                    "A WALK AT THE PARK",
                    "\"IS THAT A SEAL?\"",
                    "ITSUMADEMO KIMI GA\nSHIAWASE NARA"
                ]
            }),
    ]
    for args, kwargs in memory_data:
        yield Memory(*args, **kwargs)
