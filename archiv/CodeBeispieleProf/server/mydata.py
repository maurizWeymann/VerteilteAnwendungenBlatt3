from pydantic import BaseModel

class MyInventoryElement(BaseModel):
    name : str
    quantity : int
    id : int = 0

class MyInventoryPostElement(BaseModel):
    name : str
    quantity : int






class MyInventory:
    def __init__(self):
        self.elements = list()
        self.id = 0

    def add_element(self, element : MyInventoryElement, put = False) -> int:
        if put and element.id > 0:
            self.id = element.id
        else:
            self.id += 1
            element.id = self.id
        
        self.elements.append(element)
        return element
    
    def remove_element(self, id : int) -> int:
        t_elements = self.elements[:]
        for t_element in t_elements:
            if t_element.id == id:
                self.elements.remove(t_element)
                return id
        return 0
    
    def get_elements(self) -> list:
        return self.elements
    
    def get_element(self, id : int) -> MyInventoryElement:
        for element in self.elements:
            if element.id == id:
                return element
        return 0
    
    # state 0 change, status 1 new
    def update_element(self, id : int, element : MyInventoryElement):
        state = 1
        t_elements = self.elements[:]
        print(id)
        for t_element in t_elements:
            if t_element.id == int(id):
                element.id = int(id)
                self.elements[self.elements.index(t_element)] = element
                state = 0
                print("done")
                return (state, element)
        
        element.id = int(id)
        element = self.add_element(element, True)
        return (state, element)
         
    def get_max_id(self) -> int:
        return self.id
    