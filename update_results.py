#!/usr/bin/env python3
"""Interactive script to update match results after a completed Bundesliga matchday.

Automatically determines the next matchday, prompts for each match result,
then updates results.py and data_loader.py.

Usage:
    python update_results.py
"""
import re
import sys
from datetime import datetime


def get_last_matchday():
    """Read results.py to find the highest matchday number."""
    with open("results.py", "r", encoding="utf-8") as f:
        content = f.read()

    # Find all results_dN patterns
    matches = re.findall(r"results_d(\d+)\s*=", content)
    if not matches:
        return 0
    return max(int(m) for m in matches)


def get_next_matchday_fixtures(matchday_num):
    """Read match_days.py to get fixtures for the given matchday."""
    import match_days

    if matchday_num not in match_days.match_days:
        print(f"❌ Тур {matchday_num} не найден в match_days.py")
        sys.exit(1)

    matches = match_days.match_days[matchday_num]["matches"]
    fixtures = []
    for i in sorted(matches.keys()):
        home = matches[i]["H"]
        away = matches[i]["A"]
        fixtures.append((i, home, away))
    return fixtures


def parse_score(score_str):
    """Parse a score string like '2-1' or '2 : 1' into (home_goals, away_goals)."""
    score_str = score_str.strip()
    parts = re.split(r"[-:]", score_str)
    if len(parts) != 2:
        return None
    try:
        home = int(parts[0].strip())
        away = int(parts[1].strip())
        return (home, away)
    except ValueError:
        return None


def parse_half_time_score(score_str):
    """Parse a half-time score string like '1-0' or '1 : 0' into (home_ht, away_ht)."""
    return parse_score(score_str)


def determine_result(home_goals, away_goals):
    """Determine match result: 'H', 'D', or 'A'."""
    if home_goals > away_goals:
        return "H"
    elif home_goals < away_goals:
        return "A"
    else:
        return "D"


def determine_half_time_result(home_ht, away_ht):
    """Determine half-time result: 'H', 'D', or 'A'."""
    if home_ht > away_ht:
        return "H"
    elif home_ht < away_ht:
        return "A"
    else:
        return "D"


def prompt_match_result(match_num, home, away):
    """Prompt user for a single match result. Returns dict with all fields."""
    print(f"\n--- Матч {match_num}: {home} — {away} ---")

    # Full time score
    while True:
        score = input(f"  Счёт (полный матч), например '2-1': ").strip()
        ft = parse_score(score)
        if ft is not None:
            break
        print("  ❌ Формат: 'голы_хозяев-голы_гостей', например '2-1'")

    # Half time score
    while True:
        ht_score = input(f"  Счёт (1-й тайм), например '1-0': ").strip()
        ht = parse_half_time_score(ht_score)
        if ht is not None:
            break
        print("  ❌ Формат: 'голы_хозяев-голы_гостей', например '1-0'")

    # Date
    while True:
        date_str = input(f"  Дата (ДД/ММ/ГГ), например '29/11/26': ").strip()
        if re.match(r"^\d{2}/\d{2}/\d{2}$", date_str):
            break
        print("  ❌ Формат: ДД/ММ/ГГ, например '29/11/26'")

    return {
        "HomeTeam": home,
        "AwayTeam": away,
        "FTHG": ft[0],
        "FTAG": ft[1],
        "HTHG": ht[0],
        "HTAG": ht[1],
        "FTR": determine_result(ft[0], ft[1]),
        "HTR": determine_half_time_result(ht[0], ht[1]),
        "Date": date_str,
    }


def generate_results_code(matchday_num, results_list):
    """Generate Python code for a new results DataFrame."""
    home_teams = [r["HomeTeam"] for r in results_list]
    away_teams = [r["AwayTeam"] for r in results_list]
    fthg = [r["FTHG"] for r in results_list]
    ftag = [r["FTAG"] for r in results_list]
    hthg = [r["HTHG"] for r in results_list]
    httag = [r["HTAG"] for r in results_list]
    ftr = [r["FTR"] for r in results_list]
    htr = [r["HTR"] for r in results_list]
    dates = [r["Date"] for r in results_list]

    # Format lists with proper quoting
    def format_list(items):
        if all(isinstance(x, str) for x in items):
            return "[" + ", ".join(f"'{x}'" for x in items) + "]"
        else:
            return "[" + ", ".join(str(x) for x in items) + "]"

    code = f"""
results_d{matchday_num} = pd.DataFrame({{
    "HomeTeam": {format_list(home_teams)},
    "AwayTeam": {format_list(away_teams)},
    "FTHG": {format_list(fthg)},
    "FTAG": {format_list(ftag)},
    "HTHG": {format_list(hthg)},
    "HTAG": {format_list(httag)},
    "FTR": {format_list(ftr)},
    "HTR": {format_list(htr)},
    "Date": {format_list(dates)}
}})
"""
    return code


def update_results_py(matchday_num, code):
    """Insert new results DataFrame into results.py before results_empty."""
    with open("results.py", "r", encoding="utf-8") as f:
        content = f.read()

    # Find the results_empty line and insert before it
    empty_pattern = r"\nresults_empty = pd\.DataFrame"
    match = re.search(empty_pattern, content)
    if not match:
        print("❌ Не удалось найти results_empty в results.py")
        sys.exit(1)

    # Insert new code before results_empty
    insert_pos = match.start()
    new_content = content[:insert_pos] + code + "\n" + content[insert_pos:]

    with open("results.py", "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"\n✅ results.py обновлён: добавлен results_d{matchday_num}")


def update_data_loader_py(matchday_num):
    """Add the new results_dN to load_results_dataframes() in data_loader.py."""
    with open("predict_bundesliga/data_loader.py", "r", encoding="utf-8") as f:
        content = f.read()

    # Find the last results.dN in the return statement and add the new one
    # The pattern matches the end of the return list
    new_entry = f", results.results_d{matchday_num}"

    # Find the closing bracket of the return list and insert before it
    # Look for the pattern: results.results_dN]
    pattern = r"(return \[.*?results\.results_d\d+)(\])"
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print("❌ Не удалось найти load_results_dataframes в data_loader.py")
        sys.exit(1)

    # Insert the new entry before the closing bracket
    new_content = content[:match.end(1)] + new_entry + content[match.end(1):]

    with open("predict_bundesliga/data_loader.py", "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✅ data_loader.py обновлён: добавлен results.results_d{matchday_num}")


def main():
    print("=" * 60)
    print("  Обновление результатов Бундеслиги")
    print("=" * 60)

    # Determine last completed matchday
    last_matchday = get_last_matchday()
    next_matchday = last_matchday + 1

    print(f"\nПоследний добавленный тур: {last_matchday}")
    print(f"Следующий тур для обновления: {next_matchday}")

    # Confirm
    confirm = input(f"\nОбновить результаты тура {next_matchday}? (y/n): ").strip().lower()
    if confirm != "y":
        print("Отмена.")
        return

    # Get fixtures
    fixtures = get_next_matchday_fixtures(next_matchday)
    print(f"\nНайдено {len(fixtures)} матчей в туре {next_matchday}:\n")

    # Collect results
    results_list = []
    for match_num, home, away in fixtures:
        result = prompt_match_result(match_num, home, away)
        results_list.append(result)

    # Summary
    print("\n" + "=" * 60)
    print("  Сводка результатов")
    print("=" * 60)
    for r in results_list:
        print(f"  {r['HomeTeam']:20s} {r['FTHG']}-{r['FTAG']} {r['AwayTeam']:20s}  (1-й тайм {r['HTHG']}-{r['HTAG']})")

    # Confirm write
    confirm = input(f"\nЗаписать результаты в файлы? (y/n): ").strip().lower()
    if confirm != "y":
        print("Отмена. Файлы не изменены.")
        return

    # Update files
    code = generate_results_code(next_matchday, results_list)
    update_results_py(next_matchday, code)
    update_data_loader_py(next_matchday)

    print("\n" + "=" * 60)
    print("  ✅ Готово!")
    print("=" * 60)
    print(f"\nТур {next_matchday} добавлен. Перезапустите сервер:")
    print("  python app.py")


if __name__ == "__main__":
    main()
