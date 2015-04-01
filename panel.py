# -*- coding: utf-8 -*-
from mpld3 import plugins

js = """
<script>
var obj = d3.select("#chart{{id}}")
.on("mousemove", function(d, i){
                    obj
                      .style("top", d3.event.pageY + 10 + "px")
                      .style("left",d3.event.pageX + 10 + "px");
}.bind(this));
</script>
"""

    def __init__(self,  css=None):
        self.dict_ = {"type": "htmltooltip",
                      "id": get_id(points, suffix),
                      "labels": labels,
                      "hoffset": hoffset,
                      "voffset": voffset}
