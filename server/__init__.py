from flask import Flask

from .bypassers.adfly import adfly_bypass
from .bypassers.droplink import droplink_bypass
from .bypassers.gplinks import gplinks_bypass
from .bypassers.linkvertise import linkvertise_bypass
from .bypassers.ouo import ouo_bypass
from .bypassers.rocklinks import rocklinks_bypass
from .bypassers.shorte_st import sh_st_bypass

BYPASSERS = {
    "adfly": adfly_bypass,
    "droplink": droplink_bypass,
    "gplinks": gplinks_bypass,
    "linkvertise": linkvertise_bypass,
    "ouo": ouo_bypass,
    "rocklinks": rocklinks_bypass,
    "shorte": sh_st_bypass,
}

app = Flask(
            __name__,
            static_url_path="/static", static_folder="assets",
            template_folder="templates",
        )
