from linked__list import LinkedList

linked_list1 = LinkedList()
linked_list1.insert_last(10)
linked_list1.insert_last(20)
linked_list1.insert_last(30)
linked_list1.insert_last(2)

linked_list1.view_list()

print("The length of the linked list is " + str(linked_list1.length_ll()))

try:

    print(linked_list1.get_at_index(2))

except SyntaxError:

    print("Syntax error! Give the valid index")


########################################################

print("insertion test: ")

linked_list1.insert_at_index(1, 5)
linked_list1.view_list()

###############################################################

print("deletion test: ")

try:

    linked_list1.delete_node(2)

except SyntaxError:

    print("Syntax error! Give the valid index")

except:

    print("something else went wrong")

linked_list1.view_list()

print("reverse list")

linked_list1.reverse_ll()

# print("Again reversing the linked list")
# linked_list1.reverse_ll()

print("sorting the linked list")
linked_list1.sorting_ll()
