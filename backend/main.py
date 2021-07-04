from multiprocessing import Pool
import os

# Main
if __name__ == '__main__':

  # Run `predict.py` and `capture.py` simultaneously
  processes = ('Package/predict.py', 'Package/capture.py')

  def run_process(process):                                                             
      os.system('python {}'.format(process))  

  pool = Pool(processes=None)                                                       
  pool.map(run_process, processes)

  # run_process('Package/predict.py')
  # run_process('Package/capture.py')