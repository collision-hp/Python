import copy
Original_list=[['Shallow', 2, 3], [4, 5, 6]] 
Swallow_Copy=copy.copy(Original_list)
Deep_Copy=copy.deepcopy(Original_list)
Swallow_Copy[0][0]="Done"#changes are applied both in original_list and swallow_copy
Deep_Copy[0][0]=[21,34,23] #changes are made just in deep_copy
print(Original_list)
print(Swallow_Copy)
print(Deep_Copy)