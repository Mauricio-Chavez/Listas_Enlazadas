class node:
    def __init__(self,value):
        self.value=value
        self.next=None

class linkedList:
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
        def popfirst(self):
            if self.head is None:
                print("No hay nodo, no se puede ejecutar la operacion")

            else:
                tempo=self.head
                self.head=tempo.next
                tempo.next=None
                self.length-=1
        def remove(self, value):
            i = value
            tem = self.head
            dborrar = self.head
            if i > 0 and i <= self.length:
                if i == 1:
                    self.popfirst()
                if i > 1 and i < self.length:
                    for i in range(1, i):
                        dborrar = dborrar.next
                        i = value
                    for i in range(1, i - 1):
                        tem = tem.next

                    tem.next = dborrar.next
                    dborrar.next = None

                if i == self.length:
                    self.pop()

        def quitarEspacio(self):
            tem=self.head
            i=0
            while tem is not None:
                i+=1
                if tem.value==" ":
                    self.remove(i)

                tem=tem.next


            """if my_linked_list.length==my_linked_list2:
                while i<=self.length:
                    if
            else:
                print("La palabras ingresadas no son anagramas")"""

node1=linkedList()
node2=linkedList()
i=0
j=0
a=input(str(("Ingresa la palabra 1: ")))
b=input(str(("Ingresa la palabra 2: ")))
a=a.replace(" ","")
b=b.replace(" ","")
a=a.lower()
b=b.lower()
a=sorted(a)
b=sorted(b)
print(a)
print(b)
for i in a:
    node1.append(i)

for j in b:
    node2.append(j)

node1.print_list()
node2.print_list()
if node1.length==node2.length:
    aux1 = node1.head
    aux2 = node2.head
    cont = 0
    while aux1.next is not None:
        if aux1.value == aux2.value:
            cont += 1
            aux1 = aux1.next
            aux2 = aux2.next
        else:
            print("Las palabras ingresadas no son anagramas")
            exit()

    print("Las palabras ingresadas son anagramas")
else:
    print("Las palabras ingresadas no son anagramas")
"""while i !='.':
    i=str(input())
    my_linked_list.append(i)

my_linked_list.pop()
print("Ingresa tu palabra 2 letra por letra terminando con un .")
i='s'
while i !='.':
    i=str(input())
    my_linked_list2.append(i)
my_linked_list2.pop()"""




