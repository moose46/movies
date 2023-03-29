from pathlib import Path

print(Path.cwd())

print(Path.cwd() / "moviesite")

moviesite = Path.cwd() / "moviesite" / "moviesite"

print(f"{moviesite} {moviesite.is_dir()}")

cnt = 0
for s in moviesite.glob("s*.py"):
    if s.exists():
        cnt += 1

assert cnt > 0
