
import os, git

from pypet import Environment, Trajectory

from .explored_params import explore_dict, name
from .add_parameters import add_params
from .model import run_model

# control the number of cores to be used for computation
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--ncores", "-c", help="No. cores", nargs=1)
parser.add_argument("--testrun", "-t", action='store_true')
args = parser.parse_args()
ncores = int(args.ncores[0])
print("Using {:d} cores".format(ncores))

# check the state of the git repository
repo = git.Repo('./code/')

if not args.testrun:
    # check for changes, while ignoring submodules
    if repo.git.status('-s', '--ignore-submodules'):
        raise pex.GitDiffError('Found not committed changes!')

    commit = repo.commit(None)

filename = os.path.join(os.getcwd(), 'data/', name+'.hdf5')

    
# if not the first run, tr2 will be merged later
label = 'tr1'
first_run = True
if os.path.exists(filename):
    first_run = False
    label = 'tr2'
    
env = Environment(trajectory=label,
                  add_time=False,
                  filename=filename,
                  continuable=False, # ??
                  lazy_debug=False,  # ??
                  multiproc=True,     
                  ncores=ncores,
                  use_pool=False, # likely not working w/ brian2
                  wrap_mode='QUEUE', # ??
                  overwrite_file=False)


tr = env.trajectory

add_params(tr)

if not args.testrun:
    tr.f_add_parameter('mconfig.git.sha1', str(commit))
    tr.f_add_parameter('mconfig.git.message', commit.message)

tr.f_explore(explore_dict)

env.run(run_model)

