import re

from package.ENV import ENV


class RegexWrapper:
    """A wrapper for common Regex queries"""
    @staticmethod
    def is_key(s: str) -> bool:
        """Determine if s is a game activation key or redemption URL"""
        return bool(re.match(ENV.steam_key_regex, s) or
                    re.match(ENV.gog_key_regex, s) or
                    re.match(ENV.hb_gift_regex, s) or
                    re.match(ENV.itch_key_regex, s) or
                    re.match(ENV.origin_key_regex, s) or
                    re.match(ENV.uplay_key_regex, s))
