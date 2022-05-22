from xml.dom.minidom import parse
import xml.dom.minidom
import numpy as np
import re
import matplotlib.pyplot as plt
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")

total_list =[]
translation_list = []
number_of_terms = 0

#calculate the overall terms using "for" statement. And calculate the overall childnodes by listing "is_a" elements.
for term in terms:
    number_of_terms+=1
    childnodes = term.getElementsByTagName("is_a")
    number_of_childnodes = len(childnodes)
    total_list.append(number_of_childnodes)

#report the total number of terms
a = "the total number of terms currently recorded in the Gene Ontology is: "
print(a+str(number_of_terms))

#calculate the overall terms related to translation by listing "defstr" elements. And calculate the overall childnodes related to translation by listing "is_a" elements. 
for term in terms:
    defstr = term.getElementsByTagName("defstr")[0]
    defstr_text = str(defstr.childNodes[0].data)
    if re.findall("translation",defstr_text):
        childnodes_translation = term.getElementsByTagName("is_a")
        number_of_childnodes_translation = len(childnodes_translation)
        translation_list.append(number_of_childnodes_translation)

#print a boxplot describing the distribution of childnodes
plt.boxplot(total_list,labels = ["Gene Ontology"])
plt.title("The distribution of childnodes across terms in the Gene Ontology")
plt.xlabel("terms")
plt.ylabel("the number of childnodes")
plt.show()

#print a boxplot describing the distribution of childnodes related to translation.
plt.boxplot(translation_list,labels = ["translation Gene Ontology"])
plt.title("The distribution of childnodes across terms associated with translation")	            
plt.xlabel("terms with translation")
plt.ylabel("the number of childnodes")
plt.show()

#calculate and compare the average childnodes between the overall GO and the "translation" terms
total_average = sum(total_list)/len(total_list)
translation_average = sum(translation_list)/len(translation_list)
x = "The translation terms contain, on average, a smaller number of childnodes than the overall Gene Ontology."
y = "The translation terms contain, on average, a greater number of childnodes than the overall Gene Ontology."
if total_average>translation_average:
    print(x)
if total_average<translation_average:
    print(y)
#The translation terms contain, on average, a great number of childnodes than the overall Gene Oncology.
