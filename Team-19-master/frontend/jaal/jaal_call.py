# import
from jaal import Jaal
from jaal.datasets import load_got
import os
import pandas as pd

# load the data
# edge_df, node_df = load_got()
# # dd = node_df['gender'][0]
# title = [None]*1618;
# for index, i in enumerate(title):
#   title[index] = 'type:' + node_df['type_desc'][index] + '<br>create date: ' + str(node_df['create_date'][index]) + '<br>modify date: ' + str(node_df['modify_date'][index])
# node_df['title'] = title


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
    title = [None]*1618;
    for index, i in enumerate(title):
      title[index] = 'type:' + node_df['type_desc'][index] + '<br>create date: ' + str(node_df['create_date'][index]) + '<br>modify date: ' + str(node_df['modify_date'][index])
    node_df['title'] = title
    # node_df = pd.read_csv(os.path.join(this_dir, "got", "got_node_df.csv"))
    # return 
    return edge_df, node_df
edge_df, node_df = load_get()

# title = [None]*1618;
# for index, i in enumerate(title):
#   title[index] = 'type:' + node_df['type_desc'][index] + '<br>create date: ' + str(node_df['create_date'][index]) + '<br>modify date: ' + str(node_df['modify_date'][index])
# node_df['title'] = title

# init Jaal and run server (with opts)
Jaal(edge_df, node_df).plot(vis_opts={'height': '400px', # change height
                                      'interaction':{'hover': True}, # turn on-off the hover 
                                      'manipulation': {
                                        'enabled': True
                                        },
                                      'physics': False,
                                      'hierarchical':{'nodeSpacing': 10000}
                                        # 'clickToUse': True,
                                        # 'nodes': {'chosen': True,
                                        # 'label': 'tttt',
                                        # 'title':'fdfdf',
                                        # }
                                        })
# if __name__ == "__main__":
#   print(node_df)
  # print(node_df.shape[1])
  # print(dd)
  
# init Jaal and run server (with gunicorn)
# app = Jaal(edge_df, node_df).create()
# server = app.server