# What is the Answer to the Great Question of Life, the Universe, and Everything?
val = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

# the answer should be 42 or forty-two or forty two
match val:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")

