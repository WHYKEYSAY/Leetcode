class Solution:
    def simplifyPath(self, path: str) -> str:
        # Initialize a stack to keep track of valid directory names
        stack = []
        
        # Split the path by slash '/'
        # This will give us a list of components. 
        # For example, "/home//foo/" -> ["", "home", "", "foo", ""]
        components = path.split("/")
        
        for component in components:
            # If component is empty (due to consecutive slashes) or is just '.', ignore it
            if component == "" or component == ".":
                continue
            
            # If component is '..', we need to go up one level
            if component == "..":
                # Pop from stack if it's not empty
                if stack:
                    stack.pop()
            else:
                # Otherwise, it's a valid directory name, push to stack
                stack.append(component)
        
        # Join the valid directory names with '/' and prepend a '/' for the root
        return "/" + "/".join(stack)
