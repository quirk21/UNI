N = int(input())
words = [input() for _ in range(N)]
graph = {}
all_char = set()
for word in words:
    for c in word:
        graph[c] = set()
        all_char.add(c)
visited = {}
path = []

# creating graph
def graph_building(graph, N):
    for i in range(N-1):
        min_len = min(len(words[i]), len(words[i+1]))
        if len(words[i]) > len(words[i+1]) and words[i].startswith(words[i+1]):
            return True
        for j in range(min_len):
            if words[i][j] != words[i+1][j]:
                graph[words[i][j]].add(words[i+1][j])
                break
    return False

def topo_sort(graph, visited, root, stack):
        visited[root] += 1 
        for nx in sorted(graph[root]):
            if nx not in visited:
                visited[nx] = -1 
                if topo_sort(graph, visited, nx, stack): return True
            elif visited[nx] == 0: return True
        visited[root] += 1
        stack.append(root)
        return False

def main():
    bool = graph_building(graph, N)
    for i in sorted(all_char, reverse= True):
        if i not in visited: 
            visited[i] = -1
            if topo_sort(graph, visited, i, path): return True
    return bool

if main() : 
    for i in range(len(path)-1,-1,-1): print(path[i],end="")
else:
    print(-1)