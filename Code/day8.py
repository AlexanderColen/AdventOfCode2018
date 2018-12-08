import string
import operator


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


def checkNodeChildren(data, number_of_children, count):
    nodes = []
    saved_IDs = []
    # Save the IDs.
    for x in range(number_of_children):
        saved_IDs.append(count)
        count += 1
    # Now recursively loop through.
    for x in range(number_of_children):
        header, data = getHeaderFromData(data=data)
        new_nodes = []
        if header[0] > 0:
            new_nodes, data = checkNodeChildren(data=data, number_of_children=header[0], count=count)
            nodes += new_nodes
        metadata, data = getMetadataFromData(number_of_entries=header[1], data=data)
        nodes.append(Node(ID=saved_IDs[x], header=header, metadata=metadata, data=data.copy(), children=new_nodes))

    return nodes, data


def getAllNodes(data_input, count=0):
    data = list(map(int, data_input.split()))
    nodes = []
    header, data = getHeaderFromData(data=data)
    base_data = data.copy()[:-header[1]]
    saved_ID = count
    count += 1
    new_nodes, data = checkNodeChildren(data=data.copy(), number_of_children=header[0], count=count)
    nodes += new_nodes
    # Create base node and add it to the list.
    metadata, data = getMetadataFromData(number_of_entries=header[1], data=data)
    nodes.append(Node(ID=saved_ID, header=header, metadata=metadata, data=base_data, children=new_nodes))

    return nodes


def calculateNodeValue(node):
    value = 0
    # No children means value of combined metadata.
    if len(node.children) == 0:
        value += sum(node.metadata)
    # Otherwise metadata entries are child node indexes.
    else:
        node.children.sort(key=operator.attrgetter('ID'))
        for i in node.metadata:
            try:
                value += calculateNodeValue(node.children[:node.header[0]][i - 1])
            except IndexError:
                {}
    return value


def puzzle1():
    file_input = open('../Input/input_day8.txt', 'r')
    test_input = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'

    nodes = getAllNodes(test_input)
    # nodes = getAllNodes(file_input.readline())

    metadata_sum = 0
    for node in nodes:
        metadata_sum += sum(node.metadata)

    return metadata_sum


def puzzle2():
    file_input = open('../Input/input_day8.txt', 'r')
    test_input = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'

    # nodes = getAllNodes(test_input)
    nodes = getAllNodes(file_input.readline())

    return calculateNodeValue(nodes[len(nodes) - 1])


class Node:
    def __init__(self, ID, header, metadata, data, children):
        self.ID = ID
        self.header = header
        self.metadata = metadata
        self.data = data
        self.children = children
        self.value = 0

    def __str__(self):
        return f'ID: {self.ID} - Header: {self.header} - Metadata: {self.metadata} - ' \
               f'Children: {len(self.children)} - Data: {self.data}'


print(f'Puzzle 1 outcome: {puzzle1()}')
print(f'Puzzle 2 outcome: {puzzle2()}')
