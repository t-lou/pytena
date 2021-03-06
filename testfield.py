from __future__ import print_function

import os
import tempfile
import datetime

import FigureManager
import canvas
import testfield_source

# Some abbreviations.
add_all_figures = FigureManager.g_figure_manager.add_all_figures
add_figure = FigureManager.g_figure_manager.add_figure
save_all_figures = FigureManager.FigureManager.save_all_figures
remove_figure = FigureManager.g_figure_manager.remove_figure
remove_all_figures = FigureManager.g_figure_manager.remove_all_figures
get_figure = FigureManager.g_figure_manager.get_figure
get_all_figures = FigureManager.g_figure_manager.get_all_figures
reset_figure = FigureManager.g_figure_manager.reset_figure
add_pmg = FigureManager.g_figure_manager.add_pmg


def update_figures():
    """Show all figures added to default FileManager.
    
    The default manager is FigureManager.g_figure_manager
    """
    canvas.show_figure_from_manager(FigureManager.g_figure_manager)


# Execute the string (from script or command line).
if testfield_source.content is not None:
    with open(os.path.join(tempfile.gettempdir(), 'pytena_history'),
              'a') as log:
        separator = '#' * 26 + ' ' + str(
            datetime.datetime.now()) + ' ' + '#' * 26
        log.writelines('\n'.join([separator, testfield_source.content, '\n']))

    exec(testfield_source.content)
