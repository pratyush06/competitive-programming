while True:
    try:
        # Read input line
        list_of_number = list(map(int, input().split()))
        n = list_of_number[0]
        sequence = list_of_number[1:]

        # Check if sequence length matches n
        if len(sequence) != n:
            print("Not jolly")
            continue
        
        # Handle n = 1 case
        if n == 1:
            print("Jolly")
            continue
        
        # Handle n <= 0 or invalid cases
        if n <= 0:
            print("Not jolly")
            continue

        # Calculate absolute differences
        diffs = set(abs(sequence[i+1] - sequence[i]) for i in range(n - 1))
        
        # Check if differences match {1, 2, ..., n-1}
        expected = set(range(1, n))
        print("Jolly" if diffs == expected else "Not jolly")

    except EOFError:
        break
    except ValueError:
        # Handle invalid input (e.g., non-integer values)
        print("Not jolly")
    except IndexError:
        # Handle cases where input is empty or insufficient
        print("Not jolly")
