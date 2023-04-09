import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_PYTHON = "Integers Booleans Dictionary Strings List Tuples Sets Floats"
def unknown():
    response = ['Could you please rephrase that?',
                "...",
                "Sounds about right",
                "What does that mean?"][random.randrange(4)]
    return response