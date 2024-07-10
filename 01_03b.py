from collections import Counter

def main():
    #Add code here
    inventory = Counter(STA001=10, SAL002=20, ENT004=13)
    print(inventory)

    #sell 5 starters, 3 salads, and 3 entrees
    remove_counts = Counter(STA001=5, SAL002=3, ENT004=3)
    inventory -= remove_counts 
    print(inventory)

    #make 9 more starters and 1 more entree
    add_counts = Counter(STA001=9, ENT004=1)
    inventory += add_counts
    print(inventory)

if __name__ == "__main__":
    main()