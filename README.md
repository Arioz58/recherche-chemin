# Algorithme de Dijkstra

L'algorithme de Dijkstra est un algorithme de recherche de chemin le plus court dans un graphe pondéré. Il a été conçu par l'informaticien néerlandais Edsger Dijkstra en 1956 et publié en 1959.

## Principe de l'algorithme

L'algorithme de Dijkstra fonctionne en explorant tous les chemins possibles à partir d'un nœud de départ, en utilisant une file de priorité pour toujours explorer le chemin le plus court disponible à chaque étape. Voici les étapes principales :

1. **Initialisation** :
    - Assigner une valeur de distance infinie à tous les nœuds sauf le nœud de départ, qui reçoit une valeur de distance de 0.
    - Placer tous les nœuds dans une file de priorité.

2. **Traitement** :
    - Tant que la file de priorité n'est pas vide :
      - Extraire le nœud avec la plus petite valeur de distance.
      - Pour chaque voisin de ce nœud, calculer la distance totale depuis le nœud de départ.
      - Si cette distance est inférieure à la distance actuellement enregistrée pour ce voisin, mettre à jour la distance et ajouter le voisin à la file de priorité.

3. **Terminaison** :
    - L'algorithme se termine lorsque tous les nœuds ont été traités ou que le nœud de destination a été atteint.

## Exemple de code en Python

```python
import heapq

def dijkstra(graph, start):
     # Initialisation
     distances = {node: float('infinity') for node in graph}
     distances[start] = 0
     priority_queue = [(0, start)]
     
     while priority_queue:
          current_distance, current_node = heapq.heappop(priority_queue)
          
          if current_distance > distances[current_node]:
                continue
          
          for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                     distances[neighbor] = distance
                     heapq.heappush(priority_queue, (distance, neighbor))
     
     return distances

# Exemple d'utilisation
graph = {
     'A': {'B': 1, 'C': 4},
     'B': {'A': 1, 'C': 2, 'D': 5},
     'C': {'A': 4, 'B': 2, 'D': 1},
     'D': {'B': 5, 'C': 1}
}

start_node = 'A'
print(dijkstra(graph, start_node))
```

## Applications

L'algorithme de Dijkstra est utilisé dans divers domaines, notamment :
- Les systèmes de navigation GPS pour trouver le chemin le plus court.
- Les réseaux de télécommunications pour optimiser les routes de données.
- Les jeux vidéo pour le déplacement des personnages.

## Limitations

- L'algorithme de Dijkstra ne fonctionne que pour les graphes avec des poids d'arêtes non négatifs.
- Pour les graphes avec des poids négatifs, l'algorithme de Bellman-Ford est plus approprié.

## Références

- [Wikipedia: Algorithme de Dijkstra](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra)
- [GeeksforGeeks: Dijkstra’s shortest path algorithm](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)
