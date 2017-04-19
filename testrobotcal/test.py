def person(name, age, *args, city, job):
    print(name, age, args, city, job)

person('Jack', 24, 1,1, city = 'Beijing', job = 'Engineer')