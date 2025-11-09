while True:

    days_late = int(input("Enter the number of days the book is returned late: "))
    fine = 0
    if days_late <= 0:
        fine = 0
    elif days_late <= 6:
        fine = days_late * 0.50
    elif days_late <= 10:
        fine = 3 + (days_late - 6)
    elif days_late <= 30:
        fine = 8 + (days_late - 10) * 5
    else:
        fine = "Membership Cancelled"
    if fine == "Membership Cancelled":
        print("Your membership has been cancelled.")
    else:
        print(f"The fine is {fine} rupees.")