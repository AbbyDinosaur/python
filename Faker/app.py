import faker
fake = faker.Faker()

def generate_fake_user():
    return fake.name(), fake.address(), fake.email(), fake.phone_number()

for _ in range (5):
    username, address, email, phone = generate_fake_user()
    print (f"name   : {username}")
    print (f"address   : {address}")
    print (f"email   : {email}")
    print (f"phone   : {phone}")
    print()