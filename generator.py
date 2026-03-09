import random
import datetime
import json
import os
import numpy as np

now = datetime.datetime.now()

hour = datetime.datetime.now().hour

if hour != 0:
    if random.random() < 0.6:
        print("Skipping generation this run.")
        exit()

dirs = [
    "algorithms",
    "code",
    "neural_networks",
    "datasets",
    "math",
    "ascii",
    "ml"
]

for d in dirs:
    os.makedirs(d, exist_ok=True)


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
        f.write(f"\n# {now}\n")
        f.write(random.choice(ascii_shapes))


# ---------- ASCII GRAPH ----------
def generate_ascii_graph():

    width = 30
    values = [random.randint(0,10) for _ in range(width)]

    graph = ""

    for y in reversed(range(11)):
        for x in values:
            graph += "█" if x >= y else " "
        graph += "\n"

    with open("ascii/graphs.txt","a") as f:
        f.write(f"\n# {now}\n")
        f.write(graph)


# ---------- RANDOM DATASET ----------
def generate_dataset():

    rows = random.randint(5,20)

    with open("datasets/data.csv","a") as f:
        for _ in range(rows):
            x = random.random()
            y = random.random()
            label = 1 if x + y > 1 else 0
            f.write(f"{x},{y},{label}\n")


# ---------- RANDOM MATH FORMULA ----------
def generate_formula():

    variables = ["x","y","z"]
    ops = ["+","-","*","/"]

    v = random.choice(variables)
    expr = f"{v} {random.choice(ops)} {random.randint(1,10)}"

    formula = f"f({v}) = {expr}"

    with open("math/formulas.md","a") as f:
        f.write(f"\n{formula}\n")


# ---------- RANDOM ALGORITHM ----------
def generate_algorithm():

    algo_id = random.randint(10000,99999)

    template = f"""
def algo_{algo_id}(arr):
    \"\"\"Random generated algorithm\"\"\"
    result = 0
    for i in range(len(arr)):
        if arr[i] % {random.randint(2,5)} == 0:
            result += arr[i]
    return result
"""

    with open("algorithms/algorithms.py","a") as f:
        f.write(template)


# ---------- RANDOM CODE SNIPPET ----------
languages = {
    "python": "print('chaos')",
    "javascript": "console.log('chaos')",
    "java": 'System.out.println("chaos");',
    "c++": 'std::cout << "chaos";',
    "rust": 'println!("chaos");',
    "go": 'fmt.Println("chaos")',
}

def generate_code():

    lang = random.choice(list(languages.keys()))

    with open("code/random_snippets.txt","a") as f:
        f.write(f"\n# {lang}\n{languages[lang]}\n")


# ---------- RANDOM NEURAL ARCHITECTURE ----------
def generate_architecture():

    layers = random.randint(2,6)

    arch = {
        "timestamp": str(now),
        "layers":[
            {
                "neurons": random.randint(4,64),
                "activation": random.choice(["relu","tanh","sigmoid"])
            }
            for _ in range(layers)
        ]
    }

    with open("neural_networks/architectures.json","a") as f:
        f.write(json.dumps(arch) + "\n")


# ---------- EVOLVING NEURAL NETWORK ----------
def evolve_weights():

    path = "neural_networks/weights.npy"

    if os.path.exists(path):
        weights = np.load(path)
    else:
        weights = np.random.randn(10,10)

    noise = np.random.normal(0,0.01,weights.shape)

    weights += noise

    np.save(path,weights)

    loss = np.mean(weights**2)
    acc = random.random()

    with open("ml/training_logs.txt","a") as f:
        f.write(f"{now} | loss={loss:.4f} | acc={acc:.4f}\n")


# ---------- DASHBOARD ----------
def update_dashboard():

    algo_count = 0
    if os.path.exists("algorithms/algorithms.py"):
        with open("algorithms/algorithms.py") as f:
            algo_count = f.read().count("def algo_")

    formula_count = 0
    if os.path.exists("math/formulas.md"):
        with open("math/formulas.md") as f:
            formula_count = f.read().count("f(")

    dashboard = f"""
# Procedural Computer Science

Daily generated computer science artifacts.

## Stats

Algorithms generated: {algo_count}
Math formulas generated: {formula_count}

Last update: {now}
"""

    with open("README.md","w") as f:
        f.write(dashboard)


# ---------- RUN EVERYTHING ----------
generate_ascii()
generate_ascii_graph()
generate_dataset()
generate_formula()
generate_algorithm()
generate_code()
generate_architecture()
evolve_weights()
update_dashboard()