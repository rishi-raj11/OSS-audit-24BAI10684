import os
import pwd
import grp

def user_group_report():
    print("=== USERS & GROUPS ===")
    for user in pwd.getpwall():
        print(f"User: {user.pw_name}, UID: {user.pw_uid}, GID: {user.pw_gid}")
    print("\n=== GROUPS ===")
    for group in grp.getgrall():
        print(f"Group: {group.gr_name}, GID: {group.gr_gid}, Members: {', '.join(group.gr_mem)}")

if __name__ == "__main__":
    user_group_report()
