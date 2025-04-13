import node_class
import Compiler_class

tab1 = []
tab2 = [0]
tab3 = [0]
tab4 = [1,2]

n = node_class.node(2, "test", tab1 ,0, 2, 2, 2, 4, tab2)

print("test: " + n.get_n())

n.set_n("test2")
      
print("test: " + n.get_n())



n2 = node_class.node(2, "test", 2)

print("test: " + str(n2.get_es()))

n2.set_es(2)
      
print("test2: " + str(n2.get_es()))


n1 = node_class.node(1, "a", tab1 )
n2 = node_class.node(2, "b", tab2 )
n3 = node_class.node(5, "c", tab3 )
n4 = node_class.node(3, "d", tab4 )

nodes = [n1,n2,n3,n4]

nodes = Compiler_class.Compiler.Compile(nodes)
#c(nodes)

print("c : " + str(nodes[2].late_start))
for x in nodes:
    print("nazwa: " + str(x.get_n()) + "    es: "+ str(x.get_es()) + "    ls: "+ str(x.get_ls())+ "    ef: "+ str(x.get_ef()) + "    lf: "+ str(x.get_lf()) + "    rezerwa: " + str(x.get_r()) + "\n")