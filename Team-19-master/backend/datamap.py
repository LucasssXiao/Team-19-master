# import
# -*- coding: utf-8 -*-
from jaal import Jaal
from jaal.datasets import load_got
import os
import pandas as pd
# load the data
# edge_df, node_df = load_got()
# # init Jaal and run server
# Jaal(edge_df, node_df).plot()



# data load and return function
def load_get(filter_conections_threshold=10):
    """Load the first book of the Got Dataset
    Parameters
    -----------
    filter_conections_threshold: int
        keep the connections in GoT dataset with weights greater than this threshold 
    """
    # resolve path
    this_dir, _ = os.path.split(__file__)
    # load the edge and node data
    edge_df = pd.read_csv(os.path.join(this_dir, "edge.csv"))
    node_df = pd.read_csv(os.path.join(this_dir, "node.csv"))
    # node_df = pd.read_csv(os.path.join(this_dir, "got", "got_node_df.csv"))
    # return 
    return edge_df, node_df





if __name__ == "__main__":
    # edge_df, node_df = load_got()
    edgedd, nodedd= load_get()
    # init Jaal and run server
    # edge_df.loc[:, 'label'] = edge_df.loc[:, 'weight'].astype(str)
    # Jaal(edge_df, node_df).plot(directed=True, vis_opts={'height': '400px', # change height
    #                                   'interaction':{'hover': True,
    #                                   'tooltipDelay': 300}, # turn on-off the hover 
    #                                   'physics':{'stabilization':{'iterations': 100}},
    #                                     # 'clickToUse': True,
    #                                     'nodes': {'chosen': True,
    #                                     'label': 'tttt',
    #                                     'color': '#ff0000',
    #                                     'title': "dddd",}}) # define the convergence iteration of network
    # Jaal(edgedd).plot()
    # edgedd.loc[:, 'label'] = edgedd.loc[:, 'weight'].astype(str)
    Jaal(edgedd, nodedd).plot(directed=True, vis_opts={'height': '400px', # change height
                                      'interaction':{'hover': True,
                                      'tooltipDelay': 300}, # turn on-off the hover 
                                      'physics':{'stabilization':{'iterations': 100}},
                                        # 'clickToUse': True,
                                        'nodes': {'chosen': True,
                                        'label': 'tttt',
                                        
                                        'title': "dddd",}})
