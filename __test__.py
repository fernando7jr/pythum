from pythum import QuantumEngine, Qubit, Qublock, Qubyte

engine = QuantumEngine()

qbyte = Qubyte.from_notation("|0>|0>|01>|0>|1>|1>|1>|01>")

result = engine.measure_byte(qbyte)

print(result)
