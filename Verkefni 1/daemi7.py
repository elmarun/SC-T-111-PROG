years_str = input("Years: ") # do not change this line

years_int = int(years_str)

br = 1/7

dr = 1/13

imm = 1/35

gr = br + imm - dr

growth = gr * 60 * 60 * 24 * 365 * years_int

new_population = 307357870 + growth

print("New population after", years_int, " years is ", int(new_population)) # do not change this line