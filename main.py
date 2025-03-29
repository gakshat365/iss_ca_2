def find_cube_pairs(targ): # Fixed missing colon and incorrect variable name
    sol = []; # Fixed incorrect list initialization
    max_num = round(targ ** (1/3)) # Fixed incorrect variable name and exponentiation syntax 

    for a in range(1, max_num + 1): # Fixed 'ranges' to 'range' and added colon
        for b in range(a, max_num + 1): # Fixed 'ranges' to 'range' and added colon
            if a**3 + b**3 == targ: # Fixed incorrect exponentiation syntax
                sol.append((a, b)); # Fixed incorrect variable names and list append
    return sol

pairs = find_cube_pairs(1729) # Fixed variable name typo and removed unnecessary comma

print("Valid cube pairs for 1728:") # Fixed incorrect 'printf' syntax
for a, b in pairs: # Fixed incorrect variable name 'pair' → 'pairs' andd added :
    print(f" → {a}³ + {b}³ = {a**2} + {b**2} = 1728")# Fixed incorrect exponentiation