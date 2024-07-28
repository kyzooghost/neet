
// Tree - undirected graph that is connected, and has no cycles
// Tree with n nodes, 1 to n. 1 additional edge added
// There is one redundant edge that creates a cycle
// If you find the cycle edges, place them into a hashmap, then iterate backwards in edges until you find a match
// Undirected graph hmm....
// No repeated edges
// How do DFS through an undirected graph -> mark both directions?
// Just start DFS from one node -> if revisit then have cycle

// Sigh, union-find is 25% runtime, 39% memory
// 'if there are multiple answers', I'm not sure if there are multiple answers so no worries
function findRedundantConnection_V3(edges: number[][]): number[] {
    // Each node start as its own island of 1
    const parent: number[] = [];
    const size: number[] = [];
    const n = edges.length;

    for (let i = 0; i < n + 1; i++) {
        parent.push(i);
        size.push(1);
    }

    // Find parent
    function find(i: number) {
        if (parent[i] != i) {
            parent[i] = find(parent[i]);
        }
        return parent[i];
    }

    function union(i: number, j: number) {
        // First find root of each node, are they the same island?
        const i_root = find(i);
        const j_root = find(j);
        if (i_root == j_root) return;
        // If not same island, then merge smaller island into bigger island
        // Smaller island root change to bigger island root
        if (size[i] > size[j]) {
            size[i] += size[j];
            parent[j_root] = i_root;
        } else {
            size[j] += size[i];
            parent[i_root] = j_root;
        }
    }

    for (const [u, v] of edges) {
        if (find(u) == find(v)) return [u, v];
        union(u, v);
    }

    return [];
}

// Took comment in Neet video mm, but doesn't improve time or memory ranking. Is TypeScript just cursed for Leetcode?
function findRedundantConnection_V2(edges: number[][]): number[] {
    const n = edges.length;
    const visited = new Set<number>();
    // Cast edges to 2D array
    const directedEdges: number[][] = []

    for (let i = 0; i < n + 1; i++) {
        directedEdges[i] = [];
        for (let j = 0; j < n + 1; j++) {
            directedEdges[i][j] = 0;
        }
    }

    for (const edge of edges) {
        directedEdges[edge[0]][edge[1]] = 1
        directedEdges[edge[1]][edge[0]] = 1
    }
    // Start dfs from node 1
    // Maintain queue of visited -> dequeue until reach prior number

    function dfs(node: number, _visited: Set<number>, _directedEdges: number[][]): boolean {
        // Cycle found
        if (_visited.has(node)) {
            for (const val of _visited) {
                if (val == node) break;
                _visited.delete(val);
            }
            return true;
        }

        _visited.add(node);

        // for (const i of _directedEdges[node]) {
        for (let i = 1; i < n + 1; i++) {
            if (_directedEdges[node][i] != 0) {
                // Consume edge
                _directedEdges[node][i] = 0;
                _directedEdges[i][node] = 0;
                if (dfs(i, _visited, _directedEdges)) return true
            }
        }
        _visited.delete(node);
        return false;
    }

    dfs(1, visited, directedEdges);

    // Iterate through found cycle
    let i = n - 1;
    while (i >= 0) {
        const [u, v] = edges[i];
        if (visited.has(u) && visited.has(v)) return edges[i];
        i -= 1
    }
    return edges[i];
};


// Lol so bad....I gotten so rusty in a week of no Leetcode
// 6% runtime, 6% memory in 50 minutes
// Look at this implementation...70 lines wtf
// I think I have the correct idea of finding a cycle, but I need a much cleaner implementation
function findRedundantConnection(edges: number[][]): number[] {
    const n = edges.length;
    const visited = new Set<number>();
    // Cast edges to 2D array
    const directedEdges: number[][] = []

    for (let i = 0; i < n + 1; i++) {
        directedEdges[i] = [];
        for (let j = 0; j < n + 1; j++) {
            directedEdges[i][j] = 0;
        }
    }

    for (const edge of edges) {
        directedEdges[edge[0]][edge[1]] = 1
        directedEdges[edge[1]][edge[0]] = 1
    }
    // Start dfs from node 1
    // Maintain queue of visited -> dequeue until reach prior number

    const path: number[] = [];
    function dfs(node: number, _visited: Set<number>, _path: number[], _directedEdges: number[][]): boolean {
        _path.push(node);
        // Cycle found
        if (_visited.has(node)) {
            return true;
        }

        _visited.add(node);

        // for (const i of _directedEdges[node]) {
        for (let i = 1; i < n + 1; i++) {
            if (_directedEdges[node][i] != 0) {
                // Consume edge
                _directedEdges[node][i] = 0;
                _directedEdges[i][node] = 0;
                if (dfs(i, _visited, _path, _directedEdges)) return true
            }
        }
        _path.pop();
        return false;
    }

    dfs(1, visited, path, directedEdges);

    while (path[0] != path[path.length - 1]) {
        path.shift();
    }

    // Re-initialize directedEdges
    for (let i = 0; i < n + 1; i++) {
        directedEdges[i] = [];
        for (let j = 0; j < n + 1; j++) {
            directedEdges[i][j] = 0;
        }
    }

    for (let j = 0; j < path.length - 1; j++) {
        const a = path[j]
        const b = path[j+1]
        directedEdges[a][b] = 1;
        directedEdges[b][a] = 1;
    }

    // Iterate through found cycle
    let i = n - 1;
    while (i >= 0) {
        if (directedEdges[edges[i][0]][edges[i][1]] == 1) return edges[i];
        i -= 1
    }
    return edges[i];
};

// const edges = [[1,2],[1,3],[2,3]]
const edges = [[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]];
console.log(findRedundantConnection_V3(edges)); // [2,8]