
from . import standard_params as prm

def add_params(tr):
    
    tr.f_add_parameter('prm.an_mu', prm.an_mu)
    tr.f_add_parameter('prm.an_sig', prm.an_sig)
    tr.f_add_parameter('prm.bn_mu', prm.bn_mu)
    tr.f_add_parameter('prm.bn_sig', prm.bn_sig)

    tr.f_add_parameter('prm.X_0', prm.X_0)
    tr.f_add_parameter('prm.Nprocess', prm.Nprocess)
    tr.f_add_parameter('prm.Nsteps', prm.Nsteps)

    tr.f_add_parameter('prm.p_prune', prm.p_prune)
    tr.f_add_parameter('prm.c', prm.c)
    tr.f_add_parameter('prm.up_cap', prm.up_cap)    

    tr.f_add_parameter('prm.nrecord', prm.nrecord)
    tr.f_add_parameter('prm.var', prm.var)

