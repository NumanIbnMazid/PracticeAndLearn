# Lambda Function 

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

print(full_name("Numan", "Mazid"))

authors = [
    "Numan Mazid", "Sabiha Disha", "Nishi Khatun", "Mehedi Bivan", "Mehedi Moinul", "Abir Hasan",
    "S.G Wellafare", "Kazi Shouhardo Sonnet", "Miss Nazrana"
]

print(authors)

authors.sort(key = lambda name: name.split(" ")[-1].lower())

print(authors)

