# importing shit

from bakery import assert_equal
from drafter import *
from dataclasses import dataclass

# site info

set_site_information(
    author = "sohaf@udel.edu",
    description = """this site is based on my bmeg first lab.
    the user will see the cells too.""",
    sources = """i had no fucking resources because the provided chatgpt is useless as fuck.
    it just yaps for 100 fucking lines, giving useless ass information.
    fuck ai, this shit is not replacing me anytime soon.""",
    planning = ["planning.pdf"],
    links = ["https://github.com/blondecolaqueen/final"]
    )

# ugly bullshit that i apparently have to include

hide_debug_information()
set_website_title("Your Website Title")
set_website_framed(False)

# finally, defining the index

@route
def index (state: State) -> Page:
  return Page (
    state, [
      "Hi"
    ] )

start_server(State(()))

# unit tests

""" assert_equal()
assert_equal()
assert_equal() """
