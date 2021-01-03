from vertex import Vertex


class Edge(object):
	def __init__(self, name, weight: int, v1: Vertex, v2: Vertex, blocked_in_prob=0):
		self.name = name
		self.blocked_in_prob = blocked_in_prob
		self.weight = weight
		self.v1 = v1
		self.v2 = v2

	def __str__(self):
		s = "(EDGE " + self.name + ", blocked with probability: " + str(self.blocked_in_prob)
		s += ", weight " + str(self.weight) + ", "+ str(self.v1) + " " + str(self.v2) + ")"
		return s


def get_edge_list_as_string(edge_list):
	s = "[ "
	for edge in edge_list:
		s += str(edge) + ", "
	last_index_of_comma = s.rfind(",")
	if last_index_of_comma != -1:
		s = s[:last_index_of_comma] + s[last_index_of_comma + 1:]
	return s + "]"