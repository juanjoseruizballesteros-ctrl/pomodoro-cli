#!/usr/bin/env python3
"""Temporizador Pomodoro minimalista para la terminal."""
import argparse
import time


def countdown(minutes: int, label: str) -> None:
    total = minutes * 60
    for remaining in range(total, 0, -1):
        m, s = divmod(remaining, 60)
        print(f"\r{label}: {m:02d}:{s:02d}", end="", flush=True)
        time.sleep(1)
    print(f"\r{label}: terminado!   \a")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--work", type=int, default=25, help="minutos de trabajo")
    p.add_argument("--rest", type=int, default=5, help="minutos de descanso")
    p.add_argument("--cycles", type=int, default=4, help="numero de ciclos")
    a = p.parse_args()
    for i in range(1, a.cycles + 1):
        countdown(a.work, f"Ciclo {i}/{a.cycles} trabajo")
        if i < a.cycles:
            countdown(a.rest, f"Ciclo {i}/{a.cycles} descanso")


if __name__ == "__main__":
    main()
