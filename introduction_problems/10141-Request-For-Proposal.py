first_case = True
count = 0
# given WA bcz we put count inside while condition which cause to give count 1 for every iteration
while True:
    # Read number of requirements and proposals
    rep, proposal = map(int, input().split())
    
    # Exit condition
    if rep == 0 and proposal == 0:
        break
    
    count += 1
    
    # Skip requirement names
    for _ in range(rep):
        input()
    
    proposals = []
    # Read proposals
    for _ in range(proposal):
        prop_name = input().strip()  # Remove any trailing whitespace
        price, req_ment = input().split()  # Read as string first
        price = float(price)  # Convert price to float
        req_ment = int(float(req_ment))  # Convert req_ment to int
        # Skip requirement names for this proposal
        for _ in range(req_ment):
            input()
        compliance_score = req_ment / rep  # Calculate compliance
        proposals.append((prop_name, price, compliance_score))
    
    # Sort proposals: higher compliance, lower price
    # Python's sort is stable, so input order is preserved for ties
    proposals.sort(key=lambda x: (-x[2], x[1]))
    
    # Print blank line before all cases except the first
    if not first_case:
        print()
    first_case = False
    
    # Output result
    print(f"RFP #{count}")
    print(proposals[0][0])