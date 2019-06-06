import re

# File to hold basic model

class BaseModel:
    def __init__(self):
        self.keywords = ["1750", "1,750"]
    
    # Returns true if detected
    def run(self, tex):
        for k in self.keywords:
            r = re.findall(k, tex)
            if len(r) != 0:
                return True
        return False