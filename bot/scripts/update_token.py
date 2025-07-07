from pathlib import Path
import yaml  # pip install pyyaml, если надо

def main():
    script_dir = Path(__file__).parent
    root_dir = script_dir.parent

    answers_path = script_dir / ".copier-answers.yml"
    env_path = root_dir / ".env"

    # Читаем .copier-answers.yml
    with answers_path.open() as f:
        answers = yaml.safe_load(f)

    token_value = answers.get('token')
    if not token_value:
        print("Token not found in .copier-answers.yml")
        return

    # Читаем .env (если нет, создаём пустой список)
    if env_path.exists():
        env_lines = env_path.read_text().splitlines()
    else:
        env_lines = []

    new_lines = []
    token_updated = False

    for line in env_lines:
        if line.startswith("TOKEN="):
            new_lines.append(f"TOKEN={token_value}")
            token_updated = True
        else:
            new_lines.append(line)

    if not token_updated:
        new_lines.append(f"TOKEN={token_value}")

    env_path.write_text("\n".join(new_lines))
    print(f".env updated with TOKEN={token_value}")

if __name__ == "__main__":
    main()
