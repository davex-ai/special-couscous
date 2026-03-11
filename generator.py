import random
import datetime
import json
import os
import numpy as np

now = datetime.datetime.now()

hour = datetime.datetime.now().hour

if hour != 0:
    if random.random() < 0.1:
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
r"""
   /\\
  /  \\
 /____\\
""",
r"""
 (•_•)
 ( •_•)>⌐■-■
 (⌐■_■)
""",
r"""
  _____
 /     \\
|  O O  |
|   ^   |
| \\___/ |
 \\_____/

  """,
    r"""
       _      
      / \     
     /   \    
    /_____\   

    |  _  |   
    | | | |   
    |_|_|_|   
    """,

    r"""
      _  _

     | || | _
     | || || |
     | || || |
      \_  _/
        ||
        ||
    """,

    r"""
      [o u o]
      /|___|\\
       /   \\
    """,
    
    r"""
     _@/  _
    (   \/ )
     \____/
""",
r"""
     _

    | |
    | |
    | |
    |_|
    (_)
""",
r"""
      /|
     / |
    /  |
   /___|
  (_____)
""",
r"""
    ┬─┬ノ( º _ ºノ)

    (╯°□°）╯︵ ┻━┻
""",
r"""
     /\___/\
    (  o o  )
    (  =^=  )
     (______)
""",
r"""
     _______

    |.-----.|
    ||     ||
    ||_____||
    '-------'
""",
r"""
      _____
     /     \

    | () () |
     \  ^  /
      |||||
"""
]

def generate_ascii():
    with open("ascii/art.txt", "a") as f:
        f.write(f"\n# {now}\n")
        f.write(random.choice(ascii_shapes))

def weight_heatmap():

    path = "neural_networks/weights.npy"
    if not os.path.exists(path):
        return ""

    weights = np.load(path)

    chars = " .:-=+*#%@"

    heatmap = ""

    for row in weights:
        for v in row:
            idx = int((v + 3) / 6 * (len(chars)-1))
            idx = max(0, min(idx, len(chars)-1))
            heatmap += chars[idx]
        heatmap += "\n"

    return heatmap


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

    try:
        if os.path.exists(path) and os.path.getsize(path) > 0:
            weights = np.load(path)
        else:
            raise ValueError("weights file empty")

    except Exception:
        print("Reinitializing weights")
        weights = np.random.randn(20,20)

    noise = np.random.normal(0,0.1,weights.shape)
    weights += noise

    np.save(path, weights, allow_pickle=False)

    loss = np.mean(weights**2)
    acc = random.random()

    with open("ml/training_logs.txt","a") as f:
        f.write(f"{now} | loss={loss:.4f} | acc={acc:.4f}\n")


# ---------- DASHBOARD ----------
def update_dashboard():
    latest_ascii = ""

    if os.path.exists("ascii/art.txt"):
        with open("ascii/art.txt") as f:
            text = f.read().strip()
            blocks = text.split("# ")
            latest_ascii = blocks[-1] if len(blocks) > 1 else text

    def count_lines(path, pattern=None):
        if not os.path.exists(path):
            return 0
        with open(path) as f:
            text = f.read()
        return text.count(pattern) if pattern else len(text.splitlines())

    algo_count = count_lines("algorithms/algorithms.py", "def algo_")
    formula_count = count_lines("math/formulas.md", "f(")
    dataset_rows = count_lines("datasets/data.csv")
    ascii_art = count_lines("ascii/art.txt", "#")
    ascii_graphs = count_lines("ascii/graphs.txt", "#")
    snippets = count_lines("code/random_snippets.txt", "#")
    architectures = count_lines("neural_networks/architectures.json")
    training_logs = count_lines("ml/training_logs.txt")

    dashboard = f"""
# 🔥 Hephaestus Oracle

An autonomous forge generating computer science artifacts.

---

## 📊 Artifact Stats

| Artifact | Count |
|--------|------|
| Algorithms forged | {algo_count} |
| Math formulas discovered | {formula_count} |
| Dataset rows generated | {dataset_rows} |
| ASCII artworks | {ascii_art} |
| ASCII graphs | {ascii_graphs} |
| Code snippets | {snippets} |
| Neural architectures | {architectures} |
| Training logs | {training_logs} |

---

## ⚙️ System

- Procedural artifact generator
- Autonomous GitHub workflow
- Neural weight evolution engine

## 🎨 Latest ASCII Artifact


{latest_ascii}


---

## 🧠 Neural Weight Heatmap


{weight_heatmap()}


---

## ⚙️ System

- Procedural artifact generator
- Autonomous GitHub workflow
- Neural weight evolution engine

Last oracle cycle: **{now}**

"""

    with open("README.md","w") as f:
        f.write(dashboard)


# ---------- RUN EVERYTHING ----------
generators = [
    generate_ascii,
    generate_ascii_graph,
    generate_dataset,
    generate_formula,
    generate_algorithm,
    generate_code,
    generate_architecture,
    evolve_weights
]

for g in random.sample(generators, random.randint(3,6)):
    g()

update_dashboard()
