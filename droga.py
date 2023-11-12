def wyszukania_wezla (graf,wezel):
    for i in graf :
        if i[0]==wezel:
            return i[1]
        else:
            return None 
def shortest_path(graf):
    all_path_a=[]
    
