male_names = {
    "james", "john", "robert", "michael", "william", "david", "richard", "joseph",
    "thomas", "charles", "daniel", "matthew", "anthony", "mark", "donald", "paul",
    "steven", "andrew", "kenneth", "george", "brian", "edward", "joshua", "kevin",
    "peter", "henry", "adam", "nathan", "samuel", "patrick", "liam", "noah",
    "oliver", "elijah", "lucas", "mason", "ethan", "aiden", "logan", "jacob",
    "ali", "omar", "hassan", "ahmed", "ibrahim", "yusuf", "musa", "issa",
    "brian", "kevin", "eric", "stephen", "dennis", "felix", "victor", "simon",
    "chris", "ryan", "justin", "brandon", "tyler", "zachary", "caleb", "dylan",
    "raj", "arjun", "amit", "rohan", "rahul", "vijay", "suresh", "ravi",
    "carlos", "juan", "luis", "miguel", "jose", "antonio", "diego", "pedro"
}

female_names = {
    "mary", "patricia", "jennifer", "linda", "barbara", "elizabeth", "susan",
    "jessica", "sarah", "karen", "lisa", "nancy", "betty", "margaret", "sandra",
    "ashley", "emily", "dorothy", "kimberly", "donna", "carol", "michelle",
    "amanda", "melissa", "deborah", "stephanie", "rebecca", "sharon", "laura",
    "cynthia", "olivia", "emma", "ava", "isabella", "sophia", "mia", "abigail",
    "harper", "evelyn", "aria", "ella", "scarlett", "grace", "chloe", "victoria",
    "riley", "zoey", "nora", "lily", "eleanor", "hannah", "lillian", "addison",
    "fatima", "aisha", "zainab", "maryam", "khadijah", "amina", "halima", "sara",
    "grace", "joyce", "faith", "mercy", "blessing", "charity", "joy", "patience",
    "priya", "ananya", "divya", "pooja", "sunita", "kavya", "meera", "sneha",
    "maria", "ana", "lucia", "sofia", "valentina", "camila", "isabella", "elena"
}

def detect_gender_by_suffix(name):
    name = name.lower()
    male_suffixes   = ("on", "an", "en", "ard", "bert", "ford", "mund", "ald")
    female_suffixes = ("a", "ia", "ina", "ine", "elle", "ette", "leen", "een", "lyn")

    if name.endswith(female_suffixes):
        return "Female", "suffix pattern"
    if name.endswith(male_suffixes):
        return "Male", "suffix pattern"
    return None, None

def verify_gender(name):
    name_clean = name.strip().lower()

    if name_clean in male_names:
        return "Male", "name database"
    elif name_clean in female_names:
        return "Female", "name database"
    else:
        gender, source = detect_gender_by_suffix(name_clean)
        if gender:
            return gender, source
        return "Unknown", "not found"

def display_result(name, gender, source):
    symbols = {"Male": "♂", "Female": "♀", "Unknown": "?"}
    colors  = {"Male": "\033[94m", "Female": "\033[95m", "Unknown": "\033[93m"}
    reset   = "\033[0m"

    symbol = symbols.get(gender, "?")
    color  = colors.get(gender, "")

    print(f"\n  Name   : {name.title()}")
    print(f"  Gender : {color}{symbol}  {gender}{reset}")
    print(f"  Source : {source}")
    print("-" * 35)

def main():
    print("=" * 35)
    print("    Gender Verification by Name")
    print("=" * 35)
    print("Type 'quit' to exit.\n")

    while True:
        name = input("Enter a name: ").strip()

        if name.lower() == "quit":
            print("\nGoodbye!")
            break

        if not name:
            print("  ⚠  Please enter a name.\n")
            continue

        if not name.replace(" ", "").isalpha():
            print("  ⚠  Name should contain letters only.\n")
            continue

        gender, source = verify_gender(name)
        display_result(name, gender, source)

if __name__ == "__main__":
    main()