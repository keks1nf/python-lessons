import matplotlib.pyplot as plt
import pandas as pd


# --------------------------------------------------
# 1. LOAD DATA
# --------------------------------------------------
def load_data():
    calendar = pd.read_csv("../rental_house/calendar.csv", parse_dates=["date"])
    pricing = pd.read_csv("../rental_house/pricing.csv")
    clients = pd.read_csv("../rental_house/clients.csv")
    bookings = pd.read_csv("../rental_house/bookings_old.csv", parse_dates=["check_in", "check_out"])
    expenses = pd.read_csv("../rental_house/opex.csv", parse_dates=["date"])
    return calendar, pricing, clients, bookings, expenses


# --------------------------------------------------
# 2. FLAG BOOKED DAYS BASED ON BOOKINGS
# --------------------------------------------------
def mark_booked_days(calendar, bookings):
    calendar["is_booked"] = 0  # start with all free days

    for _, row in bookings.iterrows():
        stay_days = pd.date_range(
            row["check_in"],
            row["check_out"] - pd.Timedelta(days=1)
        )
        calendar.loc[calendar["date"].isin(stay_days), "is_booked"] = 1

    return calendar


# --------------------------------------------------
# 3. MAIN ANALYTICS
# --------------------------------------------------
def analyze(calendar, pricing, clients, bookings, expenses):
    print("\n==============================")
    print("      YEARLY ANALYTICS")
    print("==============================\n")

    # ----- Income / Expenses -----
    total_income = bookings["total_price"].sum()
    total_expenses = expenses["amount"].sum()
    profit = total_income - total_expenses

    print(f"Total income:      {total_income:,.0f} грн")
    print(f"Total expenses:    {total_expenses:,.0f} грн")
    print(f"NET PROFIT:        {profit:,.0f} грн")

    # ----- Occupancy -----
    booked_days = calendar["is_booked"].sum()
    total_days = len(calendar)
    occupancy = booked_days / total_days * 100

    print(f"Occupancy:         {occupancy:.2f}%")

    # --------------------------------------------------
    # 4. MONTHLY ANALYTICS
    # --------------------------------------------------
    bookings["month"] = bookings["check_in"].dt.to_period("M")
    expenses["month"] = expenses["date"].dt.to_period("M")
    calendar["month"] = calendar["date"].dt.to_period("M")

    income_monthly = bookings.groupby("month")["total_price"].sum()
    expenses_monthly = expenses.groupby("month")["amount"].sum()
    occ_monthly = calendar.groupby("month")["is_booked"].mean() * 100

    # --------------------------------------------------
    # 5. PLOTS
    # --------------------------------------------------
    plt.figure(figsize=(8, 5))
    plt.plot(income_monthly.index.astype(str), income_monthly.values)
    plt.title("Щомісячний Дохід")
    plt.xlabel("Місяць")
    plt.ylabel("Сума (грн)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("income_monthly.png")
    print("✔ Збережено графік: income_monthly.png")

    plt.figure(figsize=(8, 5))
    plt.plot(expenses_monthly.index.astype(str), expenses_monthly.values)
    plt.title("Щомісячні Витрати")
    plt.xlabel("Місяць")
    plt.ylabel("Сума (грн)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("expenses_monthly.png")
    print("✔ Збережено графік: expenses_monthly.png")

    plt.figure(figsize=(8, 5))
    plt.plot(occ_monthly.index.astype(str), occ_monthly.values)
    plt.title("Місячна завантаженість (%)")
    plt.xlabel("Місяць")
    plt.ylabel("Завантаження (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("occupancy_monthly.png")
    print("✔ Збережено графік: occupancy_monthly.png")


# --------------------------------------------------
# 6. ENTRY POINT
# --------------------------------------------------
def main():
    calendar, pricing, clients, bookings, expenses = load_data()
    calendar = mark_booked_days(calendar, bookings)
    analyze(calendar, pricing, clients, bookings, expenses)


if __name__ == "__main__":
    main()
