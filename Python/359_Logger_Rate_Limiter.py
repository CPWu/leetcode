class Logger:
    # Time: O(1), Space: O(M) all incoming messages 
    def __init__(self):
        # Initialize a data structure to store messages
        self.messages = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # If the message streaming in does not exist add to dictionary
        if message not in self.messages:
            self.messages[message] = timestamp
            return True
        # Message exists in dictionary but has the time passed? prev_timestamp + 10 seconds if yes, print
        elif timestamp >= self.messages[message] + 10:
            self.messages[message] = timestamp
            return True
        # messages has been seen before and time has not passed enough yet.
        else:
            return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message

