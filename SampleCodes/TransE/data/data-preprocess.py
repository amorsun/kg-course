train = './train.txt'
entity2id = './entity2id.txt'
relation2id = './relation2id.txt'

entity = set()
relation = set()
with open(train, 'r', encoding='utf-8') as f:
	for line in f.readlines():
		line_list = line.strip().split('\t')
		assert len(line_list) == 3
		entity.add(line_list[0])
		entity.add(line_list[2])
		relation.add(line_list[1])


def write2id(item, item_file):
	num_item = 0
	with open(item_file, 'w', encoding='utf-8') as f:
		for i in item:
			f.write(i)
			f.write('\t')
			f.write(str(num_item))
			f.write('\n')
			num_item += 1

write2id(entity, entity2id)
write2id(relation, relation2id)




