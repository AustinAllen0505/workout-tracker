import file_handler
import workout_functions


FILENAME = "workouts.csv"


def show_menu():
    print("\n=============================")
    print("       WORKOUT TRACKER")
    print("=============================")
    print("1. Log a Workout")
    print("2. View Workout History")
    print("3. Search by Exercise")
    print("4. View Personal Records")
    print("5. Exit")


def main():
    workouts = file_handler.load_workouts(FILENAME)

    while True:
        show_menu()

        choice = input("\nChoose an option: ")

        if choice == "1":
            workout_functions.log_workout(workouts)
            file_handler.save_workouts(FILENAME, workouts)

        elif choice == "2":
            workout_functions.view_workouts(workouts)

        elif choice == "3":
            workout_functions.search_exercise(workouts)

        elif choice == "4":
            workout_functions.view_personal_records(workouts)

        elif choice == "5":
            file_handler.save_workouts(FILENAME, workouts)
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()


#