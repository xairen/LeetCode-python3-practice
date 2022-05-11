class Solution:
	def flipgame(self, fronts: List[int], backs: List[int])) -> int:
	nopickbro = set() #i have a set 
	for i in range(len(fronts)): 
		if fronts[i] == backs[i]: #check if they the same or not
			nopickbro.add(fronts[i]) #add it to the set
		res=float('inf') #upperbound thingy INFINTE BABY

	for x in (fronts+backs): #CHECK IN EVERYTHING
		if x not in nopickbro: #it should not be the same as any front number
			res = min(res, x)

	return res if res!=float('inf') else 0

