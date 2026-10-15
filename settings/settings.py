import os
import tomllib

# Default settings
IA_NAME = "gemini-3.5-flash-lite"
VOICE_PATH = "model/tts/glados/fr_FR-glados-medium.onnx"
MODEL_PATH = "model/vosk/vosk-model-small-fr/vosk-model-small-fr-0.22"
SAMPLE_RATE = 16000
BLOCK_SIZE = 4000

# Path for config file
CONFIG_FILE = os.path.expanduser("~/tranquillity/settings.toml")

# Secrets settings
GEMINI_API_KEY = ""
NEWAPI_KEY = ""
DISCORD_API_KEY = ""
SPOTIFY_TOKEN_PUBLIC = ""
SPOTIFY_TOKEN_PRIVATE = ""

if os.path.exists(CONFIG_FILE):
    try:
        with open(CONFIG_FILE, "rb") as f:
            data = tomllib.load(f)
        IA_NAME = data["ai"]["name"]
        VOICE_PATH = data["voice"]["voice_path"]
        MODEL_PATH = data["voice"]["model_path"]
        GEMINI_API_KEY = data["secrets"]["gemini_api_key"]
        NEWAPI_KEY = data["secrets"]["newsapi_key"] or None
        DISCORD_API_KEY = data["secrets"]["discord_api_key"] or None
        SPOTIFY_TOKEN_PUBLIC = data["secrets"]["spotify_token_public"] or None
        SPOTIFY_TOKEN_PRIVATE = data["secrets"]["spotify_token_private"] or None
    except Exception as e:
        print(f"Error with config file : {e}")
        pass
else:
    print("configuration file not load")