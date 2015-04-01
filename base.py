# -*- coding: utf-8 -*-
"""
D3-based visualisations for the IPython dashboard
"""
from IPython.display import HTML, display


hide = """
<style>
.hidden {display: none;}
.input_prompt {display: none;}
.input_area {display: none;}
.prompt {display: none;}
.output_stderr {display: none;}
.dashpanel (position: fixed;}
</style>
<script>
$("#header").css('display', 'none');
var psize = $("#notebook-continer").width()
$("#notebook-container").css('width', '100%');
</script>
"""
# and .container {width: page-width;} by script

show = """
<style>
.input_prompt {display: inline;}
.input_area {display: inline;}
.prompt {display: inline;}
.output_stderr {display: inline;}
.dashpanel (position: static;}
</style>
<script>
$("#header").css('display', 'block');
$("#notebook-container").width(psize);
</script>
"""


def dashboard(on=True):
    """Turn your notebook into a dashboard by hiding input prompts and output
prompt zones. Execute with:

from IPython.html.widgets import interact
f = interact(dashboard, on=False)

to leave a button with which you can retrieve the original layout."""
    display(HTML([hide, show][on]))

d3_cont = """
<script src="http://d3js.org/d3.v3.min.js"></script>
<div id="chart{{id}}" class="dashpanel"></div>
"""

d3_clear = """
<script>
d3.select("#chart{{id}}").selectAll("*").remove()
</script>
"""
