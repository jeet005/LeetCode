class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_string = ""
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push the current number and string onto the stack
                stack.append((current_string, current_num))
                # Reset current string and number
                current_string = ""
                current_num = 0
            elif char == ']':
                # Pop the last string and number from the stack
                last_string, num = stack.pop()
                # Update current string by repeating it `num` times and appending to the last string
                current_string = last_string + current_string * num
            else:
                # Append current character to the current string
                current_string += char
        
        return current_string

        








        