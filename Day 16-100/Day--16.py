from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"]), table.add_column("Type", ["Electric", "Water", "Fire"])

table.align["Type"] = "r" # "l" for left alignment, "r" for right and "c" for center
# or print(table.align) to simply print the table alignment out
# table.align = "l" to change entire table alignment

print(table)
