import vertex as v
from graph import Graph
from enviroment import Limits


class Saboteur:

	def __init__(self, current_vertex: v.Vertex):
		self.current_vertex = current_vertex
		self.amount_of_no_ops = 0
		self.terminate = False
		self.traverse_sequence = []

	def act(self, world: Graph):
		if not self.terminate:
			if len(self.traverse_sequence) == 0:
				if self.amount_of_no_ops < Limits.V:
					self.amount_of_no_ops += 1
				else:
					self.delete_lowest_edge_and_generate_traverse_sequence(world)
					self.amount_of_no_ops = 0
			else:
				self.move()
		else:
			print("TERMINATED")

	def move(self):
		self.current_vertex = self.traverse_sequence[0]
		self.traverse_sequence = self.traverse_sequence[1:]

	def delete_lowest_edge_and_generate_traverse_sequence(self, world):
		closest_neighbor_tup = world.get_closest_neighbor(self.current_vertex)
		if closest_neighbor_tup is None:
			self.terminate = True
		if not self.terminate:
			closest_neighbor = closest_neighbor_tup[0]
			world.delete_edge(self.current_vertex, closest_neighbor)
			closest_neighbor_tup = world.get_closest_neighbor(self.current_vertex)
			if closest_neighbor_tup is None:
				self.terminate = True
			if not self.terminate:
				closest_neighbor = closest_neighbor_tup[0]
				edge_weight = closest_neighbor_tup[1]
				for i in range(edge_weight):
					self.traverse_sequence.append(closest_neighbor)
				self.move()
			else:
				print("TERMINATED")
		else:
			print("TERMINATED")
