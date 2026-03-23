
import json

CURRICULUM_FILE = "curriculum.json"

def load_curriculum():
    with open(CURRICULUM_FILE) as f:
        return json.load(f)

def get_lessons(level):

    curriculum = load_curriculum()

    return curriculum["levels"].get(str(level), [])
