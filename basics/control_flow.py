is_admin = True
password = 'admin123'

if is_admin:
    print("Access granted.")
    if password == 'admin123':
        print("Welcome, admin!")
else:
    print("Access denied.")
    
score = 85
if score >=90:
    print("Excellent performance!")
elif score >= 75:
    print("Good job!")