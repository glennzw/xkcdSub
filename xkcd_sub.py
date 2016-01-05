#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# glenn@sensepost.com // @glennzw
# 
# This mitmproxy script will substitute text in web page responses
# as per XKCD comics 1288 and 1625.
# Usage:
#  mitmdump -s xkcd_sub.py -p 8080
#
#  How you redirect traffc to 8080 is up to you. Arpspoof, DHCP
#   leases, wpad, etc.

from libmproxy.models import decoded

# https://xkcd.com/1288/
# https://xkcd.com/1625/
replacezor = {
        "witnesses" : "these dudes i know",
        "allegedly" : "kinda probably",
        "new study" : "tumblr post",
        "rebuild" : "avenge",
        "space" : "spaaace",
        "google glass" : "virtual boy",
        "smartphone" : "pokedex",
        "electric" : "atomic",
        "senator" : "elf-lord",
        "car" : "cat",
        "election" : "eating contest",
        "congressional leaders" : "river spirits",
        "homeland security" : "homestar runner",
        "could not be reached for comment" : "is guilty and everyone knows it",
        "debate" : "dance-off",
        "self driving" : "uncontrollably swerving",
        "poll" : "psychic reading",
        "candidate" : "airbender",
        "drone" : "dog",
        "vows to" : "probably won't",
        "at large" : "very large",
        "successfully" : "suddenly",
        "expands" : "physically expands",
        "first/second/third-degree" : "friggin' awful",
        "an unknown number" : "like hundreds",
        "front runner" : "blade runner",
        "global" : "spherical",
        "years" : "minutes",
        "minutes" : "years",
        "no indication" : "lots of signs",
        "urged restraint by" : "drunkenly egged on",
        "horsepower" : "tons of horsemeat"
    }


def response(context, flow):
    with decoded(flow.response):
        for k, v in replacezor.iteritems():
            flow.response.content = flow.response.content.replace(k, v)
            flow.response.content = flow.response.content.replace(k.title(), v)
