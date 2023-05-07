#!/usr/bin/env python
# coding: utf-8

# In[1]:


cities = [['Myrhorod', 'Hadiach', 61],
          ['Hadiach', 'Zavodske', 67],
          ['Zavodske', 'Romny', 71],
          ['Romny', 'Hadiach', 71],
          ['Hadiach', 'Lokhvytsia', 81],
          ['Lokhvytsia', 'Vorozhba', 94],
          ['Vorozhba', 'Hadiach', 91]]


# In[2]:


import networkx as nx


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


G = nx.Graph()


# In[5]:


cities = ['Myrhorod', 'Hadiach', 'Zavodske', 'Romny', 'Lokhvytsia', 'Vorozhba']
G.add_nodes_from(cities)


# In[6]:


edges = [('Myrhorod', 'Hadiach', 61), 
         ('Hadiach', 'Zavodske', 67), 
         ('Zavodske', 'Romny', 71), 
         ('Romny', 'Hadiach', 71), 
         ('Hadiach', 'Lokhvytsia', 81), 
         ('Lokhvytsia', 'Vorozhba', 94), 
         ('Vorozhba', 'Hadiach', 91)]

for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])


# In[7]:


pos = nx.spring_layout(G) 
nx.draw(G, pos, with_labels=True) 
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()


# In[8]:


import heapq

def shortest_path(graph, start, end):
    distances = {city: float('inf') for city in graph}
    distances[start] = 0

    heap = [(0, start)]
    path = {}

    while heap:
        (current_distance, current_city) = heapq.heappop(heap)

        if current_city == end:
            route = []
            while current_city in path:
                route.append(current_city)
                current_city = path[current_city]
            route.append(start)
            route.reverse()
            return (route, current_distance)

        if current_distance > distances[current_city]:
            continue

        for neighbor, distance in graph[current_city].items():
            distance_to_neighbor = current_distance + distance

            if distance_to_neighbor < distances[neighbor]:
                distances[neighbor] = distance_to_neighbor
                heapq.heappush(heap, (distance_to_neighbor, neighbor))
                path[neighbor] = current_city

    return None


# In[ ]:




