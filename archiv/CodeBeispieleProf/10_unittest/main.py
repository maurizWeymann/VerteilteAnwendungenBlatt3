
# Demo für Unit - Test


def add(value_1 : float, value_2 : float) -> float:
    return value_1 + value_2

def mul(value_1 : float, value_2 : float) -> float:
    return value_1 * value_2

def sub(value_1 : float, value_2 : float) -> float:
    return 0.0

def main():
    value_1 = 10
    value_2 = 5
    
    print("Test für Unit - Test")
    print(f"{value_1=}, {value_2=}")
    print(f"Add: {add(value_1, value_2)=}")
    print(f"Mul: {mul(value_1, value_2)=}")
    print(f"Sub: {sub(value_1, value_2)=}")

if __name__ == '__main__':
    main()