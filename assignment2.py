# ==========================
# TASK 1
# Interactive Terminal E-Commerce Cart & Inventory Tracker
# ==========================

def task1():
    print("========================================")
    print("TASK 1: E-COMMERCE CART & INVENTORY TRACKER")
    print("========================================")

    # Available inventory: Item Name -> Unit Price
    catalog = {"laptop": 800, "mouse": 20, "keyboard": 50, "monitor": 150}

    grand_total = 0

    while True:
        command = input("Enter item to buy (or 'checkout' / 'exit'): ").lower()

        if command == "exit":
            # Break out of the loop immediately without printing a final bill
            print("--> Order cancelled. No bill was generated.")
            break

        elif command == "checkout":
            # Apply conditional discounts based on grand_total
            if grand_total >= 500:
                discount = grand_total * 0.10
            elif 200 <= grand_total < 500:
                discount = grand_total * 0.05
            else:
                discount = 0

            final_total = grand_total - discount

            print("\nCHECKOUT RECEIPT")
            print("========================================")
            print(f"Subtotal: ${grand_total}")
            print(f"Discount: ${discount}")
            print(f"Final Total: ${final_total}")
            print("========================================")
            break

        elif command in catalog:
            price = catalog[command]
            grand_total += price
            print(f"--> Added {command} (${price}) to order.")

        else:
            print("--> [ERROR] Item not found in catalog. Try again.")


# ==========================
# TASK 2
# Student Grade Evaluator & Class Performance Tracker
# ==========================

def task2():
    print("\n========================================")
    print("TASK 2: STUDENT GRADE EVALUATOR")
    print("========================================")

    count = int(input("How many student entries do you want to create? "))
    student_records = {}

    for i in range(count):
        print(f"--- Entry {i + 1} ---")
        name = input("Enter student name: ")
        score = float(input("Enter score (0-100): "))
        student_records[name] = score

    print("========================================")
    print("EVALUATION RESULTS")
    print("========================================")

    total_passed = 0
    total_failed = 0
    total_score = 0

    for name, score in student_records.items():
        total_score += score

        if score >= 70:
            grade = "A"
            status = "Passed with Distinction"
            total_passed += 1
        elif score >= 50:
            grade = "B"
            status = "Passed"
            total_passed += 1
        else:
            grade = "F"
            status = "Needs Improvement"
            total_failed += 1

        print(f"- {name}: Score {score} | Grade {grade} | {status}")

    average_score = total_score / count

    print("========================================")
    print("CLASS PERFORMANCE")
    print("========================================")
    print(f"Average Score: {average_score}")
    print(f"Total Passed: {total_passed}")
    print(f"Total Failed: {total_failed}")
    print("========================================")


# ==========================
# TASK 3
# Backend Data Processing & User Audit Tool
# ==========================

def task3():
    print("\n========================================")
    print("TASK 3: BACKEND DATA PROCESSING & USER AUDIT TOOL")
    print("========================================")

    # Raw user records: (User ID, Name, Role, Is_Active, Login_Attempts)
    users = [
        (101, "Alice", "admin", True, 1),
        (102, "Bob", "member", True, 4),
        (103, "Charlie", "editor", False, 0),
        (104, "Diana", "admin", False, 6),
        (105, "Evan", "member", True, 2),
        (106, "Fiona", "guest", True, 0),
    ]

    total_active = 0
    total_inactive = 0
    total_flagged = 0

    for user_id, name, role, is_active, login_attempts in users:
        # Active Admin Processing
        if is_active and role == "admin":
            print(f"[GRANT] Full system access granted to {name} (ID: {user_id})")
            total_active += 1
        elif is_active and (role == "member" or role == "editor"):
            print(f"[GRANT] Standard access granted to {name} (ID: {user_id})")
            total_active += 1
        elif not is_active:
            print(f"[DENIED] Account {name} is inactive.")
            total_inactive += 1
        else:
            # Active but role not admin/member/editor (e.g. "guest")
            total_active += 1

        # Security Audit
        if login_attempts >= 5:
            print(f"[ALERT] Account {name} is LOCKED due to excessive failed logins ({login_attempts} attempts).")
            total_flagged += 1

    print("========================================")
    print("AUDIT SUMMARY REPORT")
    print("========================================")
    print(f"Total Active Users Granted: {total_active}")
    print(f"Total Inactive Accounts: {total_inactive}")
    print(f"Total Security Alerts: {total_flagged}")
    print("========================================")


# ==========================
# MAIN PROGRAM
# ==========================

if _name_ == "_main_":
    task1()
    task2()
    task3(
