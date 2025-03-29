import node_class

tab1 = [1,2]
tab2 = [3,4]

n = node_class.node(2, "test", tab1 ,0, 2, 2, 2, 4, tab2)

print("test: " + n.get_n())

n.set_n("test2")
      
print("test: " + n.get_n())



n2 = node_class.node(2, "test", 2)

print("test: " + str(n2.get_es()))

n2.set_es(2)
      
print("test2: " + str(n2.get_es()))

