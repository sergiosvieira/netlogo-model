import random

change_count = 0
inertia_count = 0
all_red_count = 0
all_gray_count = 0
gray_counter = 0
minor = 0
dist = 0

class Player:
	def __init__(self, id, color):
		self.id = id
		self.color = color
		self.left_neigh = None
		self.right_neigh = None
		self.links = []
		self.score = 0
		self.free_slots = 0
		self.uffa = 0
		self.uffa_grigia = 0
		self.red_nearby_count = 0
		self.gray_nearby_count = 0
		self.future_breed = 0
		self.next_breed = 0
		self.list_future_breed = 0
		self.my_breed = 0
		self.my_future_breed = 0
		self.equal = 0
		self.base = 0
	def __str__(self):
		left = self.left_neigh.id if self.left_neigh != None else ""
		right = self.right_neigh.id if self.right_neigh != None else ""
		return '({}, {}, l:{}, r:{})'.format(self.id, self.color, left, right)

def create_network(players_p, players_r):
	network_array = []
	total_payers = players_r + players_p
	counter_p = players_p
	counter_r = players_r
	for p in range(0, total_payers):
		id = p + 1
		if counter_p > 0:
			network_array.append(Player(id, "red"))
			counter_p = counter_p - 1
		elif counter_r > 0:
			network_array.append(Player(id, "gray"))
			counter_r = counter_r - 1
	random.shuffle(network_array)
	# make left and right neighborhoods
	for index in range(1, total_payers):
		left_index = index - 1;
		right_index = (index + 1) % total_payers
		network_array[index].left_neigh = network_array[left_index];
		network_array[index].right_neigh = network_array[right_index];
	index = 0
	left_index = (index + 1) % total_payers
	right_index = index + 1
	network_array[index].left_neigh = network_array[left_index];
	network_array[index].right_neigh = network_array[right_index];		
	return network_array

def create_links(player, k_potential_interactions, network):
	index = network.index(player)
	total_left = random.randrange(0, k_potential_interactions)
	total_right = random.randrange(0, k_potential_interactions)
	left_neigh = network[k_potential_interactions:index]
	right_neigh = network[index:k_potential_interactions]

def make_regular_network(target_degree, k_potential_interactions, network):
	for p in network:
		link_neighs(p, k_potential_interactions)


# create_network(1, 1)
for p in create_network(5, 5):
	print(p)






