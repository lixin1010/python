import sys

# f = open("hero", "r", encoding="utf-8")
# f_new = open("hero.bak", "w", encoding="utf-8")

find_str = sys.argv[1]
replace_str = sys.argv[2]

with open("hero", "r", encoding="utf-8") as f, \
        open("hero.bak", "w", encoding="utf") as f_new:
    for line in f:
        if find_str in line:
            line = line.replace(find_str, replace_str)
        f_new.write(line)

# f.close()
# f_new.close()
