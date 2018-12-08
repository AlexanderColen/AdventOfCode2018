def getHeaderFromData(data):
    header = [data[0], data[1]]
    data.remove(data[0])
    data.remove(data[0])

    return header, data


def getMetadataFromData(number_of_entries, data):
    metadata = []
    for x in range(number_of_entries):
        datapoint = data[0]
        metadata.append(datapoint)
        del data[0]

    return metadata, data


def checkNodeChildren(data, number_of_children):
    nodes = []
    for x in range(number_of_children):
        header, data = getHeaderFromData(data=data)
        new_nodes = []
        if header[0] > 0:
            new_nodes, data = checkNodeChildren(data=data, number_of_children=header[0])
            nodes += new_nodes
        metadata, data = getMetadataFromData(number_of_entries=header[1], data=data)
        nodes.append(Node(header=header, metadata=metadata, data=data, children=new_nodes))

    return nodes, data


def getAllNodes(data_input):
    data = list(map(int, data_input.split()))
    nodes = []
    header, data = getHeaderFromData(data=data)
    new_nodes, data = checkNodeChildren(data=data, number_of_children=header[0])
    nodes += new_nodes
    # Create base node and add it to the list.
    metadata, data = getMetadataFromData(number_of_entries=header[1], data=data)
    nodes.append(Node(header=header, metadata=metadata, data=data, children=new_nodes))

    return nodes


def puzzle1():
    file_input = open('../Input/input_day8.txt', 'r')
    test_input = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'

    # nodes = getAllNodes(test_input)
    nodes = getAllNodes(file_input.readline())

    metadata_sum = 0
    for node in nodes:
        metadata_sum += sum(node.metadata)

    return metadata_sum


def puzzle2():
    file_input = open('../Input/input_day8.txt', 'r')
    test_input = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'

    nodes = getAllNodes(test_input)
    # nodes = getAllNodes(file_input.readline())

    value = 0
    for node in nodes:
        print(node)
        # No children means value of combined metadata.
        if len(node.children) == 0:
            value += sum(node.metadata)
        # Otherwise metadata entries are child node indexes.
        else:
            value += 0

    return value


class Node:
    def __init__(self, header, metadata, data, children):
        self.header = header
        self.metadata = metadata
        self.data = data
        self.children = children

    def __str__(self):
        return f'Header: {self.header} - Metadata: {self.metadata} - Children: {len(self.children)}'


print(f'Puzzle 1 outcome: {puzzle1()}')
print(f'Puzzle 2 outcome: {puzzle2()}')
