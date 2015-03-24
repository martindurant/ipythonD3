# -*- coding: utf-8 -*-
"""
D3-based visualisations for the IPython dashboard
"""
from IPython.display import HTML, display
from show_chord import Chord


hide = """
<style>

.input_prompt {
    display: none;
}

.input_area {
    display: none;
}

.prompt {
    display: none;
}

.output_stderr {
    display: none;
}

</style>

<script>
$('#header-container').toggle();
$('.header-bar').toggle();
$('div#maintoolbar').toggle();
</script>
"""
show = hide.replace('none', 'inline')


def dashboard(on=True):
    """Turn your notebook into a dashboard by hiding input prompts and output
prompt zones. Execute with:

f = interact(dashboard, on=False)

to leave a button with which you can retrieve the original layout."""
    display(HTML([hide, show][on]))

d3_cont = """
<script src="http://d3js.org/d3.v3.min.js"></script>
<div id="chart{{id}}"></div>
"""

d3_clear = """
<script>
d3.select("#chart{{id}}").selectAll("*").remove()
</script>
"""
