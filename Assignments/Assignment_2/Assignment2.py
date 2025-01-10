def stars(rows, stars):
    for i in range(rows):
        print("*" * stars)

num_lines = int(input("Enter the number of lines: "))
num_stars = int(input("Enter the number of stars in each line: "))
    
stars(num_lines, num_stars)

