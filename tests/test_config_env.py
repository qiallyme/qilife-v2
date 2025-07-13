# tests/test_config_env.py
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.config import env, rules, settings

def test_get_env_keys():
    print("🔍 ENV keys:")
    config = env.get_env()
    for k, v in config.items():
        print(f"   {k}: {v or '[MISSING]'}")

def test_update_env_key():
    print("\n✏️ Testing update_env()")
    env.update_env("TEST_KEY", "test_value")
    assert env.get_value("TEST_KEY") == "test_value"
    print("✅ TEST_KEY was set correctly.")

def test_rules_load():
    print("\n📂 Loaded folder rules:")
    r = rules.load_rules()
    for drive, meta in r.get("drives", {}).items():
        print(f"   Drive {drive} → {meta['name']}")

def test_settings_access():
    print("\n🔧 ENV via settings:")
    print(f"   OPENAI_API_KEY: {settings.ENV.get('OPENAI_API_KEY', '[MISSING]')}")

    print("📁 RULE tags:")
    print(f"   Available tags: {list(settings.RULES.get('tags', {}).keys())}")

if __name__ == "__main__":
    print("🧪 Running config tests...\n")
    test_get_env_keys()
    test_update_env_key()
    test_rules_load()
    test_settings_access()
