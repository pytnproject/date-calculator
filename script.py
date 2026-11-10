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