from re import A
import node_class


class Compiler(object):
    def __init__(self):
        a=0
# expects previous attribute in nodes to be array of indices of nodes being previous to it
    @staticmethod
    def Compile(nodes):
        leng = len(nodes)
        
        ne_tab = list(range(leng))
        for i in range(leng):
            ne_tab[i] = 0
        for i in range(leng):
            for x in (nodes[i]).previous:
                ne_tab[x] +=1
        for i in range(leng): 
            (nodes[i]).next =list()
        
        

        for i in range(leng):
            for x in (nodes[i]).previous:
                nodes[x].next.append(i)
        """   
        for i in range(leng): 
            print("node " + str(i) + ":")
            #(nodes[i]).next =list(range(ne_tab[i]))
            for j in range(len(nodes[i].next)):
                print(" " + str(nodes[i].next[j]))
                #(nodes[i]).next.append(ne_tab[j])
        for i in range(leng): 
            print("node " + str(i) + ":")
            #(nodes[i]).next =list(range(ne_tab[i]))
            for j in range(len(nodes[i].previous)):
                print(" " + str(nodes[i].previous[j]))
                #(nodes[i]).next.append(ne_tab[j])
        """
        for i in range(leng):
            max_e = 0
            for x in (nodes[i]).previous:
                if(max_e<nodes[x].early_finish):
                    max_e = nodes[x].early_finish
            (nodes[i]).early_start = max_e
            (nodes[i]).early_finish = (nodes[i]).early_start + (nodes[i]).duration
        
        for i in range(leng):
            k =leng - i -1
            if(len(nodes[k].next) == 0):
                min_l = nodes[k].early_finish
            else:
                min_l = nodes[nodes[k].next[0]].late_start
                for x in (nodes[k]).next:
                    if(min_l>nodes[x].late_start):
                        min_l = nodes[x].late_start
            (nodes[k]).late_finish = min_l
            (nodes[k]).late_start = (nodes[k]).late_finish - (nodes[k]).duration
            (nodes[k]).reserve = (nodes[k]).late_start - (nodes[k]).early_start
        return nodes
            



