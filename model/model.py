
import os, pickle

import numpy as np
import scipy.stats as scts

    
class Kesten_process(object):

    def __init__(self, N, X_0, a, b):
        self.N = N
        self.a = a
        self.b = b
        self.X = np.ones(N) * X_0

    def step(self):

        asv = self.a.rvs(size=self.N)
        while len(asv[asv<=0])>0:
            asv[asv<=0] = self.a.rvs(size=len(asv[asv<=0]))
        
        self.X = asv*self.X+self.b.rvs(size=self.N)
        self.X[self.X<0]=0



        
def run_model(tr):

    np.random.seed(int(tr.v_idx))

    print("Started process with id ", str(tr.v_idx))

    namespace = tr.prm.f_to_dict(short_names=True, fast_access=True)
    namespace['idx'] = tr.v_idx

    a_n = scts.norm(loc=tr.an_mu, scale=tr.an_sig)
    b_n = scts.norm(loc=tr.bn_mu, scale=tr.bn_sig)

    kx = []
    lts = []
    record = []

    K = Kesten_process(tr.Nprocess, tr.X_0, a_n, b_n)

    counter,ts = np.zeros(tr.Nprocess), np.zeros(tr.Nprocess)

    for i in range(1):
        
        for j in range(1,tr.Nsteps+1):

            if tr.nrecord > 0:
                record.append(K.X[:tr.nrecord])

            K.step()

            ids = np.logical_and(K.X==0,
                                 np.random.uniform(size=tr.Nprocess)<tr.p_prune)

            for c,t in zip(counter[ids],ts[ids]):
                lts.append([i, c, j, t, 1,-10])

            counter[ids] += 1
            K.X[ids] =tr.X_0
            ts[ids] = j

        # -1 for end of simulation "synapse didn't die"
        for c,t,kx_v in zip(counter, ts, K.X):
            lts.append([i,c,j,t,-1,kx_v])
            kx.append([kx_v,tr.Nsteps-t])

        
    raw_dir = '../data/%.4d/'%(tr.v_idx)
    
    if not os.path.exists(raw_dir):
        os.makedirs(raw_dir)

    with open(raw_dir+'namespace.p','wb') as pfile:
        pickle.dump(namespace,pfile)   

    with open(raw_dir+'kx.p','wb') as pfile:
        pickle.dump(kx,pfile)   
    with open(raw_dir+'lts.p','wb') as pfile:
        pickle.dump(lts,pfile)
    with open(raw_dir+'record.p','wb') as pfile:
        pickle.dump(np.array(record),pfile)   

    
