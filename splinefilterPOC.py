import numpy as np
import wave
import pyaudio
from scipy.io import wavfile
from scipy import interpolate
import math
import matplotlib.pyplot as plt

#MaxVal = 2147483647
MaxVal = 19
#found relavant blog post:
#http://yehar.com/blog/?p=197

def clippingFunction(inSample):
	threshold = MaxVal #maximum 24 bit output

	outSample = threshold - threshold/(abs(inSample) + math.sqrt(threshold) + 1) ** 2

	#return 1
	return outSample * np.sign(inSample) #preserves sign


def softClip(sampleArr):
	numSamples = len(sampleArr)
	sampleArrOut = [[0] * 2 for i in range(numSamples)]

	for i in range(numSamples):
		sampleArrOut[i][0] = clippingFunction(sampleArr[i][0])
		sampleArrOut[i][1] = clippingFunction(sampleArr[i][1])

	return sampleArrOut



def main():
	fileName = 'TestAudioIn/sinC2.wav'
	sampleRate, sampleArr = wavfile.read(fileName)
	sr, sFlat = wavfile.read('TestAudioIn/silence.wav')

	#sampleArrClipped = softClip(sampleArr)

	#wavfile.write("test.wav", sampleRate, np.array(sampleArrClipped)) #need to convert to a numpy array for this function
	
	#graphSignal(sampleArr[:10])
	#graphSignal([[i*2 + 1, i*2 + 1] for i in range(10)])
	graphSignal([sampleArr, sFlat])

	#print("File Name:", fileName)
	#print("Frame Rate:", sampleRate)
	#print("Sample Array In:", sampleArr[0:100])
	#print("Sample Array Out :", sampleArrClipped[0:100])

def graphSignal(sampleArrs):
	print(sampleArrs)

	stepSize = 2

	#print(sampleArr)
			
	extractedChannel0 = list(map(lambda x: x[0]/MaxVal, sampleArrs))
	print(extractedChannel0)
	#extractedChannel0 = [item[0]/MaxVal for item in sampleArr] #scaling to (-1,1)
	skipNValues = extractedChannel0[::stepSize]
	print(skipNValues)
	#linSpace = np.linspace(0, len(skipNValues), len(sampleArrs)/stepSize)
	#interpolationSpace = np.linspace(0, len(skipNValues), len(sampleArrs))
	#linSpace = np.linspace(0, len(skipNValues), 1)
	#linSpace = range(0, len(extractedChannel0), stepSize)
	linSpace = list(range(0, len(extractedChannel0), stepSize))
	print(linSpace)
	#interpolationSpace = np.linspace(0, len(extractedChannel0), len(extractedChannel0))
	interpolationSpace = list(range(0, len(extractedChannel0)))

	#print(list(interpolationSpace))
	#print(len(linSpaceRep))
	#print(len(extractedChannel0))

	#print(list(linSpaceRep))

	splineRep = interpolate.splrep(linSpace, skipNValues, s="0")
	splineEval = interpolate.splev(interpolationSpace, splineRep)
	print(splineEval)

	#print(splineEval)

	#splineRep and splineEval arent matching up

	plt.plot(linSpace, skipNValues, marker = "x", linestyle = 'None')
	plt.plot(splineEval, marker = "o")
	plt.axis([0, 10, -1, 1])

					#testing git
					#testing git again


	'''for i, sampleArr in enumerate(sampleArrs):
					print(sampleArr)
			
					extractedChannel0 = list(map(lambda x: x/MaxVal, sampleArr))
					#extractedChannel0 = [item[0]/MaxVal for item in sampleArr] #scaling to (-1,1)
					skipNValues = extractedChannel0[::stepSize]
					linSpace = range(0, len(skipNValues))
					interpolationSpace = np.arange(0, len(skipNValues)-1, .1)
			
					#print(list(interpolationSpace))
					#print(len(linSpaceRep))
					#print(len(extractedChannel0))
			
					#print(list(linSpaceRep))
			
					splineRep = interpolate.splrep(linSpace, skipNValues, s="0")
					splineEval = interpolate.splev(interpolationSpace, splineRep, der=0)
			
					#splineRep and splineEval arent matching up
			
					plt.plot(skipNValues, marker = "x", linestyle = 'None')
					plt.plot(splineEval, marker = "o")
					plt.axis([0, 200, -1, 1])
			
					#testing git
					#testing git again
			'''
	
	plt.show()

main()

'''
Cades Clipper
	yOut = threshold - frac(threshold)(yIn +1)^power

Sigmoid Clipper
	yOut = (2*threshold)/1+e^(power*-yIn) - threshold

Bounce Clipper:
	Recursively mirrors yIn over threshold until yOut is inbetween the threshold values.
'''




'''
The following is tests regarding using the wave library
with wave.open('TestAudioIn/silence.wav', 'rb') as inFile:

	print ( "Number of channels",inFile.getnchannels())
	print ( "Sample width",inFile.getsampwidth())
	print ( "Frame rate.",inFile.getframerate())
	print ( "Number of frames",inFile.getnframes())
	print ( "parameters:",inFile.getparams())

	samplerate, data = wavfile.read('TestAudioIn/silence.wav')
	
	
	frame = inFile.setpos(100)
	f1 = inFile.readframes(1)
	f1Int = int.from_bytes(f1, "big")

	frame = inFile.setpos(50)
	f2 = inFile.readframes(1)
	f2Int = int.from_bytes(f2, "big")
	

	#print(frames)
	#print( f1Int)
	#print( f2Int)

'''
