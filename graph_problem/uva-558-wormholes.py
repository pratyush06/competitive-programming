import sys

def solve():
    # Helper to get input word by word
    def get_input():
        for line in sys.stdin:
            for word in line.split():
                yield word
    
    input_gen = get_input()
    
    try:
        # Get number of test cases
        line = next(input_gen, None)
        if line is None:
            return
        num_test_cases = int(line)
        
        for _ in range(num_test_cases):
            n = int(next(input_gen))  # Number of star systems
            m = int(next(input_gen))  # Number of wormholes
            
            edges = []
            for _ in range(m):
                u = int(next(input_gen))
                v = int(next(input_gen))
                t = int(next(input_gen))
                edges.append((u, v, t))
            
            # Bellman-Ford Algorithm
            dist = [float('inf')] * n
            dist[0] = 0
            
            for i in range(n - 1):
                changed = False
                for u, v, t in edges:
                    if dist[u] != float('inf') and dist[u] + t < dist[v]:
                        dist[v] = dist[u] + t
                        changed = True
                if not changed:
                    break
            
            has_negative_cycle = False
            for u, v, t in edges:
                if dist[u] != float('inf') and dist[u] + t < dist[v]:
                    has_negative_cycle = True
                    break
            
            # Print result immediately for this test case
            if has_negative_cycle:
                print("possible")
            else:
                print("not possible")
                
    except EOFError:
        pass
    except StopIteration:
        pass

if __name__ == "__main__":
    solve()