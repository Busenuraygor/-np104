my_list=[1,12,7,3,5]
yeni_liste=[]
for i in range(1,len(my_list)):
  if my_list[i]> my_list[i-1]:
    yeni_liste.append(my_list[i])
    print(yeni_liste)
  
