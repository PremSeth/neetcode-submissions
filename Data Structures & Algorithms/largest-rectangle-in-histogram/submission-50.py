class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        m_area = 0
        old_idx = 0
        for idx, h in enumerate(heights): 
            rollback = idx
            while stack and h < stack[-1][1]:
                old_idx, old_h = stack.pop()
                m_area = max(m_area, (idx-old_idx)*old_h)
                rollback = old_idx
            stack.append( (rollback, h) )
        while stack: 
            old_idx, old_h = stack.pop()
            print(len(heights)-old_idx)
            m_area = max(m_area, (len(heights)-old_idx)*old_h)
        return m_area
