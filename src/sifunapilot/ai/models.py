"""Recommended Ollama models for 8GB RAM systems."""

RECOMMENDED_MODELS = {
    "llama3.2:3b": {
        "name": "llama3.2:3b",
        "size_gb": ~2.0,
        "description": "Lightweight, fast, good for general tasks",
        "recommended": True,
    },
    "llama3.2:1b": {
        "name": "llama3.2:1b",
        "size_gb": ~0.8,
        "description": "Very lightweight, faster",
        "recommended": True,
    },
    "qwen2.5:3b": {
        "name": "qwen2.5:3b",
        "size_gb": ~2.0,
        "description": "Excellent reasoning for its size",
        "recommended": True,
    },
    "phi3.5:3.8b": {
        "name": "phi3.5:3.8b",
        "size_gb": ~2.2,
        "description": "Great instruction following",
        "recommended": True,
    },
    "smollm2:3b": {
        "name": "smollm2:3b",
        "size_gb": ~1.8,
        "description": "Efficient, good for local use",
        "recommended": True,
    },
    "llama3.1:8b": {
        "name": "llama3.1:8b",
        "size_gb": ~4.7,
        "description": "Higher quality, may use more RAM on 8GB",
        "recommended": False,
    },
}

DEFAULT_MODEL = "llama3.2:3b"
