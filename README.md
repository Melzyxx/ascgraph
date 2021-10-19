# Ascgraph
## Консольная графика на python

Install `pip3 install ascgraph`

---
Usage
```Python
import ascgraph

# Create map 20x20
map = ascgraph.ascgraph(20, 20, "#")

# Create point x: 3, y: 14
map.point(3, 14, "O") 

# Create rect x1: 5, y1:5, x2: 15, y2:15
map.rect(5, 5, 15, 15, "O")

# Create line x1: 0, y1: 0, x2: 20, y2: 20
map.line(0, 0, 20, 20, "O")

# Print map
print(str(map))

# Clear map
map.clear()
```
