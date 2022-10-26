import os
import re
import random

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from rich.console import Console

# --- Constants --- #

app = APIRouter(tags=["Sentence Generator"])
console = Console()

# --- Routes --- #

@app.get("/generate")
async def main(sentence: str) -> dict:
    new = await generate_sentence(sentence)

# --- Helpers --- #

async def generate_sentence(sentence):
    file = random.choice(os.listdir("words"))
    with open("words/"+file, "r") as f:
        words_list = f.readlines()[::2]

    sentence_list = sentence.split()
    for word in sentence_list:
        if re.search("<(noun|verb-(sp|pc|pp|ppc|spa|pac|pap|papc|sf|fc|fp|fpc)|adjective)>", word):
            pass
    
    return sentence_list


    

# -------------- #