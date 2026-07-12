class Solution(object):
    def isNumber(self, s):
        digit_seen = False
        dot_seen = False
        e_seen = False

        for i, ch in enumerate(s):

            if ch.isdigit():
                digit_seen = True

            elif ch in ['+', '-']:
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False

            elif ch == '.':
                if dot_seen or e_seen:
                    return False
                dot_seen = True

            elif ch in ['e', 'E']:
                if e_seen or not digit_seen:
                    return False
                e_seen = True
                digit_seen = False

            else:
                return False

        return digit_seen