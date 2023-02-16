class node:
    def __init__(self,value):
        self.value=value
        self.next=None


class linkedList:
        """def __init__(self,value):
        nuevo_Nodo=node(value)
        self.head=nuevo_Nodo
        self.tail=nuevo_Nodo
        self.length=1"""



        def __init__(self):
            self.head=None
        def print_list(self):
            temp = self.head
            """for i in range(self.length):
                print(temp.value)
                temp = temp.next"""
            while temp is not None:
                print(temp.value)
                temp=temp.next
        def append(self,value):
            if self.head is None:
                self.head=node(value)
                self.tail=self.head
                self.length=1
            else:
                self.tail.next=node(value)
                self.tail=self.tail.next
                self.length+=1
        def pop(self):
            if self.head is None:
                print("No existe nodo")
            if self.length==1:
                self.head=None
                self.tail=None
            else:
                tem=self.head
                while tem.next != self.tail:
                    tem=tem.next

                self.tail=tem
                self.tail.next=None
        def prepend(self,value):
            nuevo_nodo=node(value)
            if self.head is None:
                self.head=nuevo_nodo
                self.tail=self.head
                self.length+=1
            else:
                nuevo_nodo.next=self.head
                self.head=nuevo_nodo
                self.length+=1
        def popfirst(self):
            if self.head is None:
                print("No hay nodo, no se puede ejecutar la operacion")

            else:
                tempo=self.head
                self.head=tempo.next
                tempo.next=None
                self.length-=1
        def get(self,value):
            indice=value
            recorrer=self.head
            if indice<=self.length and indice>0:
                    for i in range(1,value):
                        recorrer=recorrer.next
                    print(recorrer.value)

            else:
                print("El indice indicado no existe")

        def insert(self,value,v):
            i=value
            d=v
            re=self.head
            new_nodo=node(d)
            if i>0 and i<=(self.length+1):
                if self.length==0:
                    new_nodo.next=None
                    self.head=new_nodo
                    self.tail=new_nodo
                    self.length+=1
                else:
                    if i ==1:
                        new_nodo.next=self.head
                        self.head=new_nodo
                        self.length += 1
                    if i==(self.length+1):
                        self.tail.next=new_nodo
                        print("entro")  #corregir
                        self.tail=new_nodo
                        self.length += 1
                    if i >1 and i <=self.length:
                        for i in range(1,i-1):
                            re=re.next
                        new_nodo.next=re.next
                        re.next=new_nodo
                        self.length += 1
            else:
                print("Los datos ingresados no son validos")

        def set (self,value,v):
            index=value
            da=v
            tem=self.head
            if self.length==0:
                new_nodo=node(v)
                self.head=new_nodo
                self.tail=new_nodo
            else:
                if index>0 and index<=self.length:
                    for j in range(1,index):
                        tem=tem.next

                    tem.value=da








my_linked_list=linkedList()
my_linked_list.append(4)
"""print("head",my_linked_list.head.value)
print("Tail",my_linked_list.tail.value)
print("Length",my_linked_list.length)"""
my_linked_list.append(5)
"""print("head",my_linked_list.head.value)
print("Tail",my_linked_list.tail.value)
print("Length",my_linked_list.length)"""
my_linked_list.append(2)
"""print("head",my_linked_list.head.value)
print("Tail",my_linked_list.tail.value)
print("Length",my_linked_list.length)"""
print("-------------------------------")
my_linked_list.print_list()
print("-------------------------------")
my_linked_list.pop()
my_linked_list.print_list()
print("-------------------------------")
my_linked_list.prepend(5)
my_linked_list.print_list()
print("-------------------------------")
my_linked_list.popfirst()
try:
    my_linked_list.print_list()
except:
    print("No existen nodos para imprimir")

print("-------------------------------")
my_linked_list.get(2)
print("-------------------------------")
my_linked_list.insert(1,3)
my_linked_list.print_list()
print("-------------------------------")
my_linked_list.set(1,10)
my_linked_list.print_list()


