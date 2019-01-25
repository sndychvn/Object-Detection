#from ImageDetection import final_classID
from collections import Counter


class Count:
    def yimage_conf_out(final):

        object_name = ['motorbike', 'person', 'bus', 'truck', 'bicycle', 'car', 'suitcase']
        file1 = open("Object_Number.txt", "r+")
        obj9 = file1.read().split()
        for vari in object_name:
            #print(final)
            # print(obj9.index(object_name))
            #print(obj9)
            ind = obj9.index(vari)
            # print(obj9[final[0]])
            print(obj9[ind])
            cobj = Counter(final)
            print(cobj[ind])
            # print(cobj[final[0]])

            # if (obj9[final[0]])


















