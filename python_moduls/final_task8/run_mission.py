import argparse
import sched
import time
import csv
import os
import threading
from mission import delta_v, flight_time, fuel_needed, random_event

csv_lock = threading.Lock()

def build_parser():
    p = argparse.ArgumentParser(description="Симулятор межпланетной миссии «АРЕС-1»")
    p.add_argument("--days",  type=int,   default=30,   help="длительность миссии, сут")
    p.add_argument("--seed",  type=int,   default=None, help="зерно ГСЧ")
    p.add_argument("--speed", type=float, default=0.1,  help="секунд на 1 сутки")
    p.add_argument("--ship",  type=str,   default="АРЕС-1", help="название корабля")
    p.add_argument("--csv",   type=str,   default="mission_report.csv", help="файл для сохранения хроники CSV")
    p.add_argument("--fleet", action="store_true", help="запустить флот из нескольких кораблей в независимых потоках")
    return p

def run_single_mission(ship_name, days, seed, speed, csv_file):
    """Симуляция одного космического корабля с собственным планировщиком."""
    resource = 100
    s = sched.scheduler(time.time, time.sleep)
    chronicle_data = []

    def day_report(day):
        nonlocal resource

        event_seed = (seed + day) if seed is not None else None
        desc, delta = random_event(event_seed)
        resource = max(0, min(100, resource + delta))
        
        bar = '#' * (resource // 5)
        log_line = f"Сутки {day:>2} | {desc:<38s} {delta:+3d} | ресурс {resource:3d}% {bar}"
        print(f"[{ship_name}] {log_line}")
        
        chronicle_data.append({
            "ship": ship_name, 
            "day": day, 
            "event": desc, 
            "delta": delta, 
            "resource": resource
        })

        if resource == 0:
            print(f"[{ship_name}] КРИТИЧЕСКИЙ ОТКАЗ. Миссия прервана на сутках {day}.")
            for ev in list(s.queue):
                s.cancel(ev)
            return

        if day < days:
            s.enter(speed, 1, day_report, (day + 1,))

    s.enter(speed, 1, day_report, (1,))
    s.run()

    if csv_file:
        file_exists = os.path.exists(csv_file)
        with csv_lock:
            with open(csv_file, mode="a", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["ship", "day", "event", "delta", "resource"])
                if not file_exists:
                    writer.writeheader()
                writer.writerows(chronicle_data)

def run_fleet_missions(days, speed, csv_file):
    """Запуск нескольких кораблей параллельно в независимых потоках."""
    ships = [
        ("АРЕС-1", 42),
        ("ГЕРМЕС-2", 100),
        ("ЗЕВС-3", 777)
    ]
    
    if os.path.exists(csv_file):
        os.remove(csv_file)

    print("=" * 65)
    print(f"       ЗАПУСК ФЛОТА ИЗ {len(ships)} КОРАБЛЕЙ В НЕЗАВИСИМЫХ ПОТОКАХ")
    print("=" * 65)
    
    threads = []
    for name, seed in ships:
        t = threading.Thread(target=run_single_mission, args=(name, days, seed, speed, csv_file))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
        
    print("=" * 65)
    print(f"Все миссии флота успешно завершены. Общая хроника сохранена в: {csv_file}")

def main():
    args = build_parser().parse_args()
    
    if args.fleet:
        run_fleet_missions(args.days, args.speed, args.csv)
    else:
        print("=" * 65)
        print(f"               МИССИЯ «{args.ship}»: Марс ({args.days} сут)")
        print("=" * 65)
        
        if os.path.exists(args.csv):
            os.remove(args.csv)
            
        run_single_mission(args.ship, args.days, args.seed, args.speed, args.csv)
        print("-" * 65)
        print(f"Хроника одиночной миссии сохранена в файл: {args.csv}")

if __name__ == "__main__":
    main()