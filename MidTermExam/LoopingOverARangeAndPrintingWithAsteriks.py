def print_number_pyramid():
    """
    Bu funksiya 1-dən 10-a qədər olan ədədləri piramida şəklində çap edir.
    Hər sətrin əvvəlində və sonunda ulduz (*) simvolları əlavə olunur.
    """
    n = 10  # Piramidanın hündürlüyü (sətir sayı)

    for i in range(1, n + 1):  # 1-dən 10-a qədər dövr edir
        spaces = ' ' * (n - i)  # Sol tərəfdə boşluqlar
        numbers = ' '.join(str(num) for num in range(1, i + 1))  # Rəqəmləri birləşdiririk
        padding = '*' * (n - i)  # Ulduzlarla bəzək
        print(f"{padding}{spaces}{numbers}{spaces}{padding}")  # Çap edirik

# Piramidanı ekrana çap edirik
print_number_pyramid()