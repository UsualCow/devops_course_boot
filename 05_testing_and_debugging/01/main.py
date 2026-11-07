def total_xp(level, xp_to_add):
   total = level * 100 + xp_to_add
   return total

def main():
    
    level = int(input("Enter character level: "))
    xp_to_add = int(input("Enter XP to add: "))
    total = total_xp(level, xp_to_add)
    print(f"Total XP after adding {xp_to_add} to level {level}: {total}")

if __name__ == "__main__":
    main()

