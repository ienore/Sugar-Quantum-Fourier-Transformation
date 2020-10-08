
import pyqpanda.pyQPanda as pq
import numpy as np

###################################################################

from pyqpanda import *

if __name__ == "__main__":

    init(QMachineType.CPU)
    qubits = qAlloc_many(3)
    cbits = cAlloc_many(3)

    # 构建量子程序
    prog = QProg()
    circuit = create_empty_circuit()
    #circuit.insert(H(qubits[0]))
    
    circuit.insert(H(qubits[0]))\
        .insert(CR(qubits[1],qubits[0],2*np.pi/2**2)) \
        .insert(CR(qubits[2],qubits[0],2*np.pi/2**3))\
        .insert(H(qubits[1]))\
        .insert(CR(qubits[2],qubits[1],2*np.pi/2**2))\
        .insert(H(qubits[2]))\
        .insert(SWAP(qubits[0],qubits[2]))
        
    prog.insert(circuit)
    result_prob = prob_run_dict(prog,qubits,-1)


    # 打印量子态在量子程序多次运行结果中出现的次数

    print("Probability Result:\n")
    print(result_prob)
    
    finalize()
####################################################  
pq.draw_qprog(prog)

    