from random import choice
import html
import requests
import re


class NamedJokes:
    def __init__(self, name="Thor"):
        self.name = name
        names = self._spaces.split(self.name.strip())
        self.first_name = names[0]
        self.last_name = names[-1]

    def __call__(self, search_term=None, all_jokes=False):
        """returns a joke string from api.chucknorris.io, replacing with given name"""
        jokes_api = (
            f"https://api.chucknorris.io/jokes/search?query={search_term}"
            if search_term
            else "https://api.chucknorris.io/jokes/random"
        )
        joke_json = self._get_json(jokes_api)

        if joke_json:
            jokes = self._get_jokes_from_json(joke_json)
            if len(jokes) > 0:
                if not all_jokes:
                    return self._repl_name(choice(jokes))
                else:
                    return list(map(self._repl_name, jokes))
            else:
                return None

    def _repl_name(self, txt):
        txt = self._chuck_norris.sub(self.name, txt)
        txt = self._chuck.sub(self.first_name, txt)
        txt = self._norris.sub(self.last_name, txt)
        return txt

    def _get_json(self, api_url):
        """calls the api and returns the response json if the status is 200, otherwise returns False"""
        r = requests.get(api_url)
        if r.status_code != 200:
            return False
        else:
            return r.json()

    def _get_jokes_from_json(self, joke_json):
        if joke_json:
            if "value" in joke_json:
                return [self._repl_name(joke_json["value"])]
            else:
                if joke_json["total"] > 0:
                    return [x["value"] for x in joke_json["result"]]
                else:
                    return []

    _spaces = re.compile(r"\s+")
    _chuck_norris = re.compile("Chuck Norris", re.IGNORECASE)
    _chuck = re.compile("Chuck", re.IGNORECASE)
    _norris = re.compile("Norris", re.IGNORECASE)


print(NamedJokes()())
