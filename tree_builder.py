class EmployeeNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

class TeamTree:
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node = None):
        if self.root is None:
            print("Tree is empty. Cannot insert without root.")
            return False

        if current_node is None:
            current_node = self.root

        if current_node.name == manager_name:
            if side == "left" and current_node.left is None:
                current_node.left = EmployeeNode(employee_name)
                print(f"{employee_name} added under {manager_name} on the left.")
                return True
            
            elif side == "right"and current_node.right is None:
                current_node.right = EmployeeNode(employee_name)
                print(f"{employee_name} added under {manager_name} on the right.")
                return True
            
            else:
                print(f"Cannot add {employee_name}: {manager_name} already has a {side} subordinate.")
                return False

        found_left = False
        found_right = False

        if current_node.left:
            found_left = self.insert(manager_name, employee_name, side, current_node.left)

        if current_node.right and not found_left:
            found_right  = self.insert(manager_name, employee_name, side, current_node.right)

        if not(found_left or found_right):
            if current_node == self.root:
                print(f"Manager {manager_name} not found in the tree.")
            return False

        return True
    
    def print_tree(self, node=None, level = 0):
        if node is None:
            if level == 0:
                node = self.root
            if node is None:
                print("The tree is empty.")
                return
            
        indent = "  " * level
        print(f"-{indent}{node.name}")

        #Printing the recursive calls for left and right children
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''




# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")

#Design Memo
#1 - Recursive Insertion works by traversing the entire tree to find the manager node.
#Once the manager node is found, it checks if the specified side is left or right and if that position is available.
#Then the new employee node is created and linked to the manager node. Because employees are under a manager, the tree structure is maintained.
#If the manager is not found, it will print a message indicating that there is no manager with that name in the tree.
#The user will recieve a true or false response based on whether the insertion was effective or not.
#If the manager is found but the specified side is already occupied, then it will state that there already is a subordinate in that position.

#2) Some challenges I faced when finding the right spot for a new employee are:
# - Ensuring that the manager exists in the tree before attempting to add a new employeee.
# - Handling whether or not the left or right side is already occupied by another employee.
# - Making sure that the recursive function works properly and gives the correct outputs.

#3) Trees might be preferable to other data structures when you need to represent hierachical relationships.
#For example, this could be represented on a company catelog website, where a company is selling different products and each product is under a different category.
#The product could also have subcategories, and those subcategories can have their own products. This would be a good case to use the tree structure to represent the relationship between categories and their products.