def countLatticePoints(self, A: List[List[int]]) -> int:
	ans = set()
	for x,y,r in A:
		for cx in range(x + 1, x + r + 1):
			for cy in range(y + 1, y + r + 1):
				if math.sqrt((cx-x)**2 + (cy-y)**2) <= r:
					ans.add((cx, cy))
					ans.add((2*x-cx, cy))
					ans.add((2*x-cx, 2*y-cy))
					ans.add((cx, 2*y-cy))
		for cy in range(y-r,y+r+1): ans.add((x,cy))
		for cx in range(x-r,x+r+1): ans.add((cx,y))
	return len(ans)