import datetime

class RateLimter:
    
    """
    This will help rate limit particular indentifier by given configuration
    
    Identifier: IP addresss or any unique id
    Configuration: no of request per second
    """
    
    def __init__(self):
        self.limit = None
        self.seconds = None

    def set_configuration(self, limit: int, seconds: int):
        self.limit = limit
        self.seconds = seconds

    def apply_rate_limit(self, indentifier: str)->bool:
        """ Applies rate limit for the given indentifier
        
        Arguments:
            indentifier {str} -- IP address/uuid/unique id
        
        Returns:
            bool -- true: for rate limit applied
        """
        return False