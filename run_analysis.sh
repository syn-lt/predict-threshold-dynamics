#!/bin/sh

rm -rf code/analysis
cp -r ~/lab/stoch_mods/thrs_dyn/analysis-dev/ code/analysis/

python -m code.analysis.master_1x

#cp ../../analysis/fb/lifetimes_x_T.py analysis/
#srun -p sleuths --mem 16GB python analysis/lifetimes_x_T.py
#python analysis/lifetimes_x_T.py

#cp ../../analysis/master_1x.py analysis/
#srun -p sleuths --mem 16GB python analysis/lifetimes_x_T.py
#python analysis/master_1x.py


#cp ../../analysis/traces.py analysis/
#srun -p sleuths --mem 16GB python analysis/lifetimes_x_T.py
#python analysis/traces.py


#cp ../../analysis/prb_srv_x_T.py analysis/
#srun -p sleuths --mem 16GB python analysis/lifetimes_x_T.py
#python analysis/prb_srv_x_T.py

# cp ../../analysis/kx_trace.py analysis/
# #srun -p sleuths --mem 16GB python analysis/lifetimes_x_T.py
# python analysis/kx_trace.py

#cp ../../analysis/pdf_estimate_linear.py analysis/
#python analysis/pdf_estimate_linear.py

#cp ../../analysis/pdf_estimate_log.py analysis/
#python analysis/pdf_estimate_log.py

# cp ../../analysis/prb_srv_x_scf_full.py analysis/
# python analysis/prb_srv_x_scf_full.py

#cp ../../analysis/pdf_linear_x_T.py analysis/
#srun -p sleuths --mem 16GB python analysis/lifetimes_x_T.py
#python analysis/pdf_linear_x_T.py

#cp ../../analysis/pdf_log_x_T.py analysis/
#srun -p sleuths --mem 16GB python analysis/lifetimes_x_T.py
#python analysis/pdf_log_x_T.py
