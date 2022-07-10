# Stand: 10.10.21
# Beispiele für komplexe Datentypen

# Tuples, nicht Veränderbar
my_tuple = (1, 2, 3, 4, 5, 6, 7)

# Dictionary
my_dict = {
    "entry" : 64,
    "other" : 88,
    "name"  : "Name"
} 

# Listen
my_list = ["Wert1", "Wert2", "WertN"]

# main program
def main():
    my_tuple1 = my_tuple
    print(my_tuple1[:3]) # ab element : bis element

    my_dict1 = my_dict
    print(my_dict1)
    my_dict["entry"] = 9999
    
    print(my_dict1)
    my_dict2 = my_dict.copy()
    my_dict["entry"] = 7777
    print("Referenz:", my_dict2)
    print("Copy: ", my_dict1)

    my_list.append("WertY")
    my_list.remove("Wert1")
    
    
if __name__ == "__main__":
    main()