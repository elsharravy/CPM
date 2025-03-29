import node_class

tab1 = [1,2]
tab2 = [3,4]

n = node_class.node(0, 2, 2, "test", 2, 2, 4, tab1, tab2)

print("test: " + n.get_n())

n.set_n("test2")
      
print("test: " + n.get_n())

