from slist.slist import SList, SLNode

new_list = SList()

new_list.add_to_front(1)
new_list.add_to_front(2)
new_list.add_to_front(3)
new_list.add_to_front(4)
new_list.add_to_front(5)
new_list.add_to_front(6)

new_list.remove_from_front()
new_list.remove_from_back()

new_list.print_values()