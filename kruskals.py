import collections
import math

class GraphCluster:
	def __init__(self, *edges):
		self.edges = set(edges)
		self.vertices = set()

		for e in edges:
			for v in e:
				self.vertices.add(v)

class KruskalsClusterer:
	def __init__(self, n = 1):
		self.n = n

	def __call__(self, *points):
		# compute distances

		distances_dict = {}

		for p1 in points:
			for p2 in points:
				if p1 is p2:
					continue
				distances_dict[tuple(sorted((p1, p2)))] = abs(p1 - p2)
		# sort distances

		distances = sorted(distances_dict.items(), key = lambda e: e[1])
		del distances_dict
		# compute clusters

		clusters = set()
		for p in points:
			gc = GraphCluster()
			gc.vertices.add(p)
			clusters.add(gc)

		for d in distances:
			edge, distance = d
			print('P1: ', edge[0][0],edge[0][1] , 'P2 ', edge[1][0],edge[1][1], 'D ', distance)
			# check # of clusters

			if len(clusters) <= self.n:
				break
			# check each cluster to see if points from edge are in any of them

			c0 = None
			c1 = None

			for c in clusters:
				# break out early if possible

				if c0 != None and c1 != None:
					break

				if edge[0] in c.vertices:
					c0 = c

				if edge[1] in c.vertices:
					c1 = c
			# Case 1: points in the same cluster

			if c0 == c1:
				continue
			# Case 2: points in unique clusters

			else:
				# add new edge & vertexes to 0

				c0.edges.add(edge)
				c0.vertices.add(edge[1])
				# merge c1 into c0

				for e in c1.edges:
					c0.edges.add(e)

				for v in c1.vertices:
					c0.vertices.add(v)
				clusters.remove(c1)
				del c1

		del distances
		return clusters

class Point:
	def __init__(self, *vector):
		self._vector = vector

	def __eq__(self, other):
		return self._vector == other._vector

	def __ge__(self, other):
		return self._vector >= other._vector

	def __getitem__(self, i):
		return self._vector[i]

	def __hash__(self):
		return hash(self._vector)

	def __le__(self, other):
		return self._vector <= other._vector

	def __len__(self):
		return len(self._vector)

	def __lt__(self, other):
		return self._vector < other._vector

	def __sub__(self, other):
		assert len(other) == len(self), "points must have equal numbers of dimensions"
		return math.sqrt(sum(((other[i] - self[i]) ** 2 for i in range(len(self)))))
