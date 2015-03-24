# -*- coding: utf-8 -*-
from IPython.display import HTML
from ipythonD3.base import d3_cont, d3_clear

set_chord = """
<style>

.chord path {
  fill-opacity: .67;
  stroke: #000;
  stroke-width: .5px;
}

</style>
<script>
var matrix = {{data}};
var kernel = IPython.notebook.kernel

var chord = d3.layout.chord()
    .padding(.05)
    .sortSubgroups(d3.descending)
    .matrix(matrix);

var width = 960,
    height = 500,
    innerRadius = Math.min(width, height) * .41,
    outerRadius = innerRadius * 1.1;

var fill = d3.scale.ordinal()
    .domain(d3.range({{N}}))
    .range({{c}});

var svg = d3.select("#chart{{id}}").append("svg")
  .attr("width", width)
  .attr("height", height)
  .append("g")
  .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

svg.append("g").selectAll("path")
  .data(chord.groups)
  .enter().append("path")
    .style("fill", function(d) { return fill(d.index); })
    .style("stroke", function(d) { return fill(d.index); })
    .attr("d", d3.svg.arc().innerRadius(innerRadius).outerRadius(outerRadius))
    .on("mouseover", fade(.1))
    .on("mouseout", fade(1))
    .on("click", select());

var ticks = svg.append("g").selectAll("g")
    .data(chord.groups)
  .enter().append("g").selectAll("g")
    .data(groupTicks)
  .enter().append("g")
    .attr("transform", function(d) {
      return "rotate(" + (d.angle * 180 / Math.PI - 90) + ")"
          + "translate(" + outerRadius + ",0)";
    });

ticks.append("line")
    .attr("x1", 1)
    .attr("y1", 0)
    .attr("x2", 5)
    .attr("y2", 0)
    .style("stroke", "#000");

ticks.append("text")
    .attr("x", 8)
    .attr("dy", ".35em")
    .attr("transform", function(d)
        { return d.angle > Math.PI ? "rotate(180)translate(-16)" : null; })
    .style("text-anchor", function(d)
        { return d.angle > Math.PI ? "end" : null; })
    .text(function(d) { return d.label; });

svg.append("g")
    .attr("class", "chord")
  .selectAll("path")
    .data(chord.chords)
  .enter().append("path")
    .attr("d", d3.svg.chord().radius(innerRadius))
    .style("fill", function(d) { return fill(d.target.index); })
    .style("opacity", 1);

// Returns an array of tick angles and labels, given a group.
function groupTicks(d) {
  var k = (d.endAngle - d.startAngle) / d.value;
  return d3.range(0, d.value, 1000).map(function(v, i) {
    return {
      angle: v * k + d.startAngle,
      label: i % 5 ? null : v / 1000 + "k"
    };
  });
}

// Returns an event handler for fading a given chord group.
function fade(opacity) {
  return function(g, i) {
    svg.selectAll(".chord path")
      .filter(function(d)
          { return d.source.index != i && d.target.index != i; })
      .transition()
      .style("opacity", opacity);
  };
}

function select() {
  return function(g, i) {
  kernel.execute('Chord.instances[{{id}}].update('+g.index+')');
  };
}

</script>
"""


def RGBToHTMLColor(rgb_tuple):
    """ convert an (R, G, B) tuple to #RRGGBB """
    hexcolor = '#%02x%02x%02x' % tuple(r*256 for r in rgb_tuple)
    # that's it! '%02x' means zero-padded, 2-digit hex values
    return hexcolor

import seaborn as sns
import random


class Chord(HTML):
    instances = {}

    def __init__(self, mat, c=None):
        self.id = random.randint(0, 100000)
        self.mat = mat
        self.c = c or [RGBToHTMLColor(rgb) for rgb in sns.color_palette()]
        self.shown = False
        self.data = d3_cont.replace("{{id}}", str(self.id))
        self.instances[self.id] = self

    def make_html(self):
        N = len(self.mat)
        data = set_chord.replace("{{data}}", str(self.mat))
        if self.shown:
            data = d3_clear.replace("{{id}}", str(self.id)) + data
        data = data.replace("{{N}}", str(N))
        data = data.replace("{{c}}", str(self.c))
        data = data.replace("{{id}}", str(self.id))
        self.shown = True
        return HTML(data)

    def update(self, x):
        self.value = x
        print(x)
