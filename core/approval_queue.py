"""
VERIDEX X
APPROVAL QUEUE
"""

class ApprovalQueue:

    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.append(item)

    def pending(self):
        return self.queue

    def approve(self, index):

        if index < 0 or index >= len(self.queue):
            return None

        return self.queue.pop(index)
