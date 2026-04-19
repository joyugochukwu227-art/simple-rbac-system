# Simple RBAC Implementation

users = {
    "Alice": "admin",
    "Bob": "editor",
    "Charlie": "viewer"


permissions = {
    "admin": ["create", "read", "update", "delete"],
    "editor": ["create", "read", "update"],
    "viewer": ["read"]


def check_access(user, action):
    role = users.get(user)

    if not role:
        print(f"User '{user}' does not exist.")
        return

    if action in permissions[role]:
        print(f"Access granted: {user} can {action}.")
    else:
        print(f"Access denied: {user} cannot {action}.")


# --TEST RESULTS 
print("=== RBAC TEST RESULTS ===")

check_access("Alice", "create")
check_access("Bob", "delete")
check_access("Charlie", "read")
check_access("Dave", "read")
