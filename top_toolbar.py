# -*- coding: utf-8 -*-
"""
Also of interest: http://nbviewer.ipython.org/gist/aflaxman/11156203
"""

class TopToolbar(plugins.PluginBase):
    """Plugin for moving toolbar to top of figure.
    From http://nbviewer.ipython.org/gist/aflaxman/e8000969652f6a967279"""

    JAVASCRIPT = """
    mpld3.register_plugin("toptoolbar", TopToolbar);
    TopToolbar.prototype = Object.create(mpld3.Plugin.prototype);
    TopToolbar.prototype.constructor = TopToolbar;
    function TopToolbar(fig, props){
        mpld3.Plugin.call(this, fig, props);
    };

    TopToolbar.prototype.draw = function(){
      // the toolbar svg doesn't exist
      // yet, so first draw it
      this.fig.toolbar.draw();

      // then change the y position to be
      // at the top of the figure
      this.fig.toolbar.toolbar.attr("y", 2);

      // then remove the draw function,
      // so that it is not called again
      this.fig.toolbar.draw = function() {}
    }
    """
    def __init__(self):
        "Usage: plugins.connect(plt.gcf(), TopToolbar())"
        self.dict_ = {"type": "toptoolbar"}