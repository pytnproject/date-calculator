# 📅 Date Calculator

A simple Python CLI tool that calculates the date after a given number of days from today.



# ✨ Features

- Shows today's date on startup
- Calculates future dates from user input
- Handles invalid and oversized input
- Interactive loop — type `0` to exit


# 🚀 Usage

```bash
python script.py
```


# 💻 Code — `script.py`

```python
from datetime import datetime, date, timedelta

now = datetime.now()

print(f"Today's date is {now}")

while True:
    try:
        a = input("\nEnter a number to determine in how many days a certain date will be. To exit, enter — '0': ")
        a = int(a)
        custom_date = now + timedelta(days=a)
        if a == 0:
            print("\nThank you for using the program! TG channel: @pytnproject\n")
            break
        print(f"\nIn {a} days it will be — {custom_date}\n")
    except ValueError:
        print(f"\n'{a}' is not a number!\n")
    except OverflowError:
        print(f"\n'{a}' the number is too long!\n")
```

<details>
<summary>📦 Example session</summary>

```
Today's date is 2026-11-11 14:23:45.123456

Enter a number to determine in how many days a certain date will be. To exit, enter: '0':
30

In 30 days it will be — 2026-12-11 14:23:45.123456

Enter a number to determine in how many days a certain date will be. To exit, enter: '0':
0

Thank you for using the program! TG channel: @pytnproject
```

</details>

<details>
<summary>⚠️ Error handling</summary>

| Situation | Output |
|-----------|--------|
| Not a number | `'<input>' is not a number!` |
| Number too large | `'<input>' the number is too long!` |

</details>

<details>
<summary>🧠 How it works</summary>

1. Gets the current date via `datetime.now()`
2. Prompts for a number of days
3. Adds it with `timedelta(days=a)`
4. Prints the resulting date, loops until `0` is entered

</details>



📬 Telegram: [@pytnproject](https://t.me/pytnproject)
