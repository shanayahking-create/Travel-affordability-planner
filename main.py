print()
print("TRAVEL AFFORDABILITY PLANNER")

print()
current_savings = float(input("how much money have you already saved? $"))
current_earnings = float(input("how much do you earn on average per week? $"))
savings_per_week = float(input("how much can you save per week? $"))
weeks_until_departure = int(input("how many weeks until departure?"))

print()
print("Savings =")
print(current_savings)
print("Earnings =")
print(current_earnings)
print("Savings per week =")
print(savings_per_week)
print("weeks until departure =")
print(weeks_until_departure)

print()
print("------EXPENSES------")

weekly_expenses = float(input("how much do your weekly expenses add up to? $"))
additional_expenses = float(input("how much do your additional expenses add up to? $"))
total_expenses_prior_to_trip = weekly_expenses * weeks_until_departure + additional_expenses

print("total expenses prior to trip =")
print(total_expenses_prior_to_trip)

money_saved_before_trip = savings_per_week * weeks_until_departure
money_by_departure = current_savings + money_saved_before_trip

print()
print("------MONEY BY DEPARTURE------")
print("You could have $", round(money_by_departure, 2), "by departure.")

print()
print("------TRIP OPTIONS------")

print("1 = Plan one trip")
print("2 = Compare two trips")

trip_choice = int(input("Choose 1 or 2: "))

if trip_choice == 1:
    print()
    print("------TRIP DETAILS------")
    destination = input("Where are you travelling? ")
    flight_cost = float(input("How much will flights cost? $"))
    accommodation_cost = float(input("How much will accommodation cost? $"))
    transport_cost = float(input("How much will local transport cost? $"))
    activities_cost = float(input("How much will activities cost? $"))

    trip_days = int(input("How many days is your trip? "))
    daily_spending = float(input("How much do you expect to spend each day? $"))

    total_daily_spending = trip_days * daily_spending
    total_trip_cost = flight_cost + accommodation_cost + transport_cost + activities_cost + total_daily_spending

    print()
    print("------TRIP COST------")

    print("Destination:", destination)
    print("Flights: $", round(flight_cost, 2))
    print("Accommodation: $", round(accommodation_cost, 2))
    print("Transport: $", round(transport_cost, 2))
    print("Activities: $", round(activities_cost, 2))
    print("Daily spending total: $", round(total_daily_spending, 2))
    print("Total trip cost: $", round(total_trip_cost, 2))

    print()
    print("------EMERGENCY MONEY------")

    emergency_money = float(input("How much money would you like to keep aside for emergencies? $"))
    print("Emergency money: $", round(emergency_money, 2))

    money_available_for_trip = money_by_departure - emergency_money

    print()
    print("------AFFORDABILITY RESULT------")

    print("Money available for trip: $", round(money_available_for_trip, 2))
    print("Trip cost: $", round(total_trip_cost, 2))

    if money_available_for_trip >= total_trip_cost:
        money_left = money_available_for_trip - total_trip_cost

        print("Good news! You can afford this trip.")
        print("You would have $", round(money_left, 2), "left over.")

    else:
        shortfall = total_trip_cost - money_available_for_trip

        print("You cannot afford this trip yet.")
        print("You are short by $", round(shortfall, 2))

    savings_target = total_trip_cost + emergency_money

    progress = (current_savings / savings_target) * 100

    if progress > 100:
        progress = 100

    bar_length = 20
    filled = int((progress / 100) * bar_length)
    empty = bar_length - filled

    savings_bar = "#" * filled + "-" * empty

    print()
    print("------CURRENT SAVINGS PROGRESS------")
    print("[" + savings_bar + "]")
    print("You currently have $", round(current_savings, 2), "saved.")
    print("Your total savings goal is $", round(savings_target, 2))
    print("You are", round(progress, 1), "% of the way to your savings goal.")


    flight_percentage = (flight_cost / total_trip_cost) * 100
    accommodation_percentage = (accommodation_cost / total_trip_cost) * 100
    transport_percentage = (transport_cost / total_trip_cost) * 100
    activities_percentage = (activities_cost / total_trip_cost) * 100
    daily_spending_percentage = (total_daily_spending / total_trip_cost) * 100

    print()
    print("------COST BREAKDOWN------")

    print("Flights:", round(flight_percentage, 1), "%")
    print("Accommodation:", round(accommodation_percentage, 1), "%")
    print("Transport:", round(transport_percentage, 1), "%")
    print("Activities:", round(activities_percentage, 1), "%")
    print("Daily spending:", round(daily_spending_percentage, 1), "%")


    biggest_expense = max(flight_cost, accommodation_cost,transport_cost, activities_cost, total_daily_spending)

    print()

    if biggest_expense == flight_cost:
        print("Your biggest expense is flights.")

    elif biggest_expense == accommodation_cost:
        print("Your biggest expense is accommodation.")

    elif biggest_expense == transport_cost:
        print("Your biggest expense is transport.")

    elif biggest_expense == activities_cost:
        print("Your biggest expense is activities.")

    else:
        print("Your biggest expense is daily spending.")

    affordability_score = (money_available_for_trip / total_trip_cost) * 100

    if affordability_score > 100:
        affordability_score = 100

    print()
    print("------AFFORDABILITY SCORE------")
    print("Score:", round(affordability_score, 1), "/ 100")

    if affordability_score == 100:
        print("Rating: Affordable")

    elif affordability_score >= 90:
        print("Rating: Almost there")

    elif affordability_score >= 75:
        print("Rating: Close, but some changes are needed")

    elif affordability_score >= 50:
        print("Rating: Budget may be too tight")

    else:
        print("Rating: Currently not affordable")

    print()
    print("------RECOMMENDATIONS------")

    if money_available_for_trip < total_trip_cost:

        shortfall = total_trip_cost - money_available_for_trip

        extra_savings_per_week = shortfall / weeks_until_departure

        print("You are currently short by $", round(shortfall, 2))
        print("You could make the trip affordable by saving an extra $",
              round(extra_savings_per_week, 2),
              "per week.")

        reduced_daily_spending = shortfall / trip_days

        print("Or you could reduce your daily spending by about $",
              round(reduced_daily_spending, 2),
              "per day.")

        if daily_spending > 0:
            days_to_remove = shortfall / daily_spending

            print("Or shorten the trip by about",
                  round(days_to_remove),
                  "days.")

    else:
        print("Your trip is already affordable, so no changes are needed.")

elif trip_choice == 2:
    print()
    print("------TRIP A------")

    trip_a_name = input("Where are you travelling for Trip A? ")

    flight_a = float(input("Flight cost: $"))
    accommodation_a = float(input("Accommodation cost: $"))
    transport_a = float(input("Transport cost: $"))
    activities_a = float(input("Activities cost: $"))

    days_a = int(input("How many days is Trip A? "))
    daily_spending_a = float(input("How much will you spend each day? $"))

    daily_total_a = days_a * daily_spending_a

    total_a = (flight_a + accommodation_a + transport_a + activities_a + daily_total_a)

    print()
    print("------TRIP B------")

    trip_b_name = input("Where are you travelling for Trip B? ")

    flight_b = float(input("Flight cost: $"))
    accommodation_b = float(input("Accommodation cost: $"))
    transport_b = float(input("Transport cost: $"))
    activities_b = float(input("Activities cost: $"))

    days_b = int(input("How many days is Trip B? "))
    daily_spending_b = float(input("How much will you spend each day? $"))

    daily_total_b = days_b * daily_spending_b

    total_b = (flight_b + accommodation_b + transport_b + activities_b  + daily_total_b)

    print()
    print("------TRIP COMPARISON------")

    print(trip_a_name, "costs $", round(total_a, 2))
    print(trip_b_name, "costs $", round(total_b, 2))

    if total_a < total_b:
        difference = total_b - total_a

        print(trip_a_name, "is the cheaper trip.")
        print("It is $", round(difference, 2), "cheaper than", trip_b_name)

    elif total_b < total_a:
        difference = total_a - total_b

        print(trip_b_name, "is the cheaper trip.")
        print("It is $", round(difference, 2), "cheaper than", trip_a_name)

    else:
        print("Both trips cost the same amount.")

    print()
    print("------EMERGENCY MONEY------")

    emergency_money = float(input("How much money would you like to keep aside for emergencies? $"))

    money_available = money_by_departure - emergency_money

    print()
    print("------AFFORDABILITY------")

    print("Money available for travel: $", round(money_available, 2))

    if money_available >= total_a:
        print(trip_a_name, "is affordable.")

    else:
        shortfall_a = total_a - money_available

        print(trip_a_name, "is not affordable.")
        print("You are short by $", round(shortfall_a, 2))

    if money_available >= total_b:
        print(trip_b_name, "is affordable.")

    else:
        shortfall_b = total_b - money_available

        print(trip_b_name, "is not affordable.")
        print("You are short by $", round(shortfall_b, 2))

    print()
    print("------FINAL RECOMMENDATION------")

    affordable_a = money_available >= total_a
    affordable_b = money_available >= total_b

    if affordable_a and affordable_b:

        if total_a < total_b:
            print("You can afford both trips.")
            print(trip_a_name, "is the cheaper option, so it may be the better choice.")

        elif total_b < total_a:
            print("You can afford both trips.")
            print(trip_b_name, "is the cheaper option, so it may be the better choice.")

        else:
            print("You can afford both trips and they cost the same.")

    elif affordable_a:
        print(trip_a_name, "is the better option because you can afford it.")

    elif affordable_b:
        print(trip_b_name, "is the better option because you can afford it.")

    else:
        print("Neither trip is currently affordable.")

        if total_a < total_b:
            print(trip_a_name, "is cheaper and would be easier to save for.")

        elif total_b < total_a:
            print(trip_b_name, "is cheaper and would be easier to save for.")

        else:
            print("Both trips cost the same amount.")

    print()
    print("------AFFORDABILITY SCORES------")

    score_a = (money_available / total_a) * 100
    score_b = (money_available / total_b) * 100

    if score_a > 100:
        score_a = 100

    if score_b > 100:
        score_b = 100

    print(trip_a_name, "score:", round(score_a, 1), "/ 100")
    print(trip_b_name, "score:", round(score_b, 1), "/ 100")

    if score_a == 100:
        print(trip_a_name, "rating: Affordable")
    elif score_a >= 90:
        print(trip_a_name, "rating: Almost there")
    elif score_a >= 75:
        print(trip_a_name, "rating: Close")
    else:
        print(trip_a_name, "rating: Not currently affordable")

    if score_b == 100:
        print(trip_b_name, "rating: Affordable")
    elif score_b >= 90:
        print(trip_b_name, "rating: Almost there")
    elif score_b >= 75:
        print(trip_b_name, "rating: Close")
    else:
        print(trip_b_name, "rating: Not currently affordable")

    print()
    print("------RECOMMENDATIONS------")

    # trip a recommendations
    print()
    print(trip_a_name)

    if money_available < total_a:
        shortfall_a = total_a - money_available

        extra_weekly_a = shortfall_a / weeks_until_departure
        reduce_daily_a = shortfall_a / days_a

        print("You are short by $", round(shortfall_a, 2))
        print("You could save an extra $", round(extra_weekly_a, 2), "per week.")
        print("Or reduce daily spending by about $", round(reduce_daily_a, 2), "per day.")

        if daily_spending_a > 0:
            days_to_remove_a = shortfall_a / daily_spending_a

            print("Or shorten the trip by about",
                  round(days_to_remove_a),
                  "days.")

    else:
        print("This trip is already affordable.")


    # trip b recommendations
    print()
    print(trip_b_name)

    if money_available < total_b:
        shortfall_b = total_b - money_available

        extra_weekly_b = shortfall_b / weeks_until_departure
        reduce_daily_b = shortfall_b / days_b

        print("You are short by $", round(shortfall_b, 2))
        print("You could save an extra $", round(extra_weekly_b, 2), "per week.")
        print("Or reduce daily spending by about $", round(reduce_daily_b, 2), "per day.")

        if daily_spending_b > 0:
            days_to_remove_b = shortfall_b / daily_spending_b

            print("Or shorten the trip by about",
                  round(days_to_remove_b),
                  "days.")

    else:
        print("This trip is already affordable.")

else:
    print("Please choose either 1 or 2.")
