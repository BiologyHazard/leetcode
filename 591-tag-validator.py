class Solution:
    def isValid(self, code: str) -> bool:
        i = 0
        stack = []

        while i < len(code):
            char = code[i]
            if char == '<':
                if i == len(code) - 1:
                    return False

                char1 = code[i+1]

                if char1 == '/':
                    if not stack:
                        return False
                    end_tag_idx = code.find('>', i+1)
                    if end_tag_idx == -1:
                        return False
                    tag_name = code[i+2: end_tag_idx]
                    if tag_name != stack[-1]:
                        return False
                    stack.pop()
                    i = end_tag_idx + 1

                elif char1 == '!':
                    if not stack:
                        return False
                    if code[i+2: i+9] != '[CDATA[':
                        return False
                    end_tag_idx = code.find(']]>', i+9)
                    if end_tag_idx == -1:
                        return False
                    i = end_tag_idx + 3

                else:
                    if not stack and i > 0:
                        return False
                    end_tag_idx = code.find('>', i+1)
                    if end_tag_idx == -1:
                        return False
                    tag_name = code[i+1: end_tag_idx]
                    if (not 1 <= len(tag_name) <= 9 or
                            not all(map(lambda x: 'A' <= x <= 'Z', tag_name))):
                        return False
                    stack.append(tag_name)
                    i = end_tag_idx + 1

            else:
                if not stack:
                    return False
                i += 1

        if stack:
            return False

        return True
