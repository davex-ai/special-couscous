import random
import datetime
import json

# ---------- ASCII ART ----------
ascii_shapes = [
"""
   /\\
  /  \\
 /____\\
""",
"""
 (•_•)
 ( •_•)>⌐■-■
 (⌐■_■)
""",
"""
  _____
 /     \\
|  O O  |
|   ^   |
| \\___/ |
 \\_____/
"""
]

def generate_ascii():
    with open("ascii/art.txt", "a") as f:
        f.write(f"\n# {datetime.datetime.now()}\n")
        f.write(random.choice(ascii_shapes))


# ---------- TRAINING LOG ----------
def generate_training_log():
    loss = random.random()
    acc = random.random()

    with open("ml/training_logs.txt", "a") as f:
        f.write(
            f"{datetime.datetime.now()} | loss={loss:.4f} | acc={acc:.4f}\n"
        )


# ---------- RANDOM NETWORK ----------
def generate_network():
    layers = random.randint(2, 6)

    network = {
        "layers": [
            {
                "neurons": random.randint(4, 128),
                "activation": random.choice(["relu", "tanh", "sigmoid"])
            }
            for _ in range(layers)
        ]
    }

    with open("ml/random_networks.json", "a") as f:
        f.write(json.dumps(network) + "\n")


# ---------- RANDOM CODE ----------
languages = [
    "python", "javascript", "java", "c++", "ruby", 
    "go", "rust", "php", "swift", "kotlin", 
    "typescript", "c#", "dart", "scala"
]

def generate_code():
    lang = random.choice(languages)

    snippets = {
        "python": "print('hello chaos world')",
        "javascript": "console.log('chaos')",
        "java": "System.out.println(\"chaos\");",
        "c++": 'std::cout << "chaos";',
        "ruby": 'puts "chaos"',
        "go": 'fmt.Println("chaos")',
        "rust": 'println!("chaos");',
        "php": 'echo "chaos";',
        "swift": 'print("chaos")',
        "kotlin": 'println("chaos")',
        "typescript": 'console.log("chaos");',
        "c#": 'Console.WriteLine("chaos");',
        "dart": 'print("chaos");',
        "scala": 'println("chaos")'
    }

    with open("code/random_snippets.txt", "a") as f:
        f.write(f"\n# {lang}\n{snippets[lang]}\n")


generate_ascii()
generate_training_log()
generate_network()
generate_code()