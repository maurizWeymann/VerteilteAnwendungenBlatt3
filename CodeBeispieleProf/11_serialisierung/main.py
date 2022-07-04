from dataclasses import dataclass
import pickle

@dataclass
class MyData():
    name: str
    count: int
    sales: float


def pickle_demo():
    print("=========== Pickle (Binary)")
    myd = MyData("cat", 3, 80.9)
    print(f"Type: {type(myd)} : Data: {myd}")

    dump_serialize = pickle.dumps(myd, protocol=pickle.HIGHEST_PROTOCOL)
    dump_serialize_hex = dump_serialize.hex()
    print(dump_serialize_hex)
    myd = None

    myd = pickle.loads(bytes.fromhex(dump_serialize_hex))
    print(f"Type: {type(myd)} : Data: {myd}")

def pickle_demo_list():
    print("=========== Pickle (Binary) List")
    myd_list = []
    
    #myd = 
    myd_list.append(MyData("cat", 3, 80.9))
    myd_list.append(MyData("dog", 1, 180.9))
    myd_list.append(MyData("mouse", 30, 2.02))
    
    print(f"Type: {type(myd_list)} : Data: {myd_list}")

    dump_serialize = pickle.dumps(myd_list, protocol=pickle.HIGHEST_PROTOCOL)
    dump_serialize_hex = dump_serialize.hex()
    print(dump_serialize_hex)
    myd_list = None

    myd_list = pickle.loads(bytes.fromhex(dump_serialize_hex))
    print(f"Type: {type(myd_list)} : Data: {myd_list}")


def main():
   pickle_demo()
   pickle_demo_list()
  
if __name__ == '__main__':
    main()