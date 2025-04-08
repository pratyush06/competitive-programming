# After centuries of hostilities and skirmishes between the four nations living in the land generally known
#  as Nlogonia, and years of negotiations involving diplomats, politicians and the armed forces of all
#  interested parties, with mediation by UN, NATO, G7 and SBC, it was at last agreed by all the way to
#  end the dispute, dividing the land into four independent territories.
#  It was agreed that one point, called division point, with coordinates established in the negotiations,
#  would define the country division, in the following way. Two lines, both containing the division point,
#  one in the North-South direction and one in the East-West direction, would be drawn on the map,
#  dividing the land into four new countries. Starting from the Western-most, Northern-most quadrant,
#  in clockwise direction, the new countries will be called Northwestern Nlogonia, Northeastern Nlogonia,
#  Southeastern Nlogonia and Southwestern Nlogonia.

#   Input
#  The input contains several test cases. The first line of a test case contains one integer K indicating
#  the number of queries that will be made (0 < K ≤ 103). The second line of a test case contains two
#  integers N and M representing the coordinates of the division point (−104 < N,M < 104). Each
#  of the K following lines contains two integers X and Y representing the coordinates of a residence
#  (−104 ≤ X,Y ≤104).
#  The end of input is indicated by a line containing only the number zero.
#  Output
#  For each test case in the input your program must print one line containing:
#  • the word ‘divisa’ (means border in Portuguese) if the residence is on one of the border lines
#  (North-South or East-West);
#  • ‘NO’ (means NW in Portuguese) if the residence is in Northwestern Nlogonia;
#  • ‘NE’ if the residence is in Northeastern Nlogonia;
#  • ‘SE’ if the residence is in Southeastern Nlogonia;
#  • ‘SO’ (means SW in Portuguese) if the residence is in Southwestern Nlogonia.

while True:
    k = int(input())
    if not k:
        break
    n, m = map(int, input().split())
    for _ in range(k):
        x, y = map(int, input().split())
        if x == n or y == m:
            print("divisa")
        else:
            print("N" if y > m else "S" + "O" if x < n else "E")