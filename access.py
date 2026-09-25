name="admin"
has_access=True

if name=="admin" and has_access==True:
    print("access granted")

else:
    print("Access denied.")

#logical operator with conditions

day=input("Enter today's day:")

if day=="saturday" or day=="sunday":
    print("Weekend")

else:
    print("Week day")