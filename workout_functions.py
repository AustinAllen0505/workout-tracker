def log_workout(workouts):
    date = input("Enter date (YYYY-MM-DD): ")
    exercise = input("Enter exercise: ")
    weight = input("Enter weight: ")
    sets = input("Enter sets: ")
    reps = input("Enter reps: ")

    workout = {
        "date": date,
        "exercise": exercise,
        "weight": weight,
        "sets": sets,
        "reps": reps
    }

    workouts.append(workout)

    print("\nWorkout added successfully!")


def view_workouts(workouts):
    if len(workouts) == 0:
        print("\nNo workouts found.")
        return

    print("\nWORKOUT HISTORY")
    print("-----------------------------")

    for workout in workouts:
        print(
            f"{workout['date']} - "
            f"{workout['exercise']} - "
            f"{workout['weight']} lbs - "
            f"{workout['sets']} sets x "
            f"{workout['reps']} reps"
        )


def search_exercise(workouts):
    search_term = input("Enter exercise to search for: ").lower()

    found = False

    for workout in workouts:
        if workout["exercise"].lower() == search_term:
            print(
                f"{workout['date']} - "
                f"{workout['exercise']} - "
                f"{workout['weight']} lbs - "
                f"{workout['sets']} sets x "
                f"{workout['reps']} reps"
            )

            found = True

    if found == False:
        print("\nNo workouts found for that exercise.")


def view_personal_records(workouts):
    if len(workouts) == 0:
        print("\nNo workouts found.")
        return

    personal_records = {}

    for workout in workouts:
        exercise = workout["exercise"]
        weight = float(workout["weight"])

        if exercise not in personal_records:
            personal_records[exercise] = weight

        elif weight > personal_records[exercise]:
            personal_records[exercise] = weight

    print("\nPERSONAL RECORDS")
    print("-----------------------------")

    for exercise, weight in personal_records.items():
        print(f"{exercise}: {weight} lbs")