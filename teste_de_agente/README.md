# GAE OpenRouter - Gateway Multi-Modelo
Os modelos escolhidos para esse teste são totalmente gratuitos e apenas a chave de api da própria OpenRouter foi necessária.

Houve uma preferência inicial pelos modelos "qwen" e "nvidia", mas o primeiro só aceitou uma requisição e bloqueou as seguintes e o segundo tomou um tempo muito grande para responder. "gemma" e "north" se mostraram mais receptivos pela agilidade e facilidade de comunicação.


## Requisitos
- #### Dependências
``` PowerShell
python -m pip install -r .\requirements.txt
```

- #### Keys
    criar na raiz um .env com:
```
OPENROUTER_API_KEY=sua_chave
```

## Saída
- ### 'google/gemma-4-31b-it:free'
    - "What is the meaning of life?"
    ### The "Short" Answers
    If you are looking for a quicker perspective:
    *   **The Pop Culture Answer:** According to Douglas Adams in *The Hitchhiker's Guide to the Galaxy*, the answer is **42** (though the joke is that nobody actually knows what the *question* was).
    *   **The Psychological Answer:** Meaning is often found where your **talents** meet a **need in the world**, combined with a sense of **connection** to other people.

    **Ultimately, the most empowering answer is that meaning is not something you *find*, it is something you *build*.**
- ### 'cohere/north-mini-code:free'
    The question “What is the meaning of life?” doesn’t have a single, universally accepted answer—different people find meaning in many different ways, and what counts as “meaningful” often depends on personal values, cultural background, and life circumstances.

    ### Common Themes People Use to Find Meaning

    | Perspective | Core Idea | Typical Sources of Meaning |
    |------------|-----------|---------------------------|
    | **Religious / Spiritual** | Life’s purpose is tied to a higher power, divine plan, or cosmic order. | Faith, devotion, service to others, following sacred texts, rituals, enlightenment. |
    | **Philosophical** | Meaning is something we create through reason, ethics, or existential choice. | Building lasting relationships, contributing to art, knowledge, justice, or personal excellence. |
    | **Existentialist** | There is no pre‑ordained purpose; we must create it ourselves. | Authentic choices, taking responsibility, embracing freedom, confronting absurdity. |
    | **Humanistic / Secular** | Meaning emerges from human connections, personal growth, and contributing to the well‑being of others. | Love, friendship, creativity, mentorship, helping others, pursuing hobbies. |
    | **Scientific / Naturalistic** | Life is a product of evolution; meaning can be found in understanding the natural world. | Curiosity, discovery, stewardship of the environment, curiosity‑driven learning. |
    | **Practical / Everyday** | Meaning is often found in routine, responsibilities, and simple experiences. | Caring for family, work you enjoy, hobbies, community involvement, moments of presence. |

    ### A Few Thought Experiments

    1. **The “Legacy” Question** – What would you want future generations to remember about you?  
    *Focus:* impact, relationships, ideas.

    2. **The “If I Were Dying” Question** – If you had one day left to live, what would you want to have done or experienced?  
    *Focus:* priorities, passions, gratitude.

    3. **The “What Would I Teach?” Question** – If you could teach one lesson to the next generation, what would it be?  
    *Focus:* values, lessons learned.

    ### Practical Ways to Explore Your Own Meaning
    ...
    3. **Contribution** – helping others, leaving a positive impact.  
    4. **Presence** – being mindful and appreciating the present moment.