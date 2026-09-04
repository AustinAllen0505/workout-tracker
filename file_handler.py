import csv


def load_workouts(filename):
    workouts = []

    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                workouts.append(row)

    except FileNotFoundError:
        pass

    return workouts


def save_workouts(filename, workouts):
    fieldnames = ["date", "exercise", "weight", "sets", "reps"]

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(workouts)