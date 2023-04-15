
# Convert the given edge list to the adjacency matrix of an undirected connected graph.
# The adjacency matrix is a matrix with rows and columns labeled by graph vertices,
# with a 1 or 0 in position (u, v) according to whether vertices u and v are adjacent or not.

# if an edge is [0, 1], then in adj_matrixm,  m[0][1] = 1 and m[1][0]= 1, if undirected and m[0][1] = 1 if directed.
#* Time: O(e).
#* Auxiliary space: O(1).
#* Total space: O(n * n).
def convert_edge_list_to_adjacency_matrix(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     list_list_bool
    """
    # Write your code here.
    matrix = [[0 for _ in range(n)] for _ in range(n)] # here range(n) is used instead of range(len(edges)) as edges can be 0
                                                        # as in second test case.
    for i in range(len(edges)):
        matrix[edges[i][0]][edges[i][1]] = 1
        matrix[edges[i][1]][edges[i][0]] = 1
    return matrix


print(convert_edge_list_to_adjacency_matrix(5, [[0, 1],[1, 4],[1, 2],[1, 3],[3, 4]]))
print(convert_edge_list_to_adjacency_matrix(1, []))



def convert_edge_list_to_adjacency_matrix(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     list_list_bool
    """
    # Write your code here.
    #return []
    adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i,j in edges:
        adj_matrix[i][j] = 1
        adj_matrix[j][i] = 1
    return adj_matrix

print(convert_edge_list_to_adjacency_matrix(5, [[0, 1], [1, 4], [1, 2], [1, 3], [3, 4]]))
#print(convert_edge_list_to_adjacency_matrix(1, []))
# [[0, 1, 0, 0, 0],
#  [1, 0, 1, 1, 1],
#  [0, 1, 0, 0, 0],
#  [0, 1, 0, 0, 1],
#  [0, 1, 0, 1, 0]]