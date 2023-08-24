class FlightTable:
    def _init_(self):
        self.data = [
            {"Location": "Mumbai", "Team 01": "India", "Team 02": "Sri Lanka", "Timing": "DAY"},
            {"Location": "Delhi", "Team 01": "England", "Team 02": "Australia", "Timing": "DAY-NIGHT"},
            {"Location": "Chennai", "Team 01": "India", "Team 02": "South Africa", "Timing": "DAY"},
            {"Location": "Indore", "Team 01": "England", "Team 02": "Sri Lanka", "Timing": "DAY-NIGHT"},
            {"Location": "Mohali", "Team 01": "Australia", "Team 02": "South Africa", "Timing": "DAY-NIGHT"},
            {"Location": "Delhi", "Team 01": "India", "Team 02": "Australia", "Timing": "DAY"}
        ]

    def search_by_team(self, team_name):
        matches = [match for match in self.data if team_name in (match["Team 01"], match["Team 02"])]
        return matches

    def search_by_location(self, location):
        matches = [match for match in self.data if match["Location"] == location]
        return matches

    def search_by_timing(self, timing):
        matches = [match for match in self.data if match["Timing"] == timing]
        return matches

def main():
    flight_table = FlightTable()

    while True:
        print("Search Options:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            team_name = input("Enter the Team name: ")
            matches = flight_table.search_by_team(team_name)
        elif choice == "2":
            location = input("Enter the Location: ")
            matches = flight_table.search_by_location(location)
        elif choice == "3":
            timing = input("Enter the Timing: ")
            matches = flight_table.search_by_timing(timing)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        if not matches:
            print("No matches found for the given criteria.")
        else:
            print("Match Location\tTeam 01\tTeam 02\tTiming")
            for match in matches:
                print(f"{match['Location']}\t{match['Team 01']}\t{match['Team 02']}\t{match['Timing']}")

if _name_ == "_main_":
    main()
