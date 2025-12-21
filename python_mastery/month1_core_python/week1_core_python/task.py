class Repository:
  def __init__ (self, name, language, stars):
    print(f"Creating a new object repository for '{name}'...")
    self.name = name
    self.language = language
    self.stars = stars
  def __str__(self):
    return f"{self.name} is a {self.language} repository with {self.stars}"
  def __repr__(self):
    return f"Repository({name} is '{self.name}', {language} is '{self.language} and {stars} is {self.stars})"
