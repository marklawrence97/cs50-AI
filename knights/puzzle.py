from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(AKnave, Not(AKnight)),
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(AKnave, Not(AKnight)),
    Biconditional(BKnight, Not(BKnave)),
    Biconditional(BKnave, Not(BKnight)),
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(AKnave, Not(AKnight)),
    Biconditional(BKnight, Not(BKnave)),
    Biconditional(BKnave, Not(BKnight)),
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Implication(BKnight, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Implication(BKnave, Or(And(AKnight, BKnight), And(AKnave, BKnave)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(AKnave, Not(AKnight)),
    Not(And(AKnight, AKnave)),

    Or(BKnight, BKnave),
    Biconditional(BKnight, Not(BKnave)),
    Biconditional(BKnave, Not(BKnight)),
    Not(And(BKnight, BKnave)),


    Or(CKnight, CKnave),
    Biconditional(CKnight, Not(CKnave)),
    Biconditional(CKnave, Not(CKnight)),
    Not(And(CKnight, CKnave)),

    # A Tells the truth
    Implication(AKnight, Or(AKnight, AKnave)),
    # A Tells a lie
    Implication(AKnave, Or(Not(AKnight), Not(AKnave))),

    # If B tells truth
    Implication(BKnight, CKnave),
    # B tells the truth implies either A is a knight telling the truth or a knave telling a lie.
    Implication(BKnight, Or(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))),

    # If B Lies
    Implication(BKnave, Or(Not(Implication(AKnight, AKnave)), Not(Implication(AKnave, Not(AKnave))))),
    Implication(BKnave, Not(CKnave)),

    # If C Tells the truth
    Implication(CKnight, AKnight),

    # If C tells a lie
    Implication(CKnave, Not(AKnight)),
    BKnave
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
